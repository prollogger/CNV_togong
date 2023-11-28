from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



# 위젯
class CNV_DockWidget(QDockWidget):
    def __init__(self, title, parent=None):
        super(CNV_DockWidget, self).__init__(title, parent)
        self.init_ui()

    def init_ui(self):
        # Create a label widget to act as the title bar
        title_bar = QLabel(self)
        title_bar.setText(self.windowTitle())
        title_bar.setAlignment(Qt.AlignCenter)

        # QFont 객체 생성 및 스타일 설정
        font = QFont()
        font.setBold(True)       # 굵게 설정            
        font.setFamily('맑은고딕')  # 원하는 폰트 패밀리로 변경
        font.setPointSize(10)  # 20은 크기 조절을 위한 임의의 비율 상수
        self.setFont(font)
        title_bar.setStyleSheet("background-color: #2A384C; color: #ffffff; border: 1px solid #2A384C; border-radius: 3px; min-height: 30px; max-height: 30;")

        # Set the created label as the title bar widget
        self.setTitleBarWidget(title_bar)

        # Add some content to the dock widget
        tree_widget = QTreeWidget(self)
        item = QTreeWidgetItem(["Item 1"])
        
        tree_widget.addTopLevelItem(item)
        self.setWidget(tree_widget)


# 스크롤바 영역 ---------------------------------------------------------------------------------------------------------------------

class CNV_ScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QScrollArea {
                border: 1px solid #4582EC; /* 테두리 스타일 및 색상 */
                border-radius: 3px;
                margin-top: 5px; /* 위쪽 여백 */
            }
            QScrollBar:vertical {
                border: none;
                background: #EAF1FD;
                width: 14px;
                border-radius: 0px;
            }

            /*  스크롤바(세로) */
            QScrollBar::handle:vertical {	
                background-color: #2A384C;
                min-height: 30px;
                border-radius: 3px;
            }                
                
        """)

# 툴바 ---------------------------------------------------------------------------------------------------------------------

class CNV_ToolBar(QToolBar):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setStyleSheet("""
            QToolBar {
                border: 1px solid #EAF1FD;
                background-color: #EAF1FD;
                margin-bottom: 10px; /* 툴바 아래 마진 설정 */
                spacing: 5px;
            }
            QToolButton {
                border: 1px solid #4582EC; /* 테두리 스타일 및 색상 */
                border-radius: 3px;
                margin: 10px; /* 여백 */
                background-color: #ffffff;
                padding: 5px;
                color: #4582EC;               
            }
            QToolButton:hover {
                background-color: #4582EC;
                color: #ffffff;                
            }
        """)      
        font = QFont()
        font.setBold(False)       # 굵게 설정            
        font.setFamily('맑은고딕')  # 원하는 폰트 패밀리로 변경
        font.setPointSize(10)  # 20은 크기 조절을 위한 임의의 비율 상수
        self.setFont(font)


        
        
# 체크박스 ---------------------------------------------------------------------------------------------------------------------

class CNV_CheckBox(QCheckBox):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QCheckBox {
                spacing: 10px;
                color: #4582EC;
                background-color: #EAF1FD;
            }
            QCheckBox::indicator {
                width: 15px;
                height: 15px;
            }
            QCheckBox::indicator:unchecked {
                border: 1px solid #ccc;
                background-color: #ffffff;
            }
            QCheckBox::indicator:checked {
                border: 1px solid #4582EC;
                background-color: #ffffff;
                image: url("./image/check-mark.png");                
            }
            QCheckBox::indicator:unchecked:hover {
                border: 1px solid #4582EC;
            }
        """)       
        font = QFont()
        font.setBold(False)       # 굵게 설정            
        font.setFamily('맑은고딕')  # 원하는 폰트 패밀리로 변경
        font.setPointSize(10)  # 20은 크기 조절을 위한 임의의 비율 상수
        self.setFont(font)
        
        
# 타이틀라벨----------------------------------------------------------------------------------------------------------------------
      
class CNV_TitleLabel(QLabel):
    def __init__(self, title='', parent=None):
        super().__init__(title, parent)
        font = QFont()
        font.setBold(True)       # 굵게 설정            
        font.setFamily('맑은고딕')  # 원하는 폰트 패밀리로 변경
        font.setPointSize(13)  # 20은 크기 조절을 위한 임의의 비율 상수
        self.setFont(font)
        #self.setAlignment(Qt.AlignCenter)      
        self.setMargin(5)  # 원하는 여백 크기 입력     
        self.setStyleSheet("color: #4582EC; background-color: transparent;")  # 여기에 원하는 색상 코드 입력
    
        
# 그룹박스 ----------------------------------------------------------------------------------------------------------------------
      
class CNV_GroupBox(QGroupBox):
    def __init__(self, title='', parent=None):
        super().__init__(title, parent)
        self.setStyleSheet("""
            QGroupBox {
                border: 1px solid #4582EC; /* 테두리 스타일 및 색상 */
                border-radius: 3px;
                margin-top: 5px; /* 위쪽 여백 */
                background-color: #EAF1FD;
            }
        """)
        
