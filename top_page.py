import sys
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Top Page")
        # Create widgets
        self.label_ip = QLabel("IP address:")
        self.edit_ip = QLineEdit("")
        self.label_port = QLabel("port number:")
        self.edit_port = QLineEdit("")
        self.button = QPushButton("Conect")
        
        # Create layout and add widgets
        layout = QVBoxLayout(self)
        layout.addWidget(self.label_ip)
        layout.addWidget(self.edit_ip)
        layout.addWidget(self.label_port)
        layout.addWidget(self.edit_port)
        layout.addWidget(self.button)
         # Set dialog layout
        self.setLayout(layout)
        # コネクトボタンを押したらconnect関数が呼ばれる
        self.button.clicked.connect(self.connect)

        
    def connect(self):
        print(f"{self.edit_ip.text()}") #ipアドレス
        print(f"{self.edit_port.text()}") #ポート番号

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())