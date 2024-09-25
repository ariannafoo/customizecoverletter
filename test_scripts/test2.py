from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setStyleSheet("""
            background-color: blue; 
            border-radius: 10px;
        """)
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)

        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        self.setStyleSheet("""
            background-color: pink; 
        """)

        print(self.button_is_checked)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()