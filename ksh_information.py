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

class ksh_information(QWidget):

    
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
        vbox.addWidget(self.Group3())
        
    
    #그룹박스 - 부재 ------------------------------------------------------------------ 
    def Group1(self):
        groupbox = CNV_GroupBox()
        
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)  # 그룹박스에 레이아웃 설정
        
        # 라벨 생성
        lb1 = CNV_TitleLabel('파일')
        vbox.addWidget(lb1)
        
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()

        tabs = CNV_TabWidget()
        tabs.addTab(tab1, 'PRD')
        tabs.addTab(tab2, 'RCD')
        tabs.addTab(tab3, 'PHC')
        
        # 테이블 위젯 생성
        table = CNV_TableWidget()
        table.setRowCount(8)
        table.setColumnCount(2)

        table.setHorizontalHeaderItem(0, QTableWidgetItem("부재"))
        table.setHorizontalHeaderItem(1, QTableWidgetItem("사이즈"))

        # 첫 번째 열에 콤보박스 추가
        for i in range(table.rowCount()):
            combo = CNV_ComboBox()
            combo.addItems(["Option 1", "Option 2", "Option 3"])
            table.setCellWidget(i, 1, combo)
            
        # 행의 헤더 숨기기
        header = table.verticalHeader()
        header.hide()       

        # 테이블 열 너비 조정
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 

        # 탭에 테이블 추가
        tab1 = tabs.widget(0)
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(table)
        tab1.setLayout(tab1_layout)
        
        vbox.addWidget(tabs)

        

        return groupbox

    
    #그룹박스 - 흙막이 ------------------------------------------------------------------ 
    def Group2(self):
        groupbox = CNV_GroupBox()
        
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)  # 그룹박스에 레이아웃 설정
        
        # 라벨 생성
        lb1 = CNV_TitleLabel('흙막이')
        vbox.addWidget(lb1)
        
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab4 = QWidget()

        tabs = CNV_TabWidget()
        tabs.addTab(tab1, 'CIP')
        tabs.addTab(tab2, 'PILE')
        tabs.addTab(tab3, 'H-PILE')
        tabs.addTab(tab4, '슬러리월')
        
        # 테이블 위젯 생성
        table = CNV_TableWidget()
        table.setRowCount(8)
        table.setColumnCount(2)

        table.setHorizontalHeaderItem(0, QTableWidgetItem("부재"))
        table.setHorizontalHeaderItem(1, QTableWidgetItem("사이즈"))

        # 첫 번째 열에 콤보박스 추가
        for i in range(table.rowCount()):
            combo = CNV_ComboBox()
            combo.addItems(["Option 1", "Option 2", "Option 3"])
            table.setCellWidget(i, 1, combo)
            
        # 행의 헤더 숨기기
        header = table.verticalHeader()
        header.hide()       

        # 테이블 열 너비 조정
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 

        # 탭에 테이블 추가
        tab1 = tabs.widget(0)
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(table)
        tab1.setLayout(tab1_layout)
        
        vbox.addWidget(tabs)

        

        return groupbox
    

    #그룹박스 - 버팀대 ------------------------------------------------------------------ 
    def Group3(self):
        groupbox = CNV_GroupBox()
        
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)  # 그룹박스에 레이아웃 설정
        
        # 라벨 생성
        lb1 = CNV_TitleLabel('버팀대')
        vbox.addWidget(lb1)
        
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab4 = QWidget()

        tabs = CNV_TabWidget()
        tabs.addTab(tab1, '센터파일')
        tabs.addTab(tab2, '어스앵커')
        tabs.addTab(tab3, '스트러트')
        tabs.addTab(tab4, '띠장')
        
        # 테이블 위젯 생성
        table = CNV_TableWidget()
        table.setRowCount(8)
        table.setColumnCount(2)

        table.setHorizontalHeaderItem(0, QTableWidgetItem("부재"))
        table.setHorizontalHeaderItem(1, QTableWidgetItem("사이즈"))

        # 첫 번째 열에 콤보박스 추가
        for i in range(table.rowCount()):
            combo = CNV_ComboBox()
            combo.addItems(["Option 1", "Option 2", "Option 3"])
            table.setCellWidget(i, 1, combo)
            
        # 행의 헤더 숨기기
        header = table.verticalHeader()
        header.hide()       

        # 테이블 열 너비 조정
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 

        # 탭에 테이블 추가
        tab1 = tabs.widget(0)
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(table)
        tab1.setLayout(tab1_layout)
        
        vbox.addWidget(tabs)

        

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
