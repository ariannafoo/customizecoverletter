from cover_letter_ui import MainWindow
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication([])

    # Creating window instance
    window = MainWindow()
    window.show()

    # Run application
    app.exec_()

if __name__ == "__main__":
    main()