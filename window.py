import sys
from PySide6.QtWidgets import QApplication,QWidget,QLabel
from PySide6.QtGui import QPixmap

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('大富豪') # ウィンドウのタイトル
        self.setGeometry(300,100,900,700) # ウィンドウの位置と大きさ
        label = QLabel(self) # 画像を置くQLabel
        label.move(10,550)
        pix = QPixmap('card_img/card_joker.png') # 画像を読み込むQPixmap
        pix = pix.scaledToWidth(90) # 大きさの変更
        label.setPixmap(pix)

        label = QLabel(self) # 画像を置くQLabel
        label.move(110,550)
        pix = QPixmap('card_img/card_club_01.png') # 画像を読み込むQPixmap
        pix = pix.scaledToWidth(90) # 大きさの変更
        label.setPixmap(pix)
        
    def mouseReleaseEvent(self,e):
        p = e.position() # マウスが解放された場所
        print('(%d,%d)がクリックされた'%(p.x(),p.y()))


card = ['d10', 'd3','h12', 'd6', 'h1', 'h11', 'd9', 'c12', 's5', 's10', 'c13', 'h10', 'c10']
#長さ取得
#配置場所
#カードと照合する
#表示
#カード押されたらd3などと送れるようにする

qAp = QApplication(sys.argv)
mado = main()
mado.show()
qAp.exec()