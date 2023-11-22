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

class ksh_report_result(QWidget):

    
    def __init__(self):
        QWidget.__init__(self)
        self.initUI()  # initUI 메서드 호출
      
    def initUI(self):
        
        # 수직 박스 레이아웃 생성
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        
        # 공간 확보
        spacer = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Fixed)
        vbox.addSpacerItem(spacer)   

        # 버튼 생성
        btn = CNV_Button('보링점 추가')
        vbox.addWidget(btn)


        # 그룹박스 생성
        vbox.addWidget(self.Group1())
        vbox.addWidget(self.Group2())
        vbox.addWidget(self.Group3())
        vbox.addWidget(self.Group4())
    
    #그룹박스 - 보링점1 --------------------------------------------------------------   
    def Group1(self):
        groupbox = CNV_GroupBox()
        
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)
        
        # 라벨 생성
        lb1 = CNV_TitleLabel('LX-1')
        vbox.addWidget(lb1)
        
        # 테이블 위젯 생성
        tableWidget = CNV_TableWidget()
        tableWidget.setRowCount(8)
        tableWidget.setColumnCount(2)
        

        tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("지층"))
        tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("층후(M)"))
            

        # 첫 번째 열에 콤보박스 추가
        for i in range(tableWidget.rowCount()):
            combo = CNV_ComboBox()
            combo.addItems(["매립층", "퇴적층(실트)", "퇴적층(모래)", "퇴적층(자갈)", "풍화토", "풍화암", "보통암", "경암"])
            tableWidget.setCellWidget(i, 0, combo)
            
        # 행의 헤더 숨기기
        header = tableWidget.verticalHeader()
        header.hide()       
        
        # 테이블 열 너비 조정
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
               
        vbox.addWidget(tableWidget)

        
        return groupbox
    
    
    #그룹박스 - 보링점2 --------------------------------------------------------------   
    def Group2(self):
        groupbox = CNV_GroupBox()
        
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)  # 그룹박스에 레이아웃 설정
        
        # 라벨 생성
        lb2 = CNV_TitleLabel('LX-2')
        vbox.addWidget(lb2)
        
        # 테이블 위젯 생성
        tableWidget = CNV_TableWidget()
        tableWidget.setRowCount(8)
        tableWidget.setColumnCount(2)
        

        tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("지층"))
        tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("층후(M)"))
            

        # 첫 번째 열에 콤보박스 추가
        for i in range(tableWidget.rowCount()):
            combo = CNV_ComboBox()
            combo.addItems(["매립층", "퇴적층(실트)", "퇴적층(모래)", "퇴적층(자갈)", "풍화토", "풍화암", "보통암", "경암"])
            tableWidget.setCellWidget(i, 0, combo)
            
        # 행의 헤더 숨기기
        header = tableWidget.verticalHeader()
        header.hide()       
        
        # 테이블 열 너비 조정
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
               
        vbox.addWidget(tableWidget)

        return groupbox
    
    
    #그룹박스 - 보링점3 --------------------------------------------------------------   
    def Group3(self):
        groupbox = CNV_GroupBox()
        
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)
        
        # 라벨 생성
        lb1 = CNV_TitleLabel('LX-3')
        vbox.addWidget(lb1)
        
        # 테이블 위젯 생성
        tableWidget = CNV_TableWidget()
        tableWidget.setRowCount(8)
        tableWidget.setColumnCount(2)
        

        tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("지층"))
        tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("층후(M)"))
            

        # 첫 번째 열에 콤보박스 추가
        for i in range(tableWidget.rowCount()):
            combo = CNV_ComboBox()
            combo.addItems(["매립층", "퇴적층(실트)", "퇴적층(모래)", "퇴적층(자갈)", "풍화토", "풍화암", "보통암", "경암"])
            tableWidget.setCellWidget(i, 0, combo)
            
        # 행의 헤더 숨기기
        header = tableWidget.verticalHeader()
        header.hide()       
        
        # 테이블 열 너비 조정
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
               
        vbox.addWidget(tableWidget)

        
        return groupbox
    
    
    #그룹박스 - 보링점4 --------------------------------------------------------------   
    def Group4(self):
        groupbox = CNV_GroupBox()
        
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)  # 그룹박스에 레이아웃 설정
        
        # 라벨 생성
        lb2 = CNV_TitleLabel('LX-4')
        vbox.addWidget(lb2)
        
        # 테이블 위젯 생성
        tableWidget = CNV_TableWidget()
        tableWidget.setRowCount(8)
        tableWidget.setColumnCount(2)
        

        tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("지층"))
        tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("층후(M)"))
            

        # 첫 번째 열에 콤보박스 추가
        for i in range(tableWidget.rowCount()):
            combo = CNV_ComboBox()
            combo.addItems(["매립층", "퇴적층(실트)", "퇴적층(모래)", "퇴적층(자갈)", "풍화토", "풍화암", "보통암", "경암"])
            tableWidget.setCellWidget(i, 0, combo)
            
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

    w = ksh_report_result()
    w.resize(600, 800)
    filename = sys.argv[1]
    if os.path.isfile(filename):
        w.load_ifc_file(filename)
        w.show()
    sys.exit(app.exec_())
