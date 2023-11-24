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
from ksh_style import *

class ksh_height_setting(QWidget):

    
    def __init__(self):
        QWidget.__init__(self)
        self.initUI()  # initUI 메서드 호출
      
    def initUI(self):
        
        # 수직 박스 레이아웃 생성
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        # 그룹박스 생성
        vbox.addWidget(self.Group1())
        vbox.addWidget(self.Group2())

    
   #그룹박스 - 스트러트 높이 설정 --------------------------------------------------------------   
    def Group1(self):
        groupbox = CNV_GroupBox()
        
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)
        
        # 라벨 생성
        lb1 = CNV_TitleLabel('스트러트 높이 설정')
        vbox.addWidget(lb1)
        
        # 테이블 위젯 생성
        tableWidget = CNV_TableWidget()
        tableWidget.setRowCount(10)
        tableWidget.setColumnCount(2)
        
        tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem())
        tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("mm"))
            
        # 행의 헤더 숨기기
        header = tableWidget.verticalHeader()
        header.hide()       
        
        # 테이블 열 너비 조정
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 

        vbox.addWidget(tableWidget)

        # 버튼 생성
        btn = CNV_Button('추가')
        vbox.addWidget(btn)
        self.show()    

        return groupbox
    
    
    
   #그룹박스 - 터파기 높이 설정 --------------------------------------------------------------   
    def Group2(self):
        groupbox = CNV_GroupBox()
        
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)
        
        # 라벨 생성
        lb1 = CNV_TitleLabel('터파기 높이 설정')
        vbox.addWidget(lb1)
        
        # 테이블 위젯 생성
        tableWidget = CNV_TableWidget()
        tableWidget.setRowCount(10)
        tableWidget.setColumnCount(2)
        

        tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("레이어"))
        tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("mm"))

            
        # 행의 헤더 숨기기
        header = tableWidget.verticalHeader()
        header.hide()       
        
        # 테이블 열 너비 조정
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
               
        vbox.addWidget(tableWidget)

        
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
