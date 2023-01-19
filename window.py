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
        pix = QPixmap('card_img/c1.png') # 画像を読み込むQPixmap
        pix = pix.scaledToWidth(90) # 大きさの変更
        label.setPixmap(pix)





        # カードの配列例
        card = ['d10', 'd3','h12', 'd6', 'h1', 'h11', 'd9', 'c12', 's5', 's10', 'c13', 'h10', 'c10']

        # カードの長さ取得
        len(card)

        # 配置場所
        # カードの合計が13,12枚だったら1からカードを並べる
        if len(card)==13 or len(card)==12:
            print('1番左からカードを並べる')
        # カードの合計が11,10枚だったら2からカードを並べる
        if len(card)==11 or len(card)==10:
            print('左から2番目からカードを並べる')
        # カードの合計が9,8枚だったら3からカードを並べる
        if len(card)==9 or len(card)==8:
            print('左から3番目からカードを並べる')
        # カードの合計が7,6枚だったら4からカードを並べる
        if len(card)==7 or len(card)==6:
            print('左から4番目からカードを並べる')
        # カードの合計が5,4枚だったら5からカードを並べる
        if len(card)==5 or len(card)==4:
            print('左から5番目からカードを並べる')
        # カードの合計が3,2枚だったら6からカードを並べる
        if len(card)==3 or len(card)==2:
            print('左から6番目からカードを並べる')
        # カードの合計が1枚だったら7からカードを並べる
        if len(card)==1:
            print('左から7番目からカードを並べる')


        #カードと照合する
        if 'c1' in card:
            c1 = QPixmap('card_img/c1.png') # 画像を読み込むQPixmap
        
        if 'c2' in card:
            c2 = QPixmap('card_img/c2.png') # 画像を読み込むQPixmap
        
        if 'c3' in card:
            c3 = QPixmap('card_img/c3.png') # 画像を読み込むQPixmap

        if 'c4' in card:
            c4 = QPixmap('card_img/c4.png') # 画像を読み込むQPixmap

        if 'c5' in card:
            c5 = QPixmap('card_img/c5.png') # 画像を読み込むQPixmap
             
        if 'c6' in card:
            c6 = QPixmap('card_img/c6.png') # 画像を読み込むQPixmap
        
        if 'c7' in card:
            c7 = QPixmap('card_img/c7.png') # 画像を読み込むQPixmap
        
        if 'c8' in card:
            c8 = QPixmap('card_img/c8.png') # 画像を読み込むQPixmap

        if 'c9' in card:
            c9 = QPixmap('card_img/c9.png') # 画像を読み込むQPixmap
            
        if 'c10' in card:
            c10 = QPixmap('card_img/c10.png') # 画像を読み込むQPixmap

        if 'c11' in card:
            c11 = QPixmap('card_img/c11.png') # 画像を読み込むQPixmap
        
        if 'c12' in card:
            c12 = QPixmap('card_img/c12.png') # 画像を読み込むQPixmap
        
        if 'c13' in card:
            c13 = QPixmap('card_img/c13.png') # 画像を読み込むQPixmap


        if 'd1' in card:
            d1 = QPixmap('card_img/d1.png') # 画像を読み込むQPixmap
        
        if 'd2' in card:
            d2 = QPixmap('card_img/d2.png') # 画像を読み込むQPixmap
        
        if 'd3' in card:
            d3 = QPixmap('card_img/d3.png') # 画像を読み込むQPixmap

        if 'd4' in card:
            d4 = QPixmap('card_img/d4.png') # 画像を読み込むQPixmap

        if 'd5' in card:
            d5 = QPixmap('card_img/d5.png') # 画像を読み込むQPixmap
             
        if 'd6' in card:
            d6 = QPixmap('card_img/d6.png') # 画像を読み込むQPixmap
        
        if 'd7' in card:
            d7 = QPixmap('card_img/d7.png') # 画像を読み込むQPixmap
        
        if 'd8' in card:
            d8 = QPixmap('card_img/d8.png') # 画像を読み込むQPixmap

        if 'd9' in card:
            d9 = QPixmap('card_img/d9.png') # 画像を読み込むQPixmap
            
        if 'd10' in card:
            d10 = QPixmap('card_img/d10.png') # 画像を読み込むQPixmap

        if 'd11' in card:
            d11 = QPixmap('card_img/d11.png') # 画像を読み込むQPixmap
        
        if 'd12' in card:
            d12 = QPixmap('card_img/d12.png') # 画像を読み込むQPixmap
        
        if 'd13' in card:
            d13 = QPixmap('card_img/d13.png') # 画像を読み込むQPixmap

        if 'h1' in card:
            h1 = QPixmap('card_img/h1.png') # 画像を読み込むQPixmap
        
        if 'h2' in card:
            h2 = QPixmap('card_img/h2.png') # 画像を読み込むQPixmap
        
        if 'h3' in card:
            h3 = QPixmap('card_img/h3.png') # 画像を読み込むQPixmap

        if 'h4' in card:
            h4 = QPixmap('card_img/h4.png') # 画像を読み込むQPixmap

        if 'h5' in card:
            h5 = QPixmap('card_img/h5.png') # 画像を読み込むQPixmap
             
        if 'h6' in card:
            h6 = QPixmap('card_img/h6.png') # 画像を読み込むQPixmap
        
        if 'h7' in card:
            h7 = QPixmap('card_img/h7.png') # 画像を読み込むQPixmap
        
        if 'h8' in card:
            h8 = QPixmap('card_img/h8.png') # 画像を読み込むQPixmap

        if 'h9' in card:
            h9 = QPixmap('card_img/h9.png') # 画像を読み込むQPixmap
            
        if 'h10' in card:
            h10 = QPixmap('card_img/h10.png') # 画像を読み込むQPixmap

        if 'h11' in card:
            h11 = QPixmap('card_img/h11.png') # 画像を読み込むQPixmap
        
        if 'h12' in card:
            h12 = QPixmap('card_img/h12.png') # 画像を読み込むQPixmap
        
        if 'h13' in card:
            h13 = QPixmap('card_img/h13.png') # 画像を読み込むQPixmap


        if 's1' in card:
            s1 = QPixmap('card_img/s1.png') # 画像を読み込むQPixmap
        
        if 's2' in card:
            s2 = QPixmap('card_img/s2.png') # 画像を読み込むQPixmap
        
        if 's3' in card:
            s3 = QPixmap('card_img/s3.png') # 画像を読み込むQPixmap

        if 's4' in card:
            s4 = QPixmap('card_img/s4.png') # 画像を読み込むQPixmap

        if 's5' in card:
            s5 = QPixmap('card_img/s5.png') # 画像を読み込むQPixmap
             
        if 's6' in card:
            s6 = QPixmap('card_img/s6.png') # 画像を読み込むQPixmap
        
        if 's7' in card:
            s7 = QPixmap('card_img/s7.png') # 画像を読み込むQPixmap
        
        if 's8' in card:
            s8 = QPixmap('card_img/s8.png') # 画像を読み込むQPixmap

        if 's9' in card:
            s9 = QPixmap('card_img/s9.png') # 画像を読み込むQPixmap
            
        if 's10' in card:
            s10 = QPixmap('card_img/s10.png') # 画像を読み込むQPixmap

        if 's11' in card:
            s11 = QPixmap('card_img/s11.png') # 画像を読み込むQPixmap
        
        if 's12' in card:
            s12 = QPixmap('card_img/s12.png') # 画像を読み込むQPixmap
        
        if 'c13' in card:
            c13 = QPixmap('card_img/c13.png') # 画像を読み込むQPixmap

        #表示  
        #  
        label = QLabel(self) # 画像を置くQLabel
        label.move(210,50)
        #d10 = QPixmap('card_img/d10.png') # 画像を読み込むQPixmap
        d10 = d10.scaledToWidth(90) # 大きさの変更
        label.setPixmap(d10)

        #カードを押されたらd3などと送れるようにする


        
    def mouseReleaseEvent(self,e):
        p = e.position() # マウスが解放された場所
        #print('(%d,%d)がクリックされた'%(p.x(),p.y()))



       
qAp = QApplication(sys.argv)
mado = main()
mado.show()
qAp.exec()