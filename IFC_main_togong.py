# import time
import os.path
from IFCCustomDelegate import *

from IFC_widget_3d_quantity import *
from IFC_widget_object import *
from IFC_widget_regist_constr import *
from IFC_widget_takeoff import *
from IFC_widget_property import *

from IFCListingWidget import *
from CustomDockWidget import *
import cnv_methods as cnv


class MainWindow(QMainWindow):
    def initUI(self):
        pass
        # # 여기에 창 UI 설정을 구성할 수 있습니다.
        # self.setWindowTitle('전체 화면 예제')
        # self.showFullScreen()  # 전체 화면으로 창을 표시합니다.
    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()


        # 공통 변수 설정---------------------------------------------------------------
        self.ifc_filename = ""
        self.ifc_files = {} # IFC파일을 담음 {filename:.ifc} 꼴로 담음 예를 들면 {"D:\sample.ifc":ifc파일정보}
        self.project_folder_path = "" #프로젝트 폴더 패스
        self.constr_item_list = [] #공사항목리스트(일위대가나 순수자원이나 그런 공사의 수량의 기준이되는 항목의 리스트)
        self.obj_constr_connect_list = [] #객체공산연결리스트
        self.obj_constr_quantity_list = [] # 객체와 공사항목간의 산식과 매개변수 맵핑에 관한 내용이 들어가 있는 리스트
        # //공통 변수 설정---------------------------------------------------------------



        self.current_selected_obj = None #객체리스트에서 현재 선택된 객체




        # QFont 객체 생성 및 스타일 설정
        font = QFont()
        font.setBold(True)       # 굵게 설정            
        font.setFamily('맑은고딕')  # 원하는 폰트 패밀리로 변경
        font.setPointSize(int(self.width() / 80))  # 20은 크기 조절을 위한 임의의 비율 상수





        ######

        
        self.setAcceptDrops(True) 
        self.settings = QSettings()

        self.USE_3D = self.settings.value('USE_3D', True) ##나중에확인

        # menu, actions and toolbar
        self.setUnifiedTitleAndToolBarOnMac(True)
        toolbar = QToolBar("My main toolbar")
        toolbar.setFloatable(False)
        toolbar.setFont(font)
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        menu_bar = self.menuBar()
        file_menu = QMenu("&File", self)
        menu_bar.addMenu(file_menu)

        action_ifc_open = QAction("IFC 파일 열기", self)
        action_ifc_open.setShortcut("CTRL+O")
        action_ifc_open.setFont(font)
        action_ifc_open.triggered.connect(self.action_ifc_open_click)
        toolbar.addAction(action_ifc_open)
        file_menu.addAction(action_ifc_open)

        action_select_project_folder = QAction("프로젝트폴더 선택", self)
        action_select_project_folder.setFont(font)
        action_select_project_folder.triggered.connect(self.action_select_project_folder_click)
        toolbar.addAction(action_select_project_folder)
        file_menu.addAction(action_select_project_folder)

        action_input_constr_template = QAction("공사템플릿 가져오기", self)
        action_input_constr_template.setFont(font)
        action_input_constr_template.triggered.connect(self.action_input_constr_template_click)
        toolbar.addAction(action_input_constr_template)
        file_menu.addAction(action_input_constr_template)

        action_save = QAction("프로젝트 저장", self)
        action_save.setFont(font)
        action_save.triggered.connect(self.action_save_click)
        toolbar.addAction(action_save)
        file_menu.addAction(action_save)

        # action_calc_all_quantity = QAction("전체수량계산", self)
        # action_calc_all_quantity.setFont(font)
        # action_calc_all_quantity.triggered.connect(self.action_calc_all_quantity_click)
        # toolbar.addAction(action_calc_all_quantity)
        # file_menu.addAction(action_calc_all_quantity)
        
        # action_quit = QAction("종료", self)
        # action_quit.setFont(font)
        # action_quit.triggered.connect(qApp.quit)
        # file_menu.addAction(action_quit)


        # 위젯 생성-------------------------------------------------------------------------------------
        
        self.view_3d_quantity = IFC_widget_3d_quantity() #메인위젯
        
        self.view_object = IFC_widget_object()  #객체리스트 위젯
        self.view_object.setMinimumSize(500,500)

        self.view_properties = IFC_widget_property() #객체정보 위젯
        self.view_properties.setMinimumSize(600,500)

        self.view_regist_constr = IFC_widget_regist_constr() #공사등록 위젯
        self.view_regist_constr.setMinimumSize(600,500)

        self.view_takeoff = IFC_widget_takeoff() #수량추출 위젯
        self.view_takeoff.setMinimumSize(300,500)



        # /위젯 생성-------------------------------------------------------------------------------------


        # 객체선택시 모두 싱크해서 위치를 판단할 수 있도록 하는 코드 
        self.view_regist_constr.send_constr_code_for_connect.connect(self.add_constr_item_to_obj_from_child) #cnv
        
        self.view_object.select_object.connect(self.input_current_selected_obj_from_treeview)

        self.view_object.select_object.connect(self.view_3d_quantity.select_object_by_id)
        self.view_object.deselect_object.connect(self.view_3d_quantity.deselect_object_by_id)
        self.view_3d_quantity.add_to_selected_entities.connect(self.view_object.receive_selection)
        self.view_3d_quantity.add_to_selected_entities.connect(self.view_regist_constr.receive_selection)
        self.view_3d_quantity.add_to_selected_entities.connect(self.view_takeoff.receive_selection)
        self.view_takeoff.select_object.connect(self.view_3d_quantity.select_object_by_id)
        # self.view_takeoff.deselect_object.connect(self.view_3d_quantity.deselect_object_by_id)

        # from tree to other views
        self.view_object.send_selection_set.connect(self.view_properties.set_from_selected_items)
        self.view_object.select_object.connect(self.view_takeoff.receive_selection)
        
        # send from takeoff to other views
        self.view_takeoff.select_object.connect(self.view_object.receive_selection)
        # self.view_takeoff.deselect_object.connect(self.view_object.receive_selection)

        # Update Syncing
        self.view_properties.send_update_object.connect(self.view_object.receive_object_update)





        # Docking Widgets
        
     
        self.dock = CustomDockWidget('객체', self)
        self.dock.setWidget(self.view_object)
        self.dock.setFloating(False)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock)


        self.dock2 = CustomDockWidget('객체 데이터', self)
        self.dock2.setWidget(self.view_properties)
        self.dock2.setFloating(False)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock2)

        self.dock3 = CustomDockWidget('공사 연결', self)
        self.dock3.setWidget(self.view_regist_constr)
        self.dock3.setFloating(False)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock3)

        # self.dock3 = CustomDockWidget('수량 추출', self)
        # self.dock3.setWidget(self.view_takeoff)
        # self.dock3.setFloating(False)
        # self.addDockWidget(Qt.BottomDockWidgetArea, self.dock3)

        # Main Widget
        
        self.setCentralWidget(self.view_3d_quantity)
        



    ##region File Methods




    

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            for f in urls:
                filepath = str(f.path())
                # only .ifc files are acceptable
                if os.path.isfile(filepath) and os.path.splitext(filepath)[1] == '.ifc':
                    self.load_ifc_file(filepath)
                else:
                    dialog = QMessageBox()
                    dialog.setWindowTitle("Error: Invalid File")
                    dialog.setText(str("Only .ifc files are accepted.\nYou dragged {}").format(filepath))
                    dialog.setIcon(QMessageBox.Warning)
                    dialog.exec_()

    def reload_ifc_files(self):
        """
        Reload all currently open files
        """
        for ifc_filename, ifc_file in self.ifc_files.items():
            self.load_ifc_file(ifc_filename)
        self.view_3d_quantity.obj_constr_connect_list = self.obj_constr_connect_list

    def save_files(self):
        """
        Save all currently loaded files
        """
        for ifc_filename, ifc_file in self.ifc_files.items():

            dlg = QMessageBox(self.parent())
            dlg.setWindowTitle("Confirm file save")
            dlg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            dlg.setText(str("Do you want to save:\n{}?").format(ifc_filename))
            dlg.setDetailedText(str("When you click 'OK', you still have the chance of"
                                    "selecting a new name or location."))
            button = dlg.exec_()
            if button == QMessageBox.Ok:
                savepath = QFileDialog.getSaveFileName(self, caption="Save IFC File",
                                                       directory=ifc_filename,
                                                       filter="IFC files (*.ifc)")
                if savepath[0] != '':
                    ifc_file.write(savepath[0])


    def action_calc_all_quantity_click(self):
        """
        Close all loaded files (and clear the different views)
        """
        self.ifc_files = {}
        self.view_object.action_calc_all_quantity_click()
        self.view_properties.reset()
        if self.USE_3D:
            self.view_3d_quantity.action_calc_all_quantity_click()
        self.view_takeoff.action_calc_all_quantity_click()
        self.setWindowTitle("IFC Viewer")

    def toggle_use_3d(self):
        self.USE_3D = not self.USE_3D
        self.settings.setValue("USE_3D", self.USE_3D)











    ##region cnv 추가 메소드

    def input_current_selected_obj_from_treeview(self, obj_id):
        self.current_selected_obj = obj_id
        self.view_regist_constr.object_tree.clear()
        for item in self.obj_constr_connect_list:
            if(item[0] == obj_id):
                for con_code in item[1]:
                    for all_con_data in self.constr_item_list:
                        if all_con_data["공사코드"] == con_code:
                            
                            root = QTreeWidgetItem(self.view_regist_constr.object_tree)
                            root.setText(0, all_con_data["공종"])
                            root.setText(1, all_con_data["품명"])
                            root.setText(2, all_con_data["규격"])
                            root.setData(0,Qt.UserRole,all_con_data)
                            print(root.data(0,Qt.UserRole)["공사코드"])


    def add_constr_item_to_obj_from_child(self, constr_item_code):
        
        
        print("공사코드"+constr_item_code)
        print("객체id"+self.current_selected_obj)
        print("공사연결리스트"+str(self.obj_constr_connect_list))

        is_exsit = False
        for item in self.obj_constr_connect_list:
            if(item[0] == self.current_selected_obj):
                is_exsit = True
                break

        if is_exsit == True:
            item[1].append(constr_item_code)
        else:
            self.obj_constr_connect_list.append([self.current_selected_obj,[constr_item_code]])
        
        
        self.input_current_selected_obj_from_treeview(self.current_selected_obj)
        
        self.view_3d_quantity.obj_constr_connect_list = self.obj_constr_connect_list
        self.view_3d_quantity.reset_view_quantity()


        pass



    def reset_connect_constr_combobox(self):
        self.view_regist_constr.constr_item_chooser.clear()
        for item in self.constr_item_list:
            self.view_regist_constr.constr_item_chooser.addItem(item['공사코드']+"-"+item['공종']+"-"+item['품명']+"-"+item['규격'])

    def add_constr_item_from_child(self, a, b, c, d, e):
        is_exist = False
        for item in self.view_3d_quantity.constr_item_list:
            if a == item["공사코드"]:
                is_exsit = True
        if is_exist == False:
            self.constr_item_list.append({"공사코드":a,"공종":b,"품명":c, "규격" : d,"단위":e})
            self.view_3d_quantity.constr_item_list = self.constr_item_list
            self.view_object.constr_item_list = self.constr_item_list
            self.view_properties.constr_item_list = self.constr_item_list
            self.view_regist_constr.constr_item_list = self.constr_item_list
            self.view_takeoff.constr_item_list = self.constr_item_list

            self.view_3d_quantity.reset_view_quantity()
        self.reset_connect_constr_combobox()

    # 프로젝트 저장 버튼을 클릭했을 때 발생할 메소드========================================================
    def action_save_click(self):
        print(self.project_folder_path + "constr_item_list.json")
        cnv.save_json(self.constr_item_list, self.project_folder_path + "constr_item_list.json")
        cnv.save_json(self.obj_constr_connect_list, self.project_folder_path + "obj_constr_connect_list.json")
        cnv.save_json(self.obj_constr_quantity_list, self.project_folder_path + "obj_constr_quantity_list.json")





    # / 프로젝트 저장 버튼을 클릭했을 때 발생할 메소드========================================================

    # 공사템플릿 적용 버튼을 클릭했을 때 발생할 메소드====================================================================== 

    def action_input_constr_template_click(self):
        filenames, filter_string = QFileDialog.getOpenFileNames(self, caption="Open File",
                                                                filter=" (*.json)")

        try:
            for template_item in cnv.load_json(filenames[0]):
                is_exist = False
                for current_item in self.constr_item_list:
                    if current_item["공사코드"] == template_item["공사코드"]:
                        is_exist = True
                if is_exist == False:
                    self.constr_item_list.append(template_item)
                    self.view_3d_quantity.constr_item_list = self.constr_item_list
                    self.view_3d_quantity.reset_view_quantity(template_item)
            self.reset_connect_constr_combobox()
        except:
            print("공사템플릿 파일을 가져올 수 없음")

 
    # / 공사템플릿 적용 버튼을 클릭했을 때 발생할 메소드====================================================================== 

    # 프로젝트폴더 선택 버튼을 클릭했을 때 발생할 메소드====================================================================== 

    def action_select_project_folder_click(self):
        project_folder_path = cnv.select_folder()
        self.project_folder_path = project_folder_path
        self.view_3d_quantity.project_folder_path = project_folder_path
        self.view_object.project_folder_path = project_folder_path
        self.view_properties.project_folder_path = project_folder_path
        self.view_regist_constr.project_folder_path = project_folder_path
        self.view_takeoff.project_folder_path = project_folder_path


        #폴더안에 필요한 파일을 확인하고 담는 작업을 해야함
        try:
            file = self.project_folder_path+"constr_item_list.json"
            self.constr_item_list = cnv.load_json(file)
            self.view_3d_quantity.constr_item_list = self.constr_item_list
            self.view_object.constr_item_list = self.constr_item_list
            self.view_properties.constr_item_list = self.constr_item_list
            self.view_regist_constr.constr_item_list = self.constr_item_list
            self.view_takeoff.constr_item_list = self.constr_item_list

        except:
            print("constr_item_list.json maybe none")

        try:
            file = self.project_folder_path+"obj_constr_connect_list.json"
            self.obj_constr_connect_list = cnv.load_json(file)
            self.view_3d_quantity.obj_constr_connect_list = self.obj_constr_connect_list
            self.view_object.obj_constr_connect_list = self.obj_constr_connect_list
            self.view_properties.obj_constr_connect_list = self.obj_constr_connect_list
            self.view_regist_constr.obj_constr_connect_list = self.obj_constr_connect_list
            self.view_takeoff.obj_constr_connect_list = self.obj_constr_connect_list

        except:
            print("obj_constr_connect_list.json maybe none")
            self.obj_constr_connect_list.append( ["객체아이디",["공사코드"]])
            self.view_takeoff.obj_constr_connect_list.append( ["객체아이디",["공사코드"]])
            print("실행확인")
        try:
            file = self.project_folder_path+"obj_constr_quantity_list.json"
            self.obj_constr_quantity_list = cnv.load_json(file)
            self.view_3d_quantity.obj_constr_quantity_list = self.obj_constr_quantity_list
            self.view_object.obj_constr_quantity_list = self.obj_constr_quantity_list
            self.view_properties.obj_constr_quantity_list = self.obj_constr_quantity_list
            self.view_regist_constr.obj_constr_quantity_list = self.obj_constr_quantity_list
            self.view_takeoff.obj_constr_quantity_list = self.obj_constr_quantity_list

        except:
            print("obj_constr_quantity_list.json maybe none")

        ## 공사리스트를 3d_quantity 위젯의 treeview에 담는데 객체도 연동 데이터가 있으면 같이 담고 수량도 같이 담음
        self.view_3d_quantity.reset_view_quantity()
        self.reset_connect_constr_combobox()



    # //프로젝트폴더 선택 버튼을 클릭했을 때 발생할 메소드====================================================================== 





    #IFC파일열기 버튼을 클릭했을 때 발생할 메소드====================================================================== 
    def action_ifc_open_click(self):

        filenames, filter_string = QFileDialog.getOpenFileNames(self, caption="Open IFC File",
                                                                filter="IFC files (*.ifc)")

        # self.setWindowTitle("IFC Viewer")
        for file in filenames:
            if os.path.isfile(file):
                if self.load_ifc_file(file):
                    # Concatenate all file names
                    title = "BIM 수량산출"
                    for filename, file in self.ifc_files.items():
                        title += " - " + os.path.basename(filename)
                    if len(title) > 64:
                        title = title[:64] + "..."
                    self.setWindowTitle(title)

    def load_ifc_file(self, filename):

            if filename in self.ifc_files:
                # Display warning that this model was already loaded. Replace or Cancel.
                dlg = QMessageBox(self.parent())
                dlg.setWindowTitle("Model already loaded!")
                dlg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                dlg.setIcon(QMessageBox.Warning)
                dlg.setText(str("Do you want to replace the currently loaded model?\n"
                                "{}").format(filename))
                button = dlg.exec_()
                if button == QMessageBox.Cancel:
                    return False
                
            #ifc모델 오픈후 메인윈도우, 3d_quantity위젯, object위젯의 ifc_files 변수에 저장 및 load_ifc_file메소드 실행
            ifc_file = ifcopenshell.open(filename)
            self.ifc_filename = filename
            self.view_3d_quantity.ifc_filename = filename
            self.ifc_files[filename] = ifc_file

            self.view_3d_quantity.ifc_files[filename] = ifc_file
            self.view_3d_quantity.load_ifc_file(filename)

            self.view_object.ifc_files[filename] = ifc_file
            self.view_object.load_ifc_file(filename)
            

            

            #나머지 위젯에도 ifc_file 저장
            self.view_properties.ifc_files[filename] = ifc_file
            self.view_regist_constr.ifc_files[filename] = ifc_file
            self.view_takeoff.ifc_files[filename] = ifc_file

            return True
    # //IFC파일열기 버튼을 클릭했을 때 발생할 메소드====================================================================== 

        










# Our Main function
def main():
    app = 0
    if QApplication.instance():
        app = QApplication.instance()
    else:
        app = QApplication(sys.argv)
    app.setApplicationDisplayName("BIM Estimator")
    app.setOrganizationName("CNV")
    app.setOrganizationDomain("cnvarchiplan.com")
    app.setApplicationName("BIM Estimator")

    w = MainWindow()
    w.setWindowTitle("BIM Estimator")
    # w.resize(1920, 1080)
    filename = sys.argv[1] if len(sys.argv) >= 2 else ''
    if os.path.isfile(filename):
        w.load_ifc_file(filename)
        w.setWindowTitle(w.windowTitle() + " - " + os.path.basename(filename))
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
