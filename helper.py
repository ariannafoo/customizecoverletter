import os
from datetime import date
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def isEmpty(string):
    """
    Return true if the string is empty, false otherwise.
    """
    return string == ""      

def isNotEmpty(string):
    """
    Return true if the string is empty, false otherwise.
    """
    return string != ""      

def main_layout_ui():
        """
        Return tuple containing two elements: UI for the top bar and UI for side bar.
        """
        # ------------------------ Top Nav Bar ------------------------
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

        # ------------------------ Side Bar ------------------------
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

        return (top_nav_container, side_nav_container)