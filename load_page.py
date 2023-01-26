import sys
import os
from PySide6.QtGui import QMovie, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QFileDialog
#from PySide6.QtWidgets import QFileDialog

path = 'dog.gif'

class Window(QWidget):
    def __init__(self) :
        super().__init__()
        #タイトル、ウィンドウの位置大きさ調整
        self.setWindowTitle('ロード画面')
        self.setGeometry(300,100,850,700)
        self.setFixedSize(900, 800)
        self.setStyleSheet("QWidget{ background-color: green }")
    
    def addimage(self):

        label = QLabel(self)
        movie = QMovie(path)
        """
        #パスの確認
        current_directory = os.getcwd()
        image_path = os.path.join(current_directory, "パスの入力")

        #選択して表示
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(None, "dog.gif", "", "Images (*.gif);;All Files (*)", options=options)
        if file_name:
            path = file_name
        """
        label.setMovie(movie)
        ##読み込み確認
        if label.setMovie(movie):
            print("読み込まれてる")
        else:
            print("読み込まれてない")
        
        movie.start()


app = QApplication(sys.argv)
window = Window()
window.addimage()
window.show()
sys.exit(app.exec_())




