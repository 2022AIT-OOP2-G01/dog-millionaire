import sys
import json
from PySide6.QtCore import QSize
from PySide6.QtGui import QMovie, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QWidget


path = 'dog.gif'

class Window(QWidget):
    def __init__(self) :
        super().__init__()
        #タイトル、ウィンドウの位置大きさ調整
        self.setWindowTitle('ロード画面')
        self.setGeometry(300,100,850,700)
        self.setFixedSize(900, 800)#幅・高さの最大値固定
        
        #self.setStyleSheet("QWidget{ background-image: url(img/backimage.jpg) }")
        
        pixmap = QPixmap("img/backimage")#画像の読み込み
        label = QLabel(self)
        label.move(-600, -400)#画像移動
        label.setPixmap(pixmap)

        #gif画像の貼り付け
        movie = QMovie(path)
        movie.setScaledSize(QSize(300, 250))#画像の大きさを調整
        label1 = QLabel(self)
        label1.setGeometry(500,500, 500, 300)#画像の位置を調整
        label1.setMovie(movie)
        movie.start()

    
        labelStyle = """QLabel {
            color: white;
            font-size: 20px;
        }
        """
        #文字の表示
        label2 = QLabel('<font size=7 color=white >NOW LOADING・・・</font>', self)
        label2.move(100,230)
        
       

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())




