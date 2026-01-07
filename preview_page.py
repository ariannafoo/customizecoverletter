from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from helper import *


class PreviewPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()

        self.stacked_widget = stacked_widget  # Store reference to stacked widget
        self._company = ""

        # One label that updates (avoids recreating it every time)
        self.image_label = QLabel("No preview yet.")
        self.image_label.setAlignment(Qt.AlignCenter)

        self.setup_ui()
    
    def set_company(self, company_name):
        self._company = company_name
        self.update_preview_image()  

    def get_company(self):
        if (isNotEmpty(self._company)):
            return self._company
        return None

    def setup_ui(self):
         # Create a new widget to represent the preview page
        main_layout = QVBoxLayout(self)
        content_layout = QHBoxLayout()

        # Create top and side navigation bars (if required)
        top_nav, side_nav = main_layout_ui()
        main_layout.addWidget(top_nav)  # Add top navigation bar
        content_layout.addWidget(side_nav)  # Add side navigation bar

         # Add the image label to the layout once
        content_layout.addWidget(self.image_label, stretch=1)

        # Back button
        back_button = QPushButton("Start Over")
        back_button.setFixedSize(200, 30)
        back_button.clicked.connect(self.on__back_button_clicked)  # Reset to the original UI
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #398cef; 
                color: white;
                border-radius: 10px;
            }
            QPushButton:pressed {
                background-color: #7bc8da;
            }
        """)
        content_layout.addWidget(back_button, alignment=Qt.AlignCenter)

        # Add content to the main layout
        main_layout.addLayout(content_layout)

    def update_preview_image(self):

        # Load and scale the preview image (make sure this path exists)
        preview_image_path = f"output_previews/{self._company}_CL.jpg"
        print(f"**************OUTPUT PATH**************")
        print(preview_image_path)

        if os.path.exists(preview_image_path):
            image = QPixmap(preview_image_path)
            # self.image_label.setStyleSheet("")   # clear error styling
            # self.image_label.setText("")  
            self.image_label.setPixmap(image.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.image_label.setPixmap(QPixmap())
            self.image_label.setText("Preview image not found.")
            self.image_label.setStyleSheet("color: red; font-size: 16px;")

    def on__back_button_clicked(self):
        """Handle button click event to go back to PageOne."""
        self.stacked_widget.setCurrentIndex(0)
