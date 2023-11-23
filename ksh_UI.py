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
        
       
        # 기본 폰트---------------------------------------------------------------------------------------
        self.font = QFont()
        self.font.setBold(False)       # 굵게 설정            
        self.font.setFamily('맑은고딕')  # 원하는 폰트 패밀리로 변경
        self.font.setPointSize(int(self.width() / 70))  # 20은 크기 조절을 위한 임의의 비율 상수

        
        # 프로젝트 저장 탭 -------------------------------------------------------------------------------
        self.setAcceptDrops(True) 
        self.settings = QSettings()


        # menu, actions and toolbar
        self.setUnifiedTitleAndToolBarOnMac(True)
        toolbar = QToolBar("My main toolbar")
        toolbar.setFloatable(False)
        toolbar.setFont(self.font)
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        menu_bar = self.menuBar()
        file_menu = QMenu("&File", self)
        menu_bar.addMenu(file_menu)


        action_save = QAction("프로젝트 내보내기", self)
        action_save.setFont(self.font)
        action_save.triggered.connect(self.action_save_click)
        toolbar.addAction(action_save)
        file_menu.addAction(action_save)        
        



        
        
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