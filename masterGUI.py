import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
                             QSpinBox, QComboBox, QHBoxLayout, QTabWidget, QGraphicsView, 
                             QGraphicsScene, QLineEdit, QMessageBox, QListWidget, QTextEdit, QListWidgetItem)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from WorkerClass import WorkerDataLoader, FILE_PATH


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.jsonloader = WorkerDataLoader(FILE_PATH)
        self.title = 'Setting JSON Updater'
        self.left = 500
        self.top = 500
        self.width = 600
        self.height = 700
        self.initUI()

    def initUI(self):
        # Set the window title and position
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create a vertical layout
        layout = QVBoxLayout()

        # Add a label
        self.label = QLabel("Enter JSON Data:")
        layout.addWidget(self.label)

        # Add a text edit field
        self.textEdit = QTextEdit()
        layout.addWidget(self.textEdit)

        # Add a button
        self.button = QPushButton("Update JSON")
        self.button.clicked.connect(self.on_click)
        layout.addWidget(self.button)

        # Add a status label
        self.statusLabel = QLabel("Status: Ready")
        layout.addWidget(self.statusLabel)

        # Set the layout
        self.setLayout(layout)

        # Show the window
        self.show()

    def on_click(self):
        input_text = self.textEdit.toPlainText()
        self.statusLabel.setText("JSON Updated Successfully!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())