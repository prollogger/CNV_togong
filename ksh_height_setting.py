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

        # Group1과 Group2 메서드를 호출하여 그룹박스 추가
        self.group1_box = self.Group1()
        vbox.addWidget(self.group1_box)

        self.group2_box = self.Group2()
        vbox.addWidget(self.group2_box)
    
   # 그룹박스1 - 스트러트 높이 설정 --------------------------------------------------------------   
    def Group1(self):
        groupbox = CNV_GroupBox()
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)
        
        # 라벨 생성
        lb1 = CNV_TitleLabel('스트러트 높이 설정')
        vbox.addWidget(lb1)
        
        # 테이블 위젯 생성
        table1 = CNV_TableWidget()
        table1.setRowCount(3)
        table1.setColumnCount(2)
        
        table1.setHorizontalHeaderItem(0, QTableWidgetItem())
        table1.setHorizontalHeaderItem(1, QTableWidgetItem("mm"))
            
        # 행의 헤더 숨기기
        header = table1.verticalHeader()
        header.hide()       
        
        # 테이블 열 너비 조정
        table1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 

        vbox.addWidget(table1)
        
        # 버튼들을 담을 위젯 생성
        button_widget = QWidget()  
        button_widget.setStyleSheet("background-color: #EAF1FD; font-size:15;")
        button_layout = QHBoxLayout()
        
        # 버튼 생성
        add_btn = CNV_Button('+')
        add_btn.clicked.connect(self.addRow)
        
        button_layout.addWidget(add_btn)
        
        delete_btn = CNV_Button('-')
        delete_btn.clicked.connect(self.deleteRow) 
        button_layout.addWidget(delete_btn)
        
        # 버튼 레이아웃을 위젯에 설정
        button_widget.setLayout(button_layout)  
        vbox.addWidget(button_widget)
        
        # 열 너비 설정
        table1.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        table1.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        table1.setColumnWidth(2, 10)  # 세 번째 열의 너비를 100으로 설정 (조절 가능)
        return groupbox
    
    
    # '추가' 버튼 클릭 시 호출되는 메서드
    def addRow(self):
        
        table1 = self.group1_box.findChild(QTableWidget)
        if table1 is not None:
            currentRowCount = table1.rowCount()
            table1.setRowCount(currentRowCount + 1)

    def deleteRow(self, row):
        table1 = self.group1_box.findChild(QTableWidget)
        if table1 is not None:
            table1.removeRow(row)    
    
   #그룹박스 - 터파기 높이 설정 --------------------------------------------------------------   
    def Group2(self):
        groupbox = CNV_GroupBox()
        
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)
        
        # 라벨 생성
        lb1 = CNV_TitleLabel('터파기 높이 설정')
        vbox.addWidget(lb1)
        
        # 테이블 위젯 생성
        table2 = CNV_TableWidget()
        table2.setRowCount(10)
        table2.setColumnCount(2)
        

        table2.setHorizontalHeaderItem(0, QTableWidgetItem("레이어"))
        table2.setHorizontalHeaderItem(1, QTableWidgetItem("mm"))

        # 첫 번째 열에 콤보박스 추가
        for i in range(table2.rowCount()):
            combo = CNV_ComboBox()
            combo.addItems(["layer 1", "layer 2", "layer 3"])
            table2.setCellWidget(i, 0, combo)


        # 행의 헤더 숨기기
        header = table2.verticalHeader()
        header.hide()       
        
        # 테이블 열 너비 조정
        table2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
               
        vbox.addWidget(table2)

        
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
