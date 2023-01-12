import sys
from PySide6.QtWidgets import QApplication,QWidget,QLabel
from PySide6.QtGui import QPixmap

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('大富豪') # ウィンドウのタイトル
        self.setGeometry(300,300,500,500) # ウィンドウの位置と大きさ
        label = QLabel(self) # 画像を置くQLabel
        label.move(10,10)
        pix = QPixmap('card_back.png') # 画像を読み込むQPixmap
        pix = pix.scaledToWidth(100) # 大きさの変更
        label.setPixmap(pix)
        

qAp = QApplication(sys.argv)
mado = main()
mado.show()
qAp.exec()