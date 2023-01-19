import sys
from PySide6.QtWidgets import QApplication,QWidget,QLabel
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
        

qAp = QApplication(sys.argv)
mado = main()
mado.show()
qAp.exec()