# 버튼 ----------------------------------------------------------------------------------------------------------------------
      
class CNV_Button(QPushButton):
    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                border: 1px solid #4582EC;
                border-radius: 3px;
                padding: 5px;
                background-color: #ffffff;
                color: #4582EC;               
            }
            QPushButton:hover {
                background-color: #4582EC;
                color: #ffffff;                
                cursor: hand; /* 마우스 오버 시 커서 모양 변경 */                
            }
        """)
        font = QFont()
        font.setBold(False)       # 굵게 설정            
        font.setFamily('맑은고딕')  # 원하는 폰트 패밀리로 변경
        font.setPointSize(10)  # 20은 크기 조절을 위한 임의의 비율 상수
        self.setFont(font)
   
        
# 종료 버튼 ----------------------------------------------------------------------------------------------------------------------
      
class CNV_CloseButton(QPushButton):
    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                border: 1px solid #4582EC;
                border-radius: 3px;
                padding: 5px;
                background-color: #ffffff;
                color: #4582EC;               
            }
            QPushButton:hover {
                background-color: #4582EC;
                color: #ffffff;                
                cursor: hand; /* 마우스 오버 시 커서 모양 변경 */                
            }
        """)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)         
        font = QFont()
        font.setBold(False)       # 굵게 설정            
        font.setFamily('맑은고딕')  # 원하는 폰트 패밀리로 변경
        font.setPointSize(10)  # 20은 크기 조절을 위한 임의의 비율 상수
        self.setFont(font)
        
        
                
        
# 콤보박스 ----------------------------------------------------------------------------------------------------------------------
      
class CNV_ComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QComboBox {
                border: 1px solid #D5E3FB;
                border-radius: 1px;
                padding: 1px 1px 1px 1px;
                min-width: 5em;
                background: #ffffff;
                selection-background-color: #4582EC;
            }
            QComboBox:hover {
                border: 2px solid #4582EC;
                background: #EAF1FD;
            }
            QComboBox::down-arrow {
                image: url("./image/down-mark.png"); /* 화살표 이미지 경로 지정 */
                width: 7px; /* 이미지 너비 */
                height: 7px; /* 이미지 높이 */
            } 
            QComboBox::drop-down {
                image: none;
                border: none;
                box-shadow: none;
            }           
            """)      
        font = QFont()
        font.setBold(False)       # 굵게 설정            
        font.setFamily('맑은고딕')  # 원하는 폰트 패밀리로 변경
        font.setPointSize(10)  # 20은 크기 조절을 위한 임의의 비율 상수
        self.setFont(font)
        
        
# 테이블(표) ----------------------------------------------------------------------------------------------------------------------
      
class CNV_TableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QTableWidget {
                border: 1px solid #D5E3FB;
                border-radius: 1px;
                background-color: #ffffff;
                gridline-color: #D5E3FB; /* 그리드 라인 색상 */
                
            }
            QHeaderView::section {
                background-color: #EAF1FD; /* 헤더 배경색 */
                border: 1px solid #EAF1FD; /* 헤더 테두리 스타일 */
                padding-top: 3px;
                padding-bottom: 3px;
                font-family: '맑은고딕'; /* 폰트 종류 설정 */
            }
                        
            QScrollBar:vertical {
                border: none;
                background: #EAF1FD;
                width: 14px;
                border-radius: 0px;
            }

            /*  스크롤바(세로) */
            QScrollBar::handle:vertical {	
                background-color: #2A384C;
                min-height: 30px;
                border-radius: 3px;
            }
            
        """)       
        font = QFont()
        font.setBold(False)       # 굵게 설정            
        font.setFamily('맑은고딕')  # 원하는 폰트 패밀리로 변경
        font.setPointSize(10)  # 20은 크기 조절을 위한 임의의 비율 상수
        self.setFont(font)
        
# 탭뷰 ----------------------------------------------------------------------------------------------------------------------
      
class CNV_TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #ccc;
                border-radius: 1px;
                background-color: #ffffff;
            }
            QTabBar::tab {
                background-color: #ffffff;
                border: 1px solid #ccc;
                border-radius: 1px;
                border-bottom: none; /* 선택된 탭의 하단 테두리 색상 */
                padding: 8px 12px; /* 탭 내부 여백 */
                color: #000000; /* 탭 텍스트 색상 */
            }
            QTabBar::tab:selected {
                border: 1px solid #4582EC;
                border-radius: 1px;
                background-color: #4582EC;
                color: #ffffff; /* 선택된 탭의 텍스트 색상 */
                font-family: '맑은고딕'; /* 폰트 종류 설정 */
            }
        """)     
        font = QFont()
        font.setBold(False)       # 굵게 설정            
        font.setFamily('맑은고딕')  # 원하는 폰트 패밀리로 변경
        font.setPointSize(10)  # 20은 크기 조절을 위한 임의의 비율 상수
        self.setFont(font)
        

def main():
    app = QApplication([])

    main_win = QMainWindow()
    main_win.setGeometry(100, 100, 800, 600)

    main_win.show()
    app.exec_()

if __name__ == "__main__":
    main()
