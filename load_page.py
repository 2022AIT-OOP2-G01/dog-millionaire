import sys
import os

#from PySide6.QtCore import QSize
from PySide6.QtGui import QMovie, QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QWidget


path = 'dog.gif'

class Window(QWidget):
    def __init__(self) :
        super().__init__()
        #タイトル、ウィンドウの位置大きさ調整
        self.setWindowTitle('ロード画面')
        self.setGeometry(300,100,850,700)
        #幅・高さの最大値固定
        self.setFixedSize(900, 800)
        
        css= '''
        width: 30%;
        height: auto;
        '''
        
        movie = QMovie(path)
        #movie.setScaledSize(QSize(500, 250))
        self = QLabel(self)
        self.setGeometry(380,500, 500, 250)
        self.setMovie(movie)
        self.setStyleSheet(css)
        movie.start()
        
    
        label1 = QLabel('<font size=7 color=black >NOW LOADING・・・</font>', self)
        label1.setGeometry(850,700,444,444)
        

        

        
       
    #gif画像を追加する関数
    def gif_addimage(self, path):
        movie = QMovie(path)
        self = QLabel(self)
        self.setMovie(movie)
        self.setGeometry(0, 0, 500, 400)
        movie.start()

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())




