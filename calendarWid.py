import sys
from datetime import datetime
import calendar

from PyQt5.QtCore import QSize, QDate
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CalendarDemo(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar Demo")
        self.setGeometry(300, 300, 450, 300)
        self.initUI()

    def initUI(self):
        self.calendar = QCalendarWidget(self)

        # Position and styling
        self.calendar.move(20, 20)
        self.calendar.setGridVisible(True) # show lines in calendar

         # Customize the calendar's appearance
        self.calendar.setStyleSheet("""
            QCalendarWidget {
                background-color: #f0f0f0; 
                color: #333333;  
                border: 1px solid #d3d3d3;
                border-radius: 5px;
            }
            QCalendarWidget QToolButton {
                background-color: #4A90E2;  /* Background color of month/year navigation buttons */
                color: white;  /* Text color of navigation buttons */
                border: none;
                border-radius: 5px;
                padding: 5px;
            }
            QCalendarWidget QToolButton:hover {
                background-color: #357ABD;  /* Hover color for navigation buttons */
            }
            QCalendarWidget QToolButton::menu-indicator { /* Hide the menu indicator on month/year buttons */
                image: none;
            }
            QCalendarWidget QAbstractItemView:enabled {
                background-color: white;  /* Background color of the date grid */
                color: black;  /* Text color for dates */
                selection-background-color: blue;  /* Background color when a date is selected */
                selection-color: white;  /* Text color for selected date */
            }
            QCalendarWidget QAbstractItemView:disabled {
                color: #234999;  /* Color for disabled dates */
            }
            QCalendarWidget QAbstractItemView:hover {
                background-color: #e5e5e5;  /* Hover color for dates */
            }
            QCalendarWidget QHeaderView::section {
                background-color: #4A90E2;  /* Background color of the weekday header (Sun, Mon, etc.) */
                color: white;
                padding: 5px;
                border: none;
            }
            QCalendarWidget QWidget#qt_calendar_prevmonth, QWidget#qt_calendar_nextmonth {
                border: none;
                background-color: transparent;
                color: white;
            }
        """)

        # Setting date range
        today = QDate.currentDate()
        self.calendar.setMinimumDate(today.addDays(-7))
        self.calendar.setMaximumDate(today.addDays(+7))

        # Getting date
        self.calendar.clicked.connect(lambda date: print(date.toString("MMMM d, yyyy")))

def main():
    # QApplication necessary for any PyQt5 app
    # sys.argv last that allows any CL arguments
    # [] ignores any command line arguments
    app = QApplication(sys.argv)

    demo = CalendarDemo()
    demo.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
