import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget
from home_page import HomePage
from preview_page import PreviewPage

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create QStackedWidget
        self.stacked_widget = QStackedWidget()

        # Create pages
        self.home_page = HomePage(self.stacked_widget)
        self.preview_page = PreviewPage(self.stacked_widget)

        # Add pages to stacked widget
        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.preview_page)

        # Set initial page
        self.stacked_widget.setCurrentIndex(0)

        # Create main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)

        # Set layout
        self.setLayout(main_layout)

        # Window settings
        self.setWindowTitle("Cover Letter Customizer")
        self.setFixedSize(900, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
