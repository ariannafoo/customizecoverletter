import sys
import os
from datetime import date
from cover_letter import CoverLetter

from PyQt5.QtCore import QSize, Qt, QDate
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):

    def __init__(self): 
        super().__init__()

        # Declare variables
        self.fields = []
        self.file_path = ""
        self.destination_path = ""

        self.setWindowTitle("Cover Letter Customizer")
        self.setFixedSize(900, 600)
        self.setup_ui()
    
    def setup_ui(self):
        """
        Setup the UI elements of the window.
        """
        main_layout = QVBoxLayout(self)

        # ============================================
        #              Top Nav Bar Creation
        # ============================================

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

        # ============================================
        #              Side Bar Creation
        # ============================================

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

        # ============================================
        #              Form Creation
        # ============================================

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
        self.fields = [
            ("City", QLineEdit(), "e.g. Vaughan"),
            ("Company", QLineEdit(), "e.g. Aviva Insurance"),
            ("Position", QLineEdit(), "e.g. Chat Support Rep"),
            ("Destination", QLineEdit(), "/../some/file/path")
        ]

        for i, (label_text, field, placeholder) in enumerate(self.fields):
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

        # Destination field
        self.destination_field = self.fields[-1][1]
        self.destination_field.setReadOnly(True)  # Make the field read-only
        self.destination_field.mousePressEvent = lambda event: self.on_destination_field_clicked()  # Trigger the dialog on click
        
        # ============================================
        #              File Upload Creation
        # ============================================

        file_label = QLabel("File")
        file_label.setStyleSheet("color: black; font-size: 14px;")
        grid_layout.addWidget(file_label, len(self.fields) + 1, 0)

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
        grid_layout.addWidget(self.file_upload_button, len(self.fields) + 1, 1)

        form_layout.addLayout(grid_layout)

        # ============================================
        #              Save Button Creation
        # ============================================

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
        form_layout.addWidget(save_preview_button, alignment=Qt.AlignCenter)

        # ============================================
        #              Adding to Main Layout
        # ============================================

        # Add form to the main layout
        form_container = QFrame()
        form_container.setLayout(form_layout)
        form_container.setStyleSheet("background-color: white; border-radius: 10px;")
        content_layout.addWidget(form_container, stretch=1)

        # Add content to the main layout
        main_layout.addLayout(content_layout)
    

    # ============================================
    #              Helper Functions
    # ============================================

    def open_file_dialog(self):
        """
        Return cover letter file path and set text to file name.
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "/Users/ariannafoo/Documents/RESUME_COVER_LETTER", "Word (*.docx)")

        if file_path:
            # Extract file name
            file_name = os.path.basename(file_path)
            self.file_upload_button.setText(file_name)
            self.file_path = file_path
    
    def on_destination_field_clicked(self):
        destination_directory = QFileDialog.getExistingDirectory(self, "Select Destination Folder", "/Users/ariannafoo/Documents/RESUME_COVER_LETTER")
        self.destination_path = destination_directory
        self.destination_field.setText(destination_directory)

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

    def on_save_btn_clicked(self):
        # Check if any fields are empty
        if any([field.text() == "" for (i, field, j) in self.fields]) or (isEmpty(self.file_path)) or (isEmpty(self.destination_path)):
            self.showEmptyMessage()
        # Otherwise create preview + and display preview page
        else:
            print("elloo")
            self.generate_preview()
            self.create_preview_page()

    def generate_preview(self):
        """
        Generate cover letter preview based on user input.
        """
        company = self.fields[0][1].text()
        city = self.fields[1][1].text()
        position = self.fields[2][1].text()

        s = "'" if company.endswith('s') else "'s"

        new_cover_letter = CoverLetter()
        new_cover_letter.replacePlaceholders()


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
    
    # ============================================
    #              Main Function
    # ============================================

def isEmpty(string):
    """
    Return true if the string is empty, false otherwise.
    """
    return string == ""      

def main():
    app = QApplication([])

    # Creating window instance
    window = MainWindow()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()