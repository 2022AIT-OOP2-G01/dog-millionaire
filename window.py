import sys
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton
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


        # 自分の手札データの取得
        if (self.dataa["my_card_list"] != []):
            card = self.dataa["my_card_list"]

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
                label.move(170 + x*35, 550)
                label.setPixmap(pix)

            # ボタンの表示
            btn = [0]*len(card)
            for x in range(int(len(card))):
                btn[x]= QPushButton('',self)
                btn[x].setStyleSheet("QPushButton {background-color: transparent}")
                btn[x].setGeometry(170 + x*35, 555, 50, 125)
                
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
mado.create_field()
mado.reload_field()
mado.show()
qAp.exec()
