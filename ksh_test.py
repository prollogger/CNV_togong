import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QComboBox

class MergedTableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout(self)

        # 테이블 위젯 생성
        tableWidget = QTableWidget()
        tableWidget.setRowCount(8)
        tableWidget.setColumnCount(3)
        
        # 첫 번째 열에 콤보박스 추가
        for i in range(tableWidget.rowCount()):
            combo = QComboBox()
            combo.addItems(["Option 1", "Option 2", "Option 3"])
            tableWidget.setCellWidget(i, 1, combo)
        
        # 헤더 아이템 설정
        tableWidget.horizontalHeader().setVisible(False)
        tableWidget.verticalHeader().setVisible(False)
        tableWidget.setSpan(0, 0, tableWidget.rowCount(), 1)  # 첫 번째 열 병합
        item = QTableWidgetItem("공번")
        tableWidget.setItem(0, 0, item)
        tableWidget.resizeColumnsToContents()
        
        vbox.addWidget(tableWidget)
        self.setLayout(vbox)
        self.setWindowTitle('Merged Table Widget')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    merged_table = MergedTableWidget()
    sys.exit(app.exec_())
