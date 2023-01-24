import sys
from PySide6.QtWidgets import QApplication,QWidget,QLabel
from PySide6.QtGui import QPixmap
import json
import data

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('大富豪') # ウィンドウのタイトル
        self.setGeometry(300,100,850,700) # ウィンドウの位置と大きさ
        self.setFixedSize(900,800)
        self.setStyleSheet("QWidget{ background-color: green }")

            # 右上の文字のstyle設定
        self.labelStyleP = """QLabel {
            color:            black;  /* 文字色 */
            font-size:        20px;     /* 文字サイズ */
            background-color: white;  /* 背景色 */
        }"""

        # サーバーからのデータ受け取り
        self.dataa = json.loads(data.get_server_data())

        # 残り枚数の表示に使う変数
        self.labelcard1P = ''
        self.labelcard2P = ''
        self.labelcard3P = ''
        self.labelcard4P = ''

        # カードの裏面の表示に使う変数
        self.label_Backcard2P = []
        self.label_Backcard3P = []
        self.label_Backcard4P = []

        # 場に出ているカードの表示に使う変数
        self.label_Nowcard = ''
        

    def create_field(self):
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

        # 1P
        labelP1 = QLabel("Player1", self)
        labelP1.setStyleSheet(self.labelStyleP)
        labelP1.move(400,0)

        # 2P
        labelP2 = QLabel("Player2", self)
        labelP2.setStyleSheet(self.labelStyleP)
        labelP2.move(500,0)

        # 3P
        labelP3 = QLabel("Player3", self)
        labelP3.setStyleSheet(self.labelStyleP)
        labelP3.move(600,0)

        # 4P
        labelP4 = QLabel("Player4", self)
        labelP4.setStyleSheet(self.labelStyleP)
        labelP4.move(700,0)
    


    def reload_field(self):

        if (self.dataa["remaining_number_list"] != []):

            # 残り枚数の受け取り
            card1P = self.dataa["remaining_number_list"][0]
            card2P = self.dataa["remaining_number_list"][1]
            card3P = self.dataa["remaining_number_list"][2]
            card4P = self.dataa["remaining_number_list"][3]

            
            # 残り枚数表示
            # 1P
            if (self.labelcard1P != ''):
                self.labelcard1P.deleteLater()

            self.labelcard1P = QLabel("残り"+ str(card1P) + "枚", self)
            self.labelcard1P.setStyleSheet(self.labelStyleP)
            self.labelcard1P.move(400,30)

            # 2P
            if (self.labelcard2P != ''):
                self.labelcard2P.deleteLater()

            self.labelcard2P = QLabel("残り"+ str(card2P) + "枚", self)
            self.labelcard2P.setStyleSheet(self.labelStyleP)
            self.labelcard2P.move(500,30)

            # 3P
            if (self.labelcard3P != ''):
                self.labelcard3P.deleteLater()

            self.labelcard3P = QLabel("残り"+ str(card3P) + "枚", self)
            self.labelcard3P.setStyleSheet(self.labelStyleP)
            self.labelcard3P.move(600,30)

            # 4P
            if (self.labelcard4P != ''):
                self.labelcard4P.deleteLater()

            self.labelcard4P = QLabel("残り"+ str(card4P) + "枚", self)
            self.labelcard4P.setStyleSheet(self.labelStyleP)
            self.labelcard4P.move(700,30)



            # 自分以外のカード（裏）の表示

            # 2P
            # 前のカードを削除
            for x in range(len(self.label_Backcard2P)):
                self.label_Backcard2P[x].deleteLater()

                self.label_Backcard2P.clear()

            # 今のカードの表示
            for x in range(card2P):
                self.label_Backcard2P.append(QLabel(self))
                self.label_Backcard2P[x].move(0 ,100 + x*30)
                pix = QPixmap('card_img/card_back_left.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(150) # 大きさの変更
                self.label_Backcard2P[x].setPixmap(pix)
            

            # 3P
            # 前のカードを削除
            for x in range(len(self.label_Backcard3P)):
                self.label_Backcard3P[x].deleteLater()

                self.label_Backcard3P.clear()

            # 今のカードの表示
            for x in range(card3P):
                self.label_Backcard3P.append(QLabel(self))
                self.label_Backcard3P[x].move(200 + x*30 ,60 )
                pix = QPixmap('card_img/card_back.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(100) # 大きさの変更
                self.label_Backcard3P[x].setPixmap(pix)


            # 4P
            # 前のカードを削除
            for x in range(len(self.label_Backcard4P)):
                self.label_Backcard4P[x].deleteLater()

                self.label_Backcard4P.clear()

            # 今のカードの表示
            for x in range(card4P):
                self.label_Backcard4P.append(QLabel(self))
                self.label_Backcard4P[x].move(750 ,100 + x*30)
                pix = QPixmap('card_img/card_back_right.png') # 画像を読み込むQPixmap
                pix = pix.scaledToWidth(150) # 大きさの変更
                self.label_Backcard4P[x].setPixmap(pix)


        if (self.dataa["field_card"] != ''):

            # 場に出ているカードの受け取り
            Now_card = "card_img/" + self.dataa["field_card"]

            # 前場に出ていたカードの削除
            if self.label_Nowcard != '':
                self.label_Nowcard.deleteLater()

            # 場面に出ているカードの表示
            self.label_Nowcard = QLabel(self) # 画像を置くQLabel
            self.label_Nowcard.move(370 ,250)
            pix = QPixmap(Now_card) # 画像を読み込むQPixmap
            pix = pix.scaledToWidth(150) # 大きさの変更
            self.label_Nowcard.setPixmap(pix)



        

qAp = QApplication(sys.argv)
mado = main()
mado.create_field()
mado.reload_field()
mado.show()
qAp.exec()
