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
      
        self.new_group_count = 5
              
    def initUI(self):
        
        # 수직 박스 레이아웃 생성
        self.vbox = QVBoxLayout() 
        self.setLayout(self.vbox)
        
        # 공간 확보
        spacer = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.vbox.addSpacerItem(spacer)   

        # 버튼 생성
        btn = CNV_Button('보링점 추가')
        btn.clicked.connect(self.addBoringPoint)        
        self.vbox.addWidget(btn)


        # 스크롤 가능한 영역 생성
        scroll_area = CNV_ScrollArea()
        scroll_area.setWidgetResizable(True)  # 스크롤 영역 크기 자동 조절 설정

        # 그룹박스들을 담을 위젯 생성
        self.scroll_content = QWidget()
        layout = QVBoxLayout(self.scroll_content)  # 수직 레이아웃 설정
        layout.setAlignment(Qt.AlignTop)  # 위쪽 정렬
        
        
        # 그룹박스들을 스크롤 가능한 영역에 추가
        scroll_area.setWidget(self.scroll_content)
        self.vbox.addWidget(scroll_area)

        # 그룹박스 생성
        layout.addWidget(self.Group1())
        layout.addWidget(self.Group2())
        layout.addWidget(self.Group3())
        layout.addWidget(self.Group4())
    

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

    #새로운 보링점 추가 --------------------------------------
    def addBoringPoint(self):
        # 새로운 보링점 그룹 생성 및 레이아웃 추가
        new_group = self.createBoringPointGroup()
        self.scroll_content.layout().addWidget(new_group)
        self.new_group_count += 1  # 그룹이 추가될 때마다 숫자 증가        

    def createBoringPointGroup(self):
        # '그룹1'과 같은 구조의 그룹 생성하는 함수
        groupbox = CNV_GroupBox()
        main_vbox = QVBoxLayout()
        groupbox.setLayout(main_vbox)
        
        hbox = QHBoxLayout()        
        
        lb_text = f'LX-{self.new_group_count}'
        lb = CNV_TitleLabel(lb_text)  # 보링점 제목 변경 가능
        hbox.addWidget(lb)
        
        # 각 그룹에 종료 버튼 추가
        close_btn = CNV_CloseButton('X')  # 닫기 버튼 생성
        close_btn.clicked.connect(lambda: self.closeBoringPointGroup(groupbox))  # 클릭 시 그룹 닫기
        hbox.addWidget(close_btn)  # 그룹 박스에 버튼 추가
        main_vbox.addLayout(hbox)  # 메인 레이아웃에 수평 레이아웃 추가        
       
        tableWidget = CNV_TableWidget()
        tableWidget.setRowCount(8)
        tableWidget.setColumnCount(2)
        tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("지층"))
        tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("층후(M)"))

        for i in range(tableWidget.rowCount()):
            combo = CNV_ComboBox()
            combo.addItems(["매립층", "퇴적층(실트)", "퇴적층(모래)", "퇴적층(자갈)", "풍화토", "풍화암", "보통암", "경암"])
            tableWidget.setCellWidget(i, 0, combo)
            
        header = tableWidget.verticalHeader()
        header.hide()       
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
        main_vbox.addWidget(tableWidget)

        return groupbox

    def closeBoringPointGroup(self, groupbox):
        # 선택한 그룹을 레이아웃에서 제거하고 삭제
        self.vbox.removeWidget(groupbox)
        groupbox.deleteLater()


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
