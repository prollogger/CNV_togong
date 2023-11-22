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


class ksh_information(QWidget):

    
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
        vbox.addWidget(self.Group3())
        
    
    #그룹박스 - 파일 ------------------------------------------------------------------------   
    def Group1(self):
        groupbox = QGroupBox('지형')
        
         # 탭 위젯 생성
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, 'PRD')
        tabs.addTab(tab2, 'RCD')
        tabs.addTab(tab3, 'PHC')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        groupbox.setLayout(vbox)  # 그룹박스에 레이아웃 설정
        
        return groupbox
    
    
    #그룹박스 - 흙막이 ------------------------------------------------------------------------    
    def Group2(self):
        groupbox = QGroupBox('지형')
        
         # 탭 위젯 생성
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab4 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, 'CIP')
        tabs.addTab(tab2, 'PILE')
        tabs.addTab(tab3, 'H-PILE')
        tabs.addTab(tab4, '슬러리월')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        groupbox.setLayout(vbox)  # 그룹박스에 레이아웃 설정
        
        return groupbox
    

    #그룹박스 - 버팀대 ------------------------------------------------------------------------    
    def Group3(self):
        groupbox = QGroupBox('지형')
        
         # 탭 위젯 생성
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab4 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, '센터파일')
        tabs.addTab(tab2, '어스앵커')
        tabs.addTab(tab3, '스트러트')
        tabs.addTab(tab4, '띠장')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        groupbox.setLayout(vbox)  # 그룹박스에 레이아웃 설정
        
        return groupbox

if __name__ == '__main__':
    app = 0
    if QApplication.instance():
        app = QApplication.instance()
    else:
        app = QApplication(sys.argv)

    w = ksh_information()
    w.resize(600, 800)
    filename = sys.argv[1]
    if os.path.isfile(filename):
        w.load_ifc_file(filename)
        w.show()
    sys.exit(app.exec_())
