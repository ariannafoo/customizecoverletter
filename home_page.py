import os
from cover_letter import CoverLetter
from helper import *
from datetime import date
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class HomePage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()

        # Declare variables
        self.fields = []
        self.file_path = ""
        self.destination_path = ""

        # Creating stacked widget
        self.stacked_widget = stacked_widget

        # Create Ui
        self.setup_ui()

    def setup_ui(self):
        """
        Setup the UI elements of the window.
        """
        main_layout = QVBoxLayout(self)
        content_layout = QHBoxLayout()

        # Call main_layout_ui - get ui for top and side nav
        top_nav, side_nav = main_layout_ui()
        main_layout.addWidget(top_nav)
        content_layout.addWidget(side_nav)

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
            company = self.generate_preview()
            preview_page = self.stacked_widget.widget(1)  # Get the preview page
            preview_page.set_company(company)
            self.stacked_widget.setCurrentIndex(1)

    def generate_preview(self):
        """
        Generate cover letter preview based on user input.
        """
        city = self.fields[0][1].text()
        company = self.fields[1][1].text()
        position = self.fields[2][1].text()
        suffix = "'" if company.endswith('s') else "'s"

        # Creates a new .docx and converts to PDF
        new_cover_letter = CoverLetter(company, city, position, suffix, self.file_path, self.destination_path)
        new_cover_letter.generate_cover_letter()
        return company