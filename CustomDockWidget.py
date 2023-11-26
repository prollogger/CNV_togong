from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QLabel, QVBoxLayout, QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

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
        font.setPointSize(int(self.width() / 11))  # 초기 크기 설정

        title_bar.setFont(font)

        title_bar.setStyleSheet("background-color: #4582ec; color: #ffffff; border: 1px solid #4582ec; border-radius: 3px; min-height: 30px; max-height: 30;")

        # Set the created label as the title bar widget
        self.setTitleBarWidget(title_bar)

        # Add some content to the dock widget
        tree_widget = QTreeWidget(self)
        item = QTreeWidgetItem(["Item 1"])
        
        tree_widget.addTopLevelItem(item)
        self.setWidget(tree_widget)

def main():
    app = QApplication([])

    main_win = QMainWindow()
    main_win.setGeometry(100, 100, 800, 600)

    dock_widget = CustomDockWidget("Dock Widget")
    main_win.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)

    main_win.show()
    app.exec_()

if __name__ == "__main__":
    main()
