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
        self.view_layer_selection.setMaximumWidth(400)

        self.ksh_report_result = ksh_report_result() #보링점
        self.ksh_report_result.setMinimumWidth(350)
        self.ksh_report_result.setMaximumWidth(400)

        self.ksh_height_setting = ksh_height_setting() #높이 설정
        self.ksh_height_setting.setMinimumWidth(350)
        self.ksh_height_setting.setMaximumWidth(400)

        self.ksh_information = ksh_information() #부재 정보 입력
        self.ksh_information.setMinimumWidth(350)
        self.ksh_information.setMaximumWidth(400)

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