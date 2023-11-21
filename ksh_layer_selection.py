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


class ksh_layer_selection(QWidget):

    
    def __init__(self):
        QWidget.__init__(self)
        self.initUI()  # initUI 메서드 호출
      
    def initUI(self):
        
        # 수직 박스 레이아웃 생성
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        
        # 버튼 생성
        btn = QPushButton('파일 불러오기')
        vbox.addWidget(btn)
        self.show()    


        # 그룹박스 생성
        vbox.addWidget(self.Group1())
        vbox.addWidget(self.Group2())

    
    #그룹박스 - 지형 --------------------------------------------------------------------------   
    def Group1(self):
        groupbox = QGroupBox('지형')
        
        vbox = QVBoxLayout()

        # 탭 위젯 생성
        tabs = QTabWidget()
        tabs.addTab(QWidget(), '현황')
        tabs.addTab(QWidget(), '터파기')  # 빈 탭 추가

        # 테이블 위젯 생성
        table = QTableWidget()
        table.setRowCount(8)
        table.setColumnCount(2)

        table.setHorizontalHeaderItem(0, QTableWidgetItem("부재"))
        table.setHorizontalHeaderItem(1, QTableWidgetItem("레이어선택"))

        # 첫 번째 열에 콤보박스 추가
        for i in range(table.rowCount()):
            combo = QComboBox()
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

        groupbox.setLayout(vbox)  # 그룹박스에 레이아웃 설정
        
        return groupbox
    
    #그룹박스 - 부재 ------------------------------------------------------------------ 
    def Group2(self):
        groupbox = QGroupBox('부재')
        
        vbox = QVBoxLayout()

        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab4 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, '파일')
        tabs.addTab(tab2, '흙막이')
        tabs.addTab(tab3, '버팀대')
        tabs.addTab(tab4, '복공판')
        
        # 테이블 위젯 생성
        table = QTableWidget()
        table.setRowCount(8)
        table.setColumnCount(2)

        table.setHorizontalHeaderItem(0, QTableWidgetItem("부재"))
        table.setHorizontalHeaderItem(1, QTableWidgetItem("레이어선택"))

        # 첫 번째 열에 콤보박스 추가
        for i in range(table.rowCount()):
            combo = QComboBox()
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

        groupbox.setLayout(vbox)  # 그룹박스에 레이아웃 설정
        

        return groupbox



if __name__ == '__main__':
    app = 0
    if QApplication.instance():
        app = QApplication.instance()
    else:
        app = QApplication(sys.argv)

    w = ksh_layer_selection()
    w.resize(600, 800)
    filename = sys.argv[1]
    if os.path.isfile(filename):
        w.load_ifc_file(filename)
        w.show()
    sys.exit(app.exec_())
