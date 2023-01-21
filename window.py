import sys
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton
from PySide6.QtGui import QPixmap

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('大富豪') # ウィンドウのタイトル
        self.setGeometry(300,300,500,500) # ウィンドウの位置と大きさ
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
        card = ['d10', 'd3','h12', 'd6', 'h1', 'h11', 'd9', 'c1', 's5', 's10', 'c13', 'h10', 'c2']

        # カードの長さ取得
        len(card)
        
         #カードと照合する
        for x in range(int(len(card))):
           
            if 'c1' in card[x]:
                pix = QPixmap('card_img/c1.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
                
            
            if 'c2' in card[x]:
                pix = QPixmap('card_img/c2.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
               
            
            if 'c3' in card[x]:
                pix = QPixmap('card_img/c3.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 'c4' in card[x]:
                pix = QPixmap('card_img/c4.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 'c5' in card[x]:
                pix = QPixmap('card_img/c5.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
                
            if 'c6' in card[x]:
                pix = QPixmap('card_img/c6.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'c7' in card[x]:
                pix = QPixmap('card_img/c7.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'c8' in card[x]:
                pix = QPixmap('card_img/c8.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 'c9' in card[x]:
                pix = QPixmap('card_img/c9.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
                
            if 'c10' in card[x]:
                pix = QPixmap('card_img/c10.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 'c11' in card[x]:
                pix = QPixmap('card_img/c11.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'c12' in card[x]:
                pix = QPixmap('card_img/c12.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'c13' in card[x]:
                pix = QPixmap('card_img/c13.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 'd1' in card[x]:
                pix = QPixmap('card_img/d1.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'd2' in card[x]:
                pix = QPixmap('card_img/d2.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'd3' in card[x]:
                pix = QPixmap('card_img/d3.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 'd4' in card[x]:
                pix = QPixmap('card_img/d4.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 'd5' in card[x]:
                pix = QPixmap('card_img/d5.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
                
            if 'd6' in card[x]:
                pix = QPixmap('card_img/d6.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'd7' in card[x]:
                pix = QPixmap('card_img/d7.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'd8' in card[x]:
                pix = QPixmap('card_img/d8.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 'd9' in card[x]:
                pix = QPixmap('card_img/d9.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
                
            if 'd10' in card[x]:
                pix = QPixmap('card_img/d10.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 'd11' in card[x]:
                pix = QPixmap('card_img/d11.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'd12' in card[x]:
                pix = QPixmap('card_img/d12.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'd13' in card[x]:
                pix = QPixmap('card_img/d13.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 'h1' in card[x]:
                pix = QPixmap('card_img/h1.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'h2' in card[x]:
                pix = QPixmap('card_img/h2.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'h3' in card[x]:
                pix = QPixmap('card_img/h3.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 'h4' in card[x]:
                pix = QPixmap('card_img/h4.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 'h5' in card[x]:
                pix = QPixmap('card_img/h5.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
                
            if 'h6' in card[x]:
                pix = QPixmap('card_img/h6.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'h7' in card[x]:
                pix = QPixmap('card_img/h7.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'h8' in card[x]:
                pix = QPixmap('card_img/h8.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 'h9' in card[x]:
                pix = QPixmap('card_img/h9.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 'h10' in card[x]:
                pix = QPixmap('card_img/h10.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 'h11' in card[x]:
                pix = QPixmap('card_img/h11.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'h12' in card[x]:
                pix = QPixmap('card_img/h12.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'h13' in card[x]:
                pix = QPixmap('card_img/h13.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 's1' in card[x]:
                pix = QPixmap('card_img/s1.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 's2' in card[x]:
                pix = QPixmap('card_img/s2.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 's3' in card[x]:
                pix = QPixmap('card_img/s3.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 's4' in card[x]:
                pix = QPixmap('card_img/s4.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 's5' in card[x]:
                pix = QPixmap('card_img/s5.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
                
            if 's6' in card[x]:
                pix = QPixmap('card_img/s6.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 's7' in card[x]:
                pix = QPixmap('card_img/s7.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 's8' in card[x]:
                pix = QPixmap('card_img/s8.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 's9' in card[x]:
                pix = QPixmap('card_img/s9.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
                
            if 's10' in card[x]:
                pix = QPixmap('card_img/s10.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更

            if 's11' in card[x]:
                pix = QPixmap('card_img/s11.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 's12' in card[x]:
                pix = QPixmap('card_img/s12.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            if 'c13' in card[x]:
                pix = QPixmap('card_img/c13.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(90) # 大きさの変更
            
            # カードの表示
            label = QLabel(self) # 画像を置くQLabel
            label.move(210 + x*50, 550)
            label.setPixmap(pix)

        # ボタンの表示
        btn = [0]*len(card)
        for x in range(int(len(card))):
            btn[x]= QPushButton('',self)
            btn[x].setGeometry(215 + x*50, 550, 50, 100)
            
        # 押されたカードを出力
        btn[0].clicked.connect(lambda: print(card[0])) 
        if len(card) > 2: 
            btn[1].clicked.connect(lambda: print(card[1]))
        if len(card) > 3:
            btn[2].clicked.connect(lambda: print(card[2]))
        if len(card) > 4:
            btn[3].clicked.connect(lambda: print(card[3]))
        if len(card) > 4:
            btn[4].clicked.connect(lambda: print(card[4]))
        if len(card) > 5:
            btn[5].clicked.connect(lambda: print(card[5]))
        if len(card) > 6:
            btn[6].clicked.connect(lambda: print(card[6]))
        if len(card) > 7:
            btn[7].clicked.connect(lambda: print(card[7]))
        if len(card) > 8:
            btn[8].clicked.connect(lambda: print(card[8]))
        if len(card) > 9:
            btn[9].clicked.connect(lambda: print(card[9]))
        if len(card) > 10:
            btn[10].clicked.connect(lambda: print(card[10]))
        if len(card) > 11:
            btn[11].clicked.connect(lambda: print(card[11]))
        if len(card) > 12:
            btn[12].clicked.connect(lambda: print(card[12]))

qAp = QApplication(sys.argv)
mado = main()
mado.show()
qAp.exec()