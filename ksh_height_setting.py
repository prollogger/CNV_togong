import sys
import os.path
import cnv_methods as cnv
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


class ksh_height_setting(QWidget):

    
    def __init__(self):
        QWidget.__init__(self)
        self.initUI()  # initUI 메서드 호출
      
    def initUI(self):
        
        # 수직 박스 레이아웃 생성
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        
        # 공간 확보
        spacer = QSpacerItem(0, 53, QSizePolicy.Fixed, QSizePolicy.Fixed)
        vbox.addSpacerItem(spacer)   

        # 그룹박스 생성
        vbox.addWidget(self.Group1())
        vbox.addWidget(self.Group2())

    
    #그룹박스 - 지형    
    def Group1(self):
        groupbox = QGroupBox('스트러트 높이 설정')
        

        
        return groupbox
    
    
    #그룹박스 - 부재  
    def Group2(self):
        groupbox = QGroupBox('터파기 높이 설정')

        

        return groupbox



if __name__ == '__main__':
    app = 0
    if QApplication.instance():
        app = QApplication.instance()
    else:
        app = QApplication(sys.argv)

    w = ksh_height_setting()
    w.resize(600, 800)
    filename = sys.argv[1]
    if os.path.isfile(filename):
        w.load_ifc_file(filename)
        w.show()
    sys.exit(app.exec_())
