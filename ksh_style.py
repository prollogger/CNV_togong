from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


        
# 타이틀라벨----------------------------------------------------------------------------------------------------------------------
      
class CNV_TitleLabel(QLabel):
    def __init__(self, title='', parent=None):
        super().__init__(title, parent)
        font = QFont()
        font.setBold(True)       # 굵게 설정            
        font.setFamily('맑은고딕')  # 원하는 폰트 패밀리로 변경
        font.setPointSize(int(self.width() / 60))  # 20은 크기 조절을 위한 임의의 비율 상수
        self.setFont(font)
        #self.setAlignment(Qt.AlignCenter)      
        self.setMargin(5)  # 원하는 여백 크기 입력     
        self.setStyleSheet("color: #4582EC;")  # 여기에 원하는 색상 코드 입력
        
# 그룹박스 ----------------------------------------------------------------------------------------------------------------------
      
class CNV_GroupBox(QGroupBox):
    def __init__(self, title='', parent=None):
        super().__init__(title, parent)
        self.setStyleSheet("""
            QGroupBox {
                border: 1px solid #4582EC; /* 테두리 스타일 및 색상 */
                border-radius: 3px;
                margin-top: 10px; /* 위쪽 여백 */
                background-color: #ffffff;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 3px; /* 타이틀 여백 */
                background-color: #ffffff; /* 타이틀 배경색 */
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
                background-color: #ffffff;
                color: #4582EC;               
            }
            QPushButton:hover {
                background-color: #4582EC;
                color: #ffffff;                
                cursor: hand; /* 마우스 오버 시 커서 모양 변경 */                
            }
        """)
        self.setFixedHeight(25)    
        self.font = QFont()
        self.font.setBold(True)       # 굵게 설정            
        self.font.setFamily('맑은고딕')  # 원하는 폰트 패밀리로 변경
        self.font.setPointSize(int(self.width() / 70))  # 20은 크기 조절을 위한 임의의 비율 상수
        
# 종료 버튼 ----------------------------------------------------------------------------------------------------------------------
      
class CNV_CloseButton(QPushButton):
    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                border: 1px solid #4582EC;
                border-radius: 3px;
                background-color: #ffffff;
                color: #4582EC;               
            }
            QPushButton:hover {
                background-color: #4582EC;
                color: #ffffff;                
                cursor: hand; /* 마우스 오버 시 커서 모양 변경 */                
            }
        """)
        self.setFixedHeight(25)    
        self.setFixedWidth(30)        
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)         
        self.font = QFont()
        self.font.setBold(True)       # 굵게 설정            
        self.font.setFamily('맑은고딕')  # 원하는 폰트 패밀리로 변경
        self.font.setPointSize(int(self.width() / 60))  # 20은 크기 조절을 위한 임의의 비율 상수
                
        
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
                font-size: 12px;
            }
            QComboBox:hover {
                border: 2px solid #4582EC;
                background: #EAF1FD;
            }
            QComboBox::down-arrow {
                image: url("C:/Users/thdgm/OneDrive/바탕 화면/CNV_togong_cnvksh/CNV_togong/image/down-arrow-of-angle.png"); /* 화살표 이미지 경로 지정 */
                width: 7px; /* 이미지 너비 */
                height: 7px; /* 이미지 높이 */
            } 
            QComboBox::drop-down {
                image: none;
                border: none;
                box-shadow: none;
            }           
            """)        
   
        
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
            }
        """)        
        
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
            }
        """)     
        self.tabBar().setExpanding(True)  # 탭바의 너비를 자동으로 조절하도록 설정

def main():
    app = QApplication([])

    main_win = QMainWindow()
    main_win.setGeometry(100, 100, 800, 600)

    main_win.show()
    app.exec_()

if __name__ == "__main__":
    main()
