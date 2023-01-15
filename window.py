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
        #print('(%d,%d)がクリックされた'%(p.x(),p.y()))


class card_position:
    # カードの配列例
    card = ['d10', 'd3','h12', 'd6', 'h1', 'h11', 'd9', 'c12', 's5', 's10', 'c13', 'h10', 'c10']

    # カードの長さ取得
    len(card)

    # 配置場所
    # カードの合計が13,12枚だったら1から
    if len(card)==13 or len(card)==12:
        print('1番左からカードを並べます')
    # カードの合計が11,10枚だったら2から
    if len(card)==11 or len(card)==10:
        print('左から2番目からカードを並べます')
    # カードの合計が9,8枚だったら3から
    if len(card)==9 or len(card)==8:
        print('左から3番目からカードを並べます')
    # カードの合計が7,6枚だったら4から
    if len(card)==7 or len(card)==6:
        print('左から4番目からカードを並べます')
    # カードの合計が5,4枚だったら5から
    if len(card)==5 or len(card)==4:
        print('左から5番目からカードを並べます')
    # カードの合計が3,2枚だったら6から
    if len(card)==3 or len(card)==2:
        print('左から6番目からカードを並べます')
    # カードの合計が1枚だったら7から
    if len(card)==1:
        print('左から7番目からカードを並べます')

#カードと照合する
#表示
#カード押されたらd3などと送れるようにする

qAp = QApplication(sys.argv)
mado = main()
mado.show()
qAp.exec()