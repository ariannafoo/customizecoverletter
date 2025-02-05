from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class PreviewPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()

        self.stacked_widget = stacked_widget  # Store reference to stacked widget

        # Create layout
        layout = QVBoxLayout()

        # Create widgets
        self.label = QLabel("Hello Friend!")
        self.button = QPushButton("Go Back")

        # Add widgets to layout
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Set layout
        self.setLayout(layout)

        # Connect button click to function
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        """Handle button click event to go back to PageOne."""
        self.stacked_widget.setCurrentIndex(0)
