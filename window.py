import sys
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton
from PySide6.QtGui import QPixmap
import json

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('大富豪') # ウィンドウのタイトル
        self.setGeometry(200,200,850,700) # ウィンドウの位置と大きさ
        self.setStyleSheet("QWidget{ background-color: green }")

        # ラベルのstyle設定
        labelStyle = """QLabel {
            color:            black;  /* 文字色 */
            font-size:        40px;     /* 文字サイズ */
            background-color: white;  /* 背景色 */
        }"""

        # 文字を表示するところの背景色
        labelTbg = QLabel(self)
        labelTbg.setStyleSheet(labelStyle)
        labelTbg.setGeometry(200,200,900,60)
        labelTbg.move(0,0)

        # タイトル
        labelT = QLabel("大富豪",self)
        labelT.setStyleSheet(labelStyle)
        labelT.move(0,0)


        # 右上の文字のstyle設定
        labelStyleP = """QLabel {
            color:            black;  /* 文字色 */
            font-size:        20px;     /* 文字サイズ */
            background-color: white;  /* 背景色 */
        }"""

        # # プレイヤーごとの残り枚数受け取り
        # json_open = open('Sample.json', 'r')
        # json_load = json.load(json_open)

        # card1P = json_load['Player1']['mai']
        # card2P = json_load['Player2']['mai']
        # card3P = json_load['Player3']['mai']
        # card4P = json_load['Player4']['mai']

        card1P = "13"
        card2P = "13"
        card3P = "13"
        card4P = "13"

        # 1P
        labelP1 = QLabel("Player1", self)
        labelP1.setStyleSheet(labelStyleP)
        labelP1.move(400,0)
        # 残り枚数 1P
        # card1P = str(13)  # ここにJSONから残り枚数情報を持ってくる
        labelcard1P = QLabel("残り"+ card1P + "枚", self)
        labelcard1P.setStyleSheet(labelStyleP)
        labelcard1P.move(400,30)

        # 2P
        labelP2 = QLabel("Player2", self)
        labelP2.setStyleSheet(labelStyleP)
        labelP2.move(500,0)
        # 残り枚数 2P
        # card2P = str(13)
        labelcard2P = QLabel("残り"+ card2P + "枚", self)
        labelcard2P.setStyleSheet(labelStyleP)
        labelcard2P.move(500,30)

        # 3P
        labelP3 = QLabel("Player3", self)
        labelP3.setStyleSheet(labelStyleP)
        labelP3.move(600,0)
        # 残り枚数 3P
        # card3P = str(13)
        labelcard3P = QLabel("残り"+ card3P + "枚", self)
        labelcard3P.setStyleSheet(labelStyleP)
        labelcard3P.move(600,30)

        # 4P
        labelP4 = QLabel("Player4", self)
        labelP4.setStyleSheet(labelStyleP)
        labelP4.move(700,0)
        # 残り枚数 4P
        # card4P = str(13)
        labelcard4P = QLabel("残り"+ card4P + "枚", self)
        labelcard4P.setStyleSheet(labelStyleP)
        labelcard4P.move(700,30)
        


        # 自分以外のカード（裏）の表示
        # 2P
        for x in range(int(card2P)):
            label = QLabel(self) # 画像を置くQLabel
            label.move(0 ,100 + x*30)
            pix = QPixmap('card_img/card_back_left.png') # 画像を読み込むQPixmap
            pix = pix.scaledToWidth(150) # 大きさの変更
            label.setPixmap(pix)

        # 3P
        for x in range(int(card3P)):
            label = QLabel(self) # 画像を置くQLabel
            label.move(200 + x*30 ,60 )
            pix = QPixmap('card_img/card_back.png') # 画像を読み込むQPixmap
            pix = pix.scaledToWidth(100) # 大きさの変更
            label.setPixmap(pix)
        
        # 4P
        for x in range(int(card4P)):
            label = QLabel(self) # 画像を置くQLabel
            label.move(700 ,100 + x*30)
            pix = QPixmap('card_img/card_back_right.png') # 画像を読み込むQPixmap
            pix = pix.scaledToWidth(150) # 大きさの変更
            label.setPixmap(pix)


        # label = QLabel(self) # 画像を置くQLabel
        # label.move(10,10)
        # pix = QPixmap('card_back.png') # 画像を読み込むQPixmap
        # pix = pix.scaledToWidth(100) # 大きさの変更
        # label.setPixmap(pix)


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