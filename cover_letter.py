import sys
import os
from datetime import datetime
import calendar
from cover_letter_script import CoverLetter

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
        fname, _ = QFileDialog.getOpenFileName(self, "Open File", "/Users/ariannafoo/Documents/RESUME_COVER_LETTER", "Word (*.docx)")
        
        self.setText(self.create_html(fname)) if fname else None

class MainWindow(QWidget):

    def __init__(self): 
        super().__init__()

        # Declare variables
        self.inputs = []
        self._replacements = []
        self.company = ""
        self.date_str = ""

        self.setWindowTitle("Cover Letter Customizer")
        self.setFixedSize(900, 600)
        self.setup_ui()
    
    def setup_ui(self):
        """
        Setup the UI elements of the window.
        """
        main_layout = QVBoxLayout(self)

        # Top Navigation Bar
        top_nav_layout = QHBoxLayout()
        top_nav_layout.setSpacing(20)
        top_nav_layout.setContentsMargins(15, 10, 15, 10)

        title = QLabel("Cover Letter Customizer")
        title.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        title.setAlignment(Qt.AlignLeft)

        # Add items to the top navigation bar
        top_nav_layout.addWidget(title, alignment=Qt.AlignLeft)
        top_nav_layout.addStretch()
    
        top_nav_container = QFrame()
        top_nav_container.setLayout(top_nav_layout)
        top_nav_container.setStyleSheet("background-color: #398cef;")
        top_nav_container.setFixedHeight(50)
        main_layout.addWidget(top_nav_container)

        # Main Content Layout (Side Navigation and Form)
        content_layout = QHBoxLayout()

        # Side Navigation
        side_nav_layout = QVBoxLayout()
        side_nav_layout.setSpacing(20)

        steps = [
            "Step One\nEnter position details",
            "Step Two\nPreview letter",
            "Step Three\nSave",
            "Step Four\nN/A",
            "Step Five\nN/A",
            "Step Six\nN/A"
        ]
        # TODO: Fix hightlighting
        for i, step in enumerate(steps, start=1):
            step_label = QLabel(step)
            step_label.setAlignment(Qt.AlignLeft)
            step_label.setStyleSheet(f"""
                QLabel {{
                    color: {'#f8faff' if i <= 3 else 'lightgray'};
                    font-size: 14px;
                    font-weight: {'bold' if i == 3 else 'normal'};
                }}
            """)
            side_nav_layout.addWidget(step_label)

        # Add navigation to the left of the main layout
        side_nav_container = QWidget()
        side_nav_container.setLayout(side_nav_layout)
        side_nav_container.setFixedWidth(200)
        content_layout.addWidget(side_nav_container)

        # Form Area
        form_layout = QVBoxLayout()
        form_layout.setSpacing(20)

        # Form Header
        header = QLabel("Position Details")
        header.setStyleSheet("color: #398cef; font-size: 18px; font-weight: bold; sans-serif;")
        form_layout.addWidget(header)

        # Form Fields
        grid_layout = QGridLayout()
        grid_layout.setHorizontalSpacing(20)
        grid_layout.setVerticalSpacing(15)

        # Labels and inputs
        fields = [
            ("City", QLineEdit(), "e.g. Vaughan"),
            ("Company", QLineEdit(), "e.g. Aviva Insurance"),
            ("Position", QLineEdit(), "e.g. Chat Support Rep"),
            ("Save to", QLineEdit(), "/.../some/file/path/"),
        ]

        for i, (label_text, field, placeholder) in enumerate(fields):
            label = QLabel(label_text)
            label.setStyleSheet("color: black; font-size: 14px; sans-serif;")
            grid_layout.addWidget(label, i, 0)

            field.setPlaceholderText(placeholder)
            field.setStyleSheet("""
                QLineEdit {
                    color: black;
                    border: 1px solid lightgray;
                    border-radius: 5px;
                    padding: 5px;
                }
            """)
            grid_layout.addWidget(field, i, 1)

        # File Upload
        file_label = QLabel("File")
        file_label.setStyleSheet("color: black; font-size: 14px;")
        grid_layout.addWidget(file_label, len(fields) + 1, 0)

        self.file_upload_button = QPushButton("Upload Files")
        self.file_upload_button.setStyleSheet("""
            QPushButton {
                border: 2px dashed #398cef;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                color: #398cef;
                background-color: #f8faff;
            }
            QPushButton:hover {
                background-color: #e6f0ff;
            }
        """)
        self.file_upload_button.clicked.connect(self.open_file_dialog)
        grid_layout.addWidget(self.file_upload_button, len(fields) + 1, 1)

        form_layout.addLayout(grid_layout)

        # Save & Preview Button
        save_preview_button = QPushButton("Save & Preview")
        save_preview_button.setFixedHeight(40)
        save_preview_button.setFixedWidth(130)
        save_preview_button.clicked.connect(self.on_save_btn_clicked)
        save_preview_button.setStyleSheet("""
            QPushButton {
                background-color: #398cef;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #296cc0;
            }
        """)
        form_layout.addWidget(save_preview_button, alignment=Qt.AlignRight)

        # Add form to the main layout
        form_container = QFrame()
        form_container.setLayout(form_layout)
        form_container.setStyleSheet("background-color: white; border-radius: 10px;")
        content_layout.addWidget(form_container, stretch=1)

        # Add content to the main layout
        main_layout.addLayout(content_layout)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "Word (*.docx)")
        print(file_path)

        if file_path:
            # Extract file name
            file_name = os.path.basename(file_path)
            print(file_name)
            self.file_upload_button.setText(file_name)

      
        '''
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

        # Create "Select Directory" button
        dest_button = QPushButton("Choose destination")
        dest_button.setFixedSize(150, 30)
        dest_button.clicked.connect(self.on_location_btn_clicked)
        dest_button.setStyleSheet("""
            
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

        # Create label to display directory
        self.destination_lbl = QLabel("")
        self.destination_lbl.setStyleSheet("""
                QLabel{
                    background-color: white; 
                    color: black; 
                }
        """)        
        
        # Create "Replace" button
        button = QPushButton("Replace")
        button.setFixedSize(200, 30)
        button.clicked.connect(self.on_replace_btn_clicked)
        button.setStyleSheet("""
            
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
        form_cont = QWidget()
        form_cont.setObjectName("formContainer")
        form_cont.setFixedHeight(700)
        form_cont.setStyleSheet("""
            #formContainer {
            background-color: white; 
            border-radius: 10px; 
            border: 1px solid lightgray;
            }
        """) 

        # Create vertical layout
        v_layout = QVBoxLayout() 
        v_layout.addStretch() # Add stretchable space at the top to push widgets downward

        # HBox
        h_layout = QHBoxLayout()
        h_layout.addWidget(dest_button, alignment=Qt.AlignCenter)
        h_layout.addWidget(self.destination_lbl, alignment=Qt.AlignCenter)

        v_layout.addLayout(h_layout)
        v_layout.addItem(QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding))
        v_layout.addWidget(button, alignment=Qt.AlignCenter)

        # Push widgets upward
        v_layout.addStretch()

        # Add v_layout to form container
        form_cont.setLayout(v_layout)

        # Create a layout to center the form container
        outer_layout = QVBoxLayout()
        outer_layout.addStretch() # Add space at the top

        hbox = QHBoxLayout()
        hbox.addStretch() # Add space to left
        hbox.addWidget(form_cont) # Add inner container to center
        hbox.addStretch() # Add space to right

        outer_layout.addLayout(hbox)
        outer_layout.addStretch() # Add space at the buttom

        container = QWidget()
        container.setLayout(outer_layout)
        self.setCentralWidget(container)
        '''

    def create_preview_page(self):
        new_page = QWidget()
        layout = QVBoxLayout()

        # Show message

        # back button
        back_button = QPushButton("Start Over")
        back_button.setFixedSize(200, 30)
        back_button.clicked.connect(self.setup_ui) 
        back_button.setStyleSheet("""
            
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

        # preview
        # Load and scale the image to fit the window size
        image = QPixmap(f"output_previews/{self.company}_CL.jpg")
        screen_size = self.size()  # Get the current window size
        scaled_width = int(screen_size.width() * 0.95)
        scaled_height = int(screen_size.height() * 0.95)
        scaled_image = image.scaled(scaled_width, scaled_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Create QLabel to hold the scaled image
        image_label = QLabel()
        image_label.setPixmap(scaled_image)
        image_label.setAlignment(Qt.AlignCenter)

        # Adding to Vbox layout
        layout.addWidget(image_label, alignment=Qt.AlignCenter)
        layout.addWidget(back_button, alignment=Qt.AlignCenter)


        new_page.setLayout(layout)
        self.setCentralWidget(new_page)

    def on_save_btn_clicked(self):

         # need to parse input path because it includes html
        labels = self.inputs[3].text()
        path = labels.split('"/> ')[-1]
        destination = self.destination_lbl.text()
        
        if any(input.text() == "" for input in self.inputs) or (path == "No file selected.") or (destination == ""):
            self.showEmptyMessage()
        else:
            self.generate_preview()
            self.create_preview_page()

    def showEmptyMessage(self):
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
    
    def on_location_btn_clicked(self):
        dest_dir = QFileDialog.getExistingDirectory(self, "Select Destination Folder", "/Users/ariannafoo/Documents/Cover letter")
        self.destination_lbl.setText(dest_dir)
    
    def showSavedMessage(self):
        msg = QMessageBox() 
        msg.setIcon(QMessageBox.Information) 
  
        # setting message for Message Box 
        msg.setText("Cover letter fields replaced and saved successfully.") 
        
        # setting Message box window title 
        msg.setWindowTitle("Success!") 
        
        # declaring buttons on Message Box 
        msg.setStandardButtons(QMessageBox.Ok) 
        
        # start the app 
        msg.exec_() 

    def generate_preview(self):
        """
        Generate cover letter preview based on user input.
        """
        path = self.inputs[3].text().split('"/> ')[-1]
        self.company = self.inputs[1].text()
        city = self.inputs[0].text()
        position = self.inputs[2].text()
        destination = self.destination_lbl.text()

        if self.company.endswith('s'):
            s = "'"
        else:
            s = "'s"

        new_cover_letter = CoverLetter(path, self.date_str, self.company, city, position, s, destination)
        new_cover_letter.replacePlaceholders()

    def update_selected_date(self, date):
        # The 'date' argument is automatically passed by the signal
        self.date = date
        self.date_str = date.toString("MMMM d, yyyy") 
        
def main():
    app = QApplication([])

    # Creating window instance
    window = MainWindow()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()