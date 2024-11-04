import sys
from datetime import datetime
import calendar

from PyQt5.QtCore import QSize, Qt, QDate
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# QLabel Class
class Label(QLabel):

    """
    This class represents a clickable icon and label side by side. 
    """
            
    # simpler way to do this??
    def __init__(self, parent=None):
        super(Label, self).__init__(parent)

        self.icon_path = 'images/blue_file.jpeg'  # Path to your icon
        self.setAlignment(Qt.AlignVCenter)
        self.setText(self.create_html("No file selected."))

     # Create HTML for the label
    def create_html(self, text):
        return f'<img src="{self.icon_path}" width="20" height="15" style="vertical-align: middle;"/> {text}'

    # On mouse click open file directory
    def mousePressEvent(self, event):

        self.setCursor(Qt.PointingHandCursor)

        # getOpenFileName returns a tuple
        fname, _ = QFileDialog.getOpenFileName(self, "Open File", "/Users/ariannafoo/Documents", "Word (*.docx)")
        
        self.setText(self.create_html(fname)) if fname else None

class MainWindow(QMainWindow):

    def __init__(self): 
        super().__init__()

        # Declare variables
        self.inputs = []
        self._replacements = []

        self.configure_window()
        self.setup_ui()

    
    def configure_window(self):
        """
        Set up window properties: title, size and style.
        """
        self.setWindowTitle("Cover Letter Customizer")
        
        self.setStyleSheet("""
            QMainWindow {
                background-image: url('images/background.png'); 
                background-repeat: no-repeat; 
                background-position: center;
            }
        """)

        self.setFixedSize(QSize(800, 800))
    
    def setup_ui(self):
        """
        Setup the UI elements of the window.
        """

        # Create label
        self.labels = [
            QLabel("Enter city name"),
            QLabel("Enter company name"),
            QLabel("Enter position title"),
            QLabel("Select File"),
        ]
        # Create inputs
        self.inputs = [
            QLineEdit(),
            QLineEdit(),
            QLineEdit(),
            Label()
        ]
        # Setting input placeholders
        self.inputs[0].setPlaceholderText("e.g. Vaughan"),
        self.inputs[1].setPlaceholderText("e.g. Airbnb Canada"),
        self.inputs[2].setPlaceholderText("e.g. Chat Support Rep"),
        
        # Create "Replace" button
        self.button = QPushButton("Replace")
        self.button.setFixedSize(200, 30)
        self.button.clicked.connect(self.on_replace_btn_clicked)
        self.button.setStyleSheet("""
            
            QPushButton{
                background-color: #398cef; 
                color: white;
                border-radius: 10px;
            }
            
            QPushButton:pressed {
                background-color: #7bc8da;
                color: white;
            }              
        """)

        # Create form container widget to hold form
        self.form_cont = QWidget()
        self.form_cont.setObjectName("formContainer")
        self.form_cont.setFixedHeight(600)
        self.form_cont.setStyleSheet("""
            #formContainer {
            background-color: white; 
            border-radius: 10px; 
            border: 1px solid lightgray;
            }
        """) 

        # Create vertical layout
        self.v_layout = QVBoxLayout() 
        self.v_layout.addStretch() # Add stretchable space at the top to push widgets downward

        # Create calendar
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)


        # Setting date range
        today = QDate.currentDate()
        self.calendar.setMinimumDate(today.addDays(-7))
        self.calendar.setMaximumDate(today.addDays(+7))

        # Getting date
        self.calendar.clicked.connect(lambda date: print(date.toString("MMMM d, yyyy")))

        # Add calendar to layout
        self.v_layout.addWidget(self.calendar, alignment=Qt.AlignCenter)

    

        # Add labels and inputs to the form container
        for label, input in zip(self.labels, self.inputs):

            # Setting size
            label.setFixedSize(150, 30)
            label.setStyleSheet("background-color: transparent; color: black")
            input.setFixedSize(300, 30)
            input.setStyleSheet("""
                QLineEdit, Label{
                    background-color: white; 
                    color: black; 
                    border: 1px solid lightgray; 
                    border-radius: 10px;
                }
                
                QLineEdit:focus {
                    border: 1px solid blue;
                }
            """)

            # Adding to widget vertical layout and center horizontally
            self.v_layout.addWidget(label,)
            self.v_layout.addWidget(input, alignment=Qt.AlignCenter)

        self.v_layout.addItem(QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.v_layout.addWidget(self.button, alignment=Qt.AlignCenter)

        # Push widgets upward
        self.v_layout.addStretch()

        # Add v_layout to form container
        self.form_cont.setLayout(self.v_layout)

        # Create a layout to center the form container
        self.outer_layout = QVBoxLayout()
        self.outer_layout.addStretch() # Add space at the top

        self.hbox = QHBoxLayout()
        self.hbox.addStretch() # Add space to left
        self.hbox.addWidget(self.form_cont) # Add inner container to center
        self.hbox.addStretch() # Add space to right

        self.outer_layout.addLayout(self.hbox)
        self.outer_layout.addStretch() # Add space at the buttom

        self.container = QWidget()
        self.container.setLayout(self.outer_layout)
        self.setCentralWidget(self.container)

    def on_replace_btn_clicked(self):
        if any(input.text() == "" for input in self.inputs):
            self.showMessageBox()

    def showMessageBox(self):
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Information) 
  
        # setting message for Message Box 
        msg.setText("Please complete all fields to continue.") 
        
        # setting Message box window title 
        msg.setWindowTitle("Incomplete Fields") 
        
        # declaring buttons on Message Box 
        msg.setStandardButtons(QMessageBox.Ok) 
        
        # start the app 
        msg.exec_() 

    def get_user_values(self):
        """
        Return user values from corresponding fields.
        """
        
    

    def replace_btn_toggled(self, checked):
        pass
        

def main():
    app = QApplication([])

    # Creating window instance
    window = MainWindow()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()