import sys
import os.path

try:
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
except Exception:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *

import ifcopenshell
from IFCCustomDelegate import *


class IFC_widget_takeoff(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        
        # 공통 변수 설정---------------------------------------------------------------
        self.ifc_files = {} # IFC파일을 담음 {filename:.ifc} 꼴로 담음 예를 들면 {"D:\sample.ifc":ifc파일정보}
        self.project_folder_path = None #프로젝트 폴더 패스
        self.constr_item_list = [] #공사항목리스트(일위대가나 순수자원이나 그런 공사의 수량의 기준이되는 항목의 리스트)
        self.obj_constr_connect_list = [] #객체공산연결리스트
        self.obj_constr_quantity_list = [] # 객체와 공사항목간의 산식과 매개변수 맵핑에 관한 내용이 들어가 있는 리스트
        # //공통 변수 설정---------------------------------------------------------------

        
        # QFont 객체 생성 및 스타일 설정
        font = QFont()
        font.setBold(True)       # 굵게 설정            
        font.setFamily('맑은고딕')  # 원하는 폰트 패밀리로 변경
        font.setPointSize(int(self.width() / 80))  # 20은 크기 조절을 위한 임의의 비율 상수

        # Prepare Tree Widgets in a stretchable layout
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        # Series of buttons and check boxes in a horizontal layout
        buttons = QWidget()
        vbox.addWidget(buttons)
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        buttons.setLayout(hbox)
        
        
        # 입력창
        self.root_class_chooser = QLineEdit()
        self.root_class_chooser.setFont(font)
        self.root_class_chooser.setToolTip("Select the top level class to display in the tree")
        self.root_class_chooser.setMinimumWidth(150)
        hbox.addWidget(self.root_class_chooser)
        self.root_class_chooser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed) 
        
        # 공간 확보
        spacer = QSpacerItem(5,5, QSizePolicy.Fixed, QSizePolicy.Fixed)
        hbox.addSpacerItem(spacer)   
        
        
        #버튼
        self.btn3 = QPushButton("산식 추가")
        self.btn3.setFont(font)
        hbox.addWidget(self.btn3)
        self.btn3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed) 
        
        self.btn4 = QPushButton("객체변수입력")
        self.btn4.setFont(font)
        hbox.addWidget(self.btn4)
        self.btn4.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed) 


        # Object Tree
        self.object_tree = QTreeWidget()
        vbox.addWidget(self.object_tree)
        self.object_tree.setColumnCount(2)
        self.object_tree.setHeaderLabels(["이름", "객체매개변수"])
        self.object_tree.setFont(font)
       # 모든 열의 크기를 동일하게 만들기 위해 각 열의 크기 조절 모드 설정
        for i in range(self.object_tree.columnCount()):
            self.object_tree.header().setSectionResizeMode(i, QHeaderView.Stretch)
        self.object_tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.object_tree.selectionModel().selectionChanged.connect(self.send_selection)
        self.object_tree.itemDoubleClicked.connect(self.check_object_name_edit)
        self.object_tree.itemChanged.connect(self.set_object_name_edit)
        self.object_tree.header().setDefaultAlignment(Qt.AlignHCenter)
        
    # region Selection Methods

    select_object = pyqtSignal(object)
    deselect_object = pyqtSignal(object)
    send_selection_set = pyqtSignal(object)


    def send_selection(self, selected_items, deselected_items):
        items = self.object_tree.selectedItems()
        self.send_selection_set.emit(items)
        for item in items:
            entity = item.data(0, Qt.UserRole)
            if hasattr(entity, "GlobalId"):
                GlobalId = entity.GlobalId
                if GlobalId != '':
                    self.select_object.emit(GlobalId)
                    print("IFCTreeWidget.send_selection.select_object ", GlobalId)

        # send the deselected items as well
        for index in deselected_items.indexes():
            if index.column() == 0:  # only for first column, to avoid repeats
                item = self.object_tree.itemFromIndex(index)
                entity = item.data(0, Qt.UserRole)
                if hasattr(entity, "GlobalId"):
                    GlobalId = entity.GlobalId
                    if GlobalId != '':
                        self.deselect_object.emit(GlobalId)
                        print("IFCTreeWidget.send_selection.deselect_object ", GlobalId)

    def receive_selection(self, ids):
        print("IFCTreeWidget.receive_selection ", ids)
        self.object_tree.clearSelection()
        if not len(ids):
            return
        # TODO: this may take a while in large trees - should we have a cache?
        iterator = QTreeWidgetItemIterator(self.object_tree)
        while iterator.value():
            item = iterator.value()
            entity = item.data(0, Qt.UserRole)
            if entity is not None and hasattr(entity, "GlobalId"):
                if entity.GlobalId == ids:
                    item.setSelected(not item.isSelected())
                    index = self.object_tree.indexFromItem(item)
                    self.object_tree.scrollTo(index)
            iterator += 1

    def receive_object_update(self, ifc_object):
        iterator = QTreeWidgetItemIterator(self.object_tree)
        while iterator.value():
            item = iterator.value()
            entity = item.data(0, Qt.UserRole)
            if entity == ifc_object:
                # refresh my name
                item.setText(0, ifc_object.Name)
            iterator += 1

    # endregion

    # region File Methods

    def close_files(self):
        self.ifc_files.clear()
        self.object_tree.clear()
        self.prepare_chooser()

    def load_ifc_file(self, filename):
        """
        Load the file passed as filename and builds the whole object tree.
        If it already exists, that branch is removed and recreated.

        :param filename: Full path to the IFC file
        """
        ifc_file = None
        if filename in self.ifc_files:
            ifc_file = self.ifc_files[filename]
            for i in range(self.object_tree.topLevelItemCount()):
                toplevel_item = self.object_tree.topLevelItem(i)
                if toplevel_item is not None and filename == toplevel_item.text(0):
                    root = self.object_tree.invisibleRootItem()
                    root.removeChild(toplevel_item)
        else:  # Load as new file
            ifc_file = ifcopenshell.open(filename)
            self.ifc_files[filename] = ifc_file

        self.prepare_chooser()
        self.add_objects(filename)

    # endregion

    # region Object Tree Methods

    def add_objects(self, filename):
        """Fill the Object Tree with TreeItems representing Entity Instances

        :param filename: The filename for a loaded IFC model (in the files dictionary)
        :type filename: str
        """
        ifc_file = self.ifc_files[filename]
        root_item = QTreeWidgetItem([filename, 'File'])
        root_item.setData(0, Qt.UserRole, ifc_file)
        try:
            for item in ifc_file.by_type(self.root_class):
                self.add_object_in_tree(item, root_item)
        except:
            dlg = QMessageBox(self.parent())
            dlg.setWindowTitle("Invalid IFC Class!")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.setText(str("{} is not a valid class name.\nSuggestions are IfcProject or IfcWall.").format(self.root_class))
            dlg.exec_()
        # Finish the GUI
        self.object_tree.addTopLevelItem(root_item)
        self.object_tree.expandToDepth(3)

    def add_object_in_tree(self, ifc_object, parent_item):
        """
        Fill the Object Tree recursively with Objects and their
        children, as defined by the relationships

        :param ifc_object: an IFC entity instance
        :type ifc_object: entity_instance
        :param parent_item: the parent QTreeWidgetItem
        :type parent_item: QTreeWidgetItem
        """
        my_name = ifc_object.Name if hasattr(ifc_object, "Name") else ""
        tree_item = QTreeWidgetItem([my_name, ifc_object.is_a()])
        parent_item.addChild(tree_item)
        tree_item.setData(0, Qt.UserRole, ifc_object)
        tree_item.setToolTip(0, entity_summary(ifc_object))

        if self.follow_decomposition:
            if hasattr(ifc_object, 'ContainsElements'):
                for rel in ifc_object.ContainsElements:
                    for element in rel.RelatedElements:
                        self.add_object_in_tree(element, tree_item)
            if hasattr(ifc_object, 'IsDecomposedBy'):
                for rel in ifc_object.IsDecomposedBy:
                    for related_object in rel.RelatedObjects:
                        self.add_object_in_tree(related_object, tree_item)
            if hasattr(ifc_object, 'IsGroupedBy'):
                for rel in ifc_object.IsGroupedBy:
                    if hasattr(rel, 'RelatedObjects'):
                        for related_object in rel.RelatedObjects:
                            self.add_object_in_tree(related_object, tree_item)
            if hasattr(ifc_object, 'AssignedItems'):  # objects on layers
                for rep in ifc_object.AssignedItems:
                    # self.add_object_in_tree(rep, tree_item)
                    # From Shape Representation to Product Definition Shape to Product?
                    for prod_def_shape in rep.OfProductRepresentation:
                        for prod in prod_def_shape.ShapeOfProduct:
                            self.add_object_in_tree(prod, tree_item)

    def set_object_name_edit(self, item, column):
        """
        Send the change back to the item

        :param item: QTreeWidgetItem
        :param int column: Column index
        :return:
        """
        if item.text(1) == 'File':
            return
        ifc_object = item.data(0, Qt.UserRole)
        if ifc_object is not None:
            if hasattr(ifc_object, "Name"):
                ifc_object.Name = item.text(0)
                # warn other views/widgets
                items = self.object_tree.selectedItems()
                self.send_selection_set.emit(items)

    def check_object_name_edit(self, item, column):
        """
        Check whether this item can be edited

        :param item: QTreeWidgetItem
        :param column: Column index
        :return:
        """
        if item.text(1) == 'File':
            return

        tmp = item.flags()
        if column == 0:
            item.setFlags(tmp | Qt.ItemIsEditable)
        elif tmp & Qt.ItemIsEditable:
            item.setFlags(tmp ^ Qt.ItemIsEditable)

    # endregion

    # region UI Methods

    def toggle_decomposition(self):
        self.follow_decomposition = not self.follow_decomposition
        self.regenerate_tree()

    def toggle_chooser(self, text):
        self.root_class = self.root_class_chooser.currentText()
        self.regenerate_tree()

    def prepare_chooser(self):
        buffer = self.root_class_chooser.currentText()
        if buffer == '':
            buffer = 'IfcProject'
        self.root_class_chooser.clear()
        for _, file in self.ifc_files.items():
            for t in file.wrapped_data.types():
                if self.root_class_chooser.findText(t, Qt.MatchFixedString) == -1:  # require exact matching!
                    self.root_class_chooser.addItem(t)

        # Add all available classes in the Combobox
        self.root_class_chooser.setEditable(False)
        self.root_class_chooser.model().sort(0, Qt.AscendingOrder)
        self.root_class_chooser.setCurrentText(buffer)

    def regenerate_tree(self):
        self.object_tree.clear()
        for filename, file in self.ifc_files.items():
            self.add_objects(filename)

    # endregion


if __name__ == '__main__':
    app = 0
    if QApplication.instance():
        app = QApplication.instance()
    else:
        app = QApplication(sys.argv)

    w = IFC_widget_takeoff()
    w.resize(600, 800)
    filename = sys.argv[1]
    if os.path.isfile(filename):
        w.load_ifc_file(filename)
        w.show()
    sys.exit(app.exec_())
