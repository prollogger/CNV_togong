# import time
import os.path
from IFCCustomDelegate import *

from IFC_widget_3d_quantity import *
from ksh_layer_selection import *
from ksh_report_result import *
from ksh_height_setting import *
from ksh_information import *

from IFCListingWidget import *
from CustomDockWidget import *
import cnv_methods as cnv


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        
        # 위젯 생성-------------------------------------------------------------------------------------
        
        self.view_3d_quantity = IFC_widget_3d_quantity() #메인위젯
        
        self.view_layer_selection = ksh_layer_selection() #레이어 지정
        self.view_layer_selection.setMinimumWidth(350)
        self.view_layer_selection.setMaximumWidth(800)

        self.ksh_report_result = ksh_report_result() #보링점
        self.ksh_report_result.setMinimumWidth(350)
        self.ksh_report_result.setMaximumWidth(800)

        self.ksh_height_setting = ksh_height_setting() #높이 설정
        self.ksh_height_setting.setMinimumWidth(350)
        self.ksh_height_setting.setMaximumWidth(800)

        self.ksh_information = ksh_information() #부재 정보 입력
        self.ksh_information.setMinimumWidth(350)
        self.ksh_information.setMaximumWidth(800)

        # 위젯 배치------------------------------------------------------------------------------------
        
        self.dock = CustomDockWidget('3D', self)
        self.dock.setWidget(self.view_3d_quantity)
        self.dock.setFloating(False)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock)

        self.dock2 = CustomDockWidget('레이어 선택', self)
        self.dock2.setWidget(self.view_layer_selection)
        self.dock2.setFloating(False)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock2)

        self.dock3 = CustomDockWidget('시추조사 결과 입력', self)
        self.dock3.setWidget(self.ksh_report_result)
        self.dock3.setFloating(False)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock3)

        self.dock4 = CustomDockWidget('높이 설정', self)
        self.dock4.setWidget(self.ksh_height_setting)
        self.dock4.setFloating(False)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock4)

        self.dock5 = CustomDockWidget('부재 정보 입력', self)
        self.dock5.setWidget(self.ksh_information)
        self.dock5.setFloating(False)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock5)
        
        
        # 프로젝트 저장 탭(툴바 생성) -------------------------------------------------------------------------------
        self.setUnifiedTitleAndToolBarOnMac(True)
        toolbar = CNV_ToolBar("My main toolbar")
        toolbar.setFloatable(False)
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        
        # 메뉴바
        #menu_bar = self.menuBar()
        #file_menu = QMenu("&File", self)
        #menu_bar.addMenu(file_menu)

        # 프로젝트 내보내기 --------------------------------------------------------------------------
        action_save = QAction("프로젝트 내보내기", self)
        action_save.triggered.connect(self.action_save_click)
        toolbar.addAction(action_save)        
        
        
        # 체크박스(위젯가시성) -----------------------------------------------------------------------
        
        # 공간 확보
        spacer_widget = QWidget()
        spacer_widget.setFixedWidth(20)  # 너비 조절을 통해 간격 조정
        toolbar.addWidget(spacer_widget)        
        
        # 체크박스 1
        self.check_1 = CNV_CheckBox("3D View")
        self.check_1.stateChanged.connect(self.toggle_1)
        self.check_1.setChecked(True)  # 체크박스 초기에 선택된 상태로 설정
        toolbar.addWidget(self.check_1)
        
        # 공간 확보
        spacer_widget = QWidget()
        spacer_widget.setFixedWidth(20)  # 너비 조절을 통해 간격 조정
        toolbar.addWidget(spacer_widget)        
        
        # 체크박스 2
        self.check_2 = CNV_CheckBox("레이어 선택")
        self.check_2.stateChanged.connect(self.toggle_2)
        self.check_2.setChecked(True)  # 체크박스 초기에 선택된 상태로 설정
        toolbar.addWidget(self.check_2)
        
        # 공간 확보
        spacer_widget = QWidget()
        spacer_widget.setFixedWidth(20)  # 너비 조절을 통해 간격 조정
        toolbar.addWidget(spacer_widget)        
        
        # 체크박스 3
        self.check_3 = CNV_CheckBox("시추조사 결과 입력")
        self.check_3.stateChanged.connect(self.toggle_3)
        self.check_3.setChecked(True)  # 체크박스 초기에 선택된 상태로 설정
        toolbar.addWidget(self.check_3)
        
        # 공간 확보
        spacer_widget = QWidget()
        spacer_widget.setFixedWidth(20)  # 너비 조절을 통해 간격 조정
        toolbar.addWidget(spacer_widget)        
        
        # 체크박스 4
        self.check_4 = CNV_CheckBox("높이 설정")
        self.check_4.stateChanged.connect(self.toggle_4)
        self.check_4.setChecked(True)  # 체크박스 초기에 선택된 상태로 설정
        toolbar.addWidget(self.check_4)
        
        # 공간 확보
        spacer_widget = QWidget()
        spacer_widget.setFixedWidth(20)  # 너비 조절을 통해 간격 조정
        toolbar.addWidget(spacer_widget)        
        
        # 체크박스 5
        self.check_5 = CNV_CheckBox("부재 정보 입력")
        self.check_5.stateChanged.connect(self.toggle_5)
        self.check_5.setChecked(True)  # 체크박스 초기에 선택된 상태로 설정
        toolbar.addWidget(self.check_5)
        
        
        #메뉴바
        #file_menu.addAction(action_save)        
        
        
        
    # 체크박스 상태 변화 함수 정의--------------------------------------------------------------
    
    def toggle_1(self, state):
        # 체크박스 상태에 따라 view_3d_quantity 위젯의 가시성을 설정
        self.dock.setVisible(state == Qt.Checked)        
            
    def toggle_2(self, state):
        # 체크박스 상태에 따라 view_3d_quantity 위젯의 가시성을 설정
        self.dock2.setVisible(state == Qt.Checked)        
    
    def toggle_3(self, state):
        # 체크박스 상태에 따라 view_3d_quantity 위젯의 가시성을 설정
        self.dock3.setVisible(state == Qt.Checked)        
    
    def toggle_4(self, state):
        # 체크박스 상태에 따라 view_3d_quantity 위젯의 가시성을 설정
        self.dock4.setVisible(state == Qt.Checked)        
    
    def toggle_5(self, state):
        # 체크박스 상태에 따라 view_3d_quantity 위젯의 가시성을 설정
        self.dock5.setVisible(state == Qt.Checked)        

        
        
    # 프로젝트 저장 이벤트-------------------------------------------------------------------------------
    
    def action_save_click(self):
        print(self.project_folder_path + "constr_item_list.json")
        cnv.save_json(self.constr_item_list, self.project_folder_path + "constr_item_list.json")
        cnv.save_json(self.obj_constr_connect_list, self.project_folder_path + "obj_constr_connect_list.json")
        cnv.save_json(self.obj_constr_quantity_list, self.project_folder_path + "obj_constr_quantity_list.json")
        
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