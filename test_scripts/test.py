from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App - Test")

        # Creating widgets
        label = QLabel("Enter name")
        label.setFixedSize(200, 30)

        input = QLineEdit()
        input.setFixedSize(200, 30)

        button = QPushButton("Press Me!")
        button.setFixedSize(200, 30)
        button.setCheckable(True)
        
     

        # Apply styles individually to the widgets
        label.setStyleSheet("background-color: transparent;")
        input.setStyleSheet("background-color: white; border: 2px solid lightgray; border-radius: 10px;")
        button.setStyleSheet("background-color: blue; border: 2px solid darkgray; border-radius: 10px;")

        # Create layout for inner container
        layout = QVBoxLayout()
        layout.addStretch()  # Add stretchable space at the top to push widgets downward
        layout.addWidget(label, alignment=Qt.AlignCenter)  # Center the label horizontally
        layout.addWidget(input, alignment=Qt.AlignCenter)  # Center the input horizontally
        layout.addWidget(button, alignment=Qt.AlignCenter)  # Center the button horizontally
        layout.addStretch()  # Add stretchable space at the bottom to push widgets upward

        # Create inner container
        inner_con = QWidget()
        inner_con.setLayout(layout)
        inner_con.setFixedSize(400, 500)
        inner_con.setStyleSheet("background-color: pink;")  # Only background color, no border style

        # Create a layout to center the inner container
        outer_layout = QVBoxLayout()
        outer_layout.addStretch()  # Add stretchable space at the top
        hbox = QHBoxLayout()
        hbox.addStretch()  # Add stretchable space on the left
        hbox.addWidget(inner_con)  # Add the inner container in the center
        hbox.addStretch()  # Add stretchable space on the right
        outer_layout.addLayout(hbox)
        outer_layout.addStretch()  # Add stretchable space at the bottom

        # Create outer container and set its layout
        container = QWidget()
        container.setLayout(outer_layout)
        container.setStyleSheet("background-color: lightblue")

        # Set window size
        self.setFixedSize(1000, 700)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
