import sys
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtCore import Signal, Slot, QSize
import json
import socket
import threading

BUFFER_SIZE = 1024
IP = "192.168.10.103"
PORT = 25565

put_card = -2


def check_strength(top, put, revolution):
    st = [12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
    if st[int(top[1:])-1] < st[int(put[1:])-1] and not revolution:
        return True
    elif st[int(top[1:])-1] > st[int(put[1:])-1] and revolution:
        return True
    else:
        return False

class main(QWidget):
    realod_signal = Signal(str) 
    def __init__(self):
        super().__init__()

        self.realod_signal.connect(self.reload_field)
        self.numberofcards = [13, 13, 13, 13]
        self.myid = 10
        self.turn = 11
        self.first_trigger = True
        
        self.setWindowTitle('犬富豪') # ウィンドウのタイトル
        self.setGeometry(300,100,850,700) # ウィンドウの位置と大きさ
        self.setFixedSize(900,800)
        self.setStyleSheet("QWidget{ background-color: green }")

            # 右上の文字のstyle設定
        self.labelStyleP = """QLabel {
            color:            black;  /* 文字色 */
            font-size:        20px;     /* 文字サイズ */
            background-color: white;  /* 背景色 */
        }"""

        # 自分の手札の表示に使う変数の定義
        self.label_my_card = []
        self.btn = []

    def btn_event(self, num):
        global put_card
        if self.myid == self.turn:
            put_card = num

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
        labelT = QLabel("犬富豪",self)
        labelT.setStyleSheet(labelStyle)
        labelT.move(0,0)

        # 1P
        labelP1 = QLabel("Player1  ", self)
        labelP1.setObjectName("P1")
        labelP1.setStyleSheet(self.labelStyleP)
        labelP1.move(400,0)
        number1 = QLabel("残り 0枚", self)
        number1.setObjectName("number1P")
        number1.setStyleSheet(self.labelStyleP)
        number1.move(400,30)

        # 2P
        labelP2 = QLabel("Player2  ", self)
        labelP2.setObjectName("P2")
        labelP2.setStyleSheet(self.labelStyleP)
        labelP2.move(500,0)
        number2 = QLabel("残り 0枚", self)
        number2.setObjectName("number2P")
        number2.setStyleSheet(self.labelStyleP)
        number2.move(500,30)

        # 3P
        labelP3 = QLabel("Player3  ", self)
        labelP3.setObjectName("P3")
        labelP3.setStyleSheet(self.labelStyleP)
        labelP3.move(600,0)
        number3 = QLabel("残り 0枚", self)
        number3.setObjectName("number3P")
        number3.setStyleSheet(self.labelStyleP)
        number3.move(600,30)

        # 4P
        labelP4 = QLabel("Player4  ", self)
        labelP4.setObjectName("P4")
        labelP4.setStyleSheet(self.labelStyleP)
        labelP4.move(700,0)
        number4 = QLabel("残り 0枚", self)
        number4.setObjectName("number4P")
        number4.setStyleSheet(self.labelStyleP)
        number4.move(700,30)

        # TOPカード
        label_Nowcard = QLabel(self) # 画像を置くQLabel
        label_Nowcard.setObjectName("nowcard")
        label_Nowcard.move(370 ,250)
        pix = QPixmap("./card_img/card_back.png") # 画像を読み込むQPixmap
        pix = pix.scaledToWidth(150) # 大きさの変更
        label_Nowcard.setPixmap(pix)

        #敵のカード
        back_cards = [QPixmap('./card_img/card_back_left.png').scaledToWidth(150), QPixmap('./card_img/card_back.png').scaledToWidth(100), QPixmap('./card_img/card_back_right.png').scaledToWidth(150)]
        for i in range(3):
            for x in range(13):
                card_label = QLabel(self)
                if i == 0:
                    card_label.move(0, 100 + x*30)
                elif i == 1:
                    card_label.move(200 + x*30, 60)
                else:
                    card_label.move(750, 100 + x*30)
                
                card_label.setPixmap(back_cards[i])
                card_label.setObjectName("enemy{}_cards{}".format(str(i+1), str(x+1)))
        
        #自分のカード
        for x in range(13):
            mycard_label = QLabel(self)
            mycard_label.move(750, 100 + x*30)
            mycard_label.setPixmap(QPixmap('./card_img/card_back.png').scaledToWidth(100))
            mycard_label.setObjectName("my_cards"+str(x+1))
            mycard_label.move(170 + x*35, 550)
        
        #ボタンの表示
        for x in range(13):
            btn = QPushButton(self)
            btn.setObjectName("btn"+str(x+1))
            btn.setStyleSheet("QPushButton {background-color: transparent}")
            btn.setGeometry(170 + x*35, 555, 100, 150)
        
        #for文に組み込むとなぜか関数の引数が全て12になってしまう
        self.findChild(QPushButton, "btn1").clicked.connect(lambda: self.btn_event(0))
        self.findChild(QPushButton, "btn2").clicked.connect(lambda: self.btn_event(1))
        self.findChild(QPushButton, "btn3").clicked.connect(lambda: self.btn_event(2))
        self.findChild(QPushButton, "btn4").clicked.connect(lambda: self.btn_event(3))
        self.findChild(QPushButton, "btn5").clicked.connect(lambda: self.btn_event(4))
        self.findChild(QPushButton, "btn6").clicked.connect(lambda: self.btn_event(5))
        self.findChild(QPushButton, "btn7").clicked.connect(lambda: self.btn_event(6))
        self.findChild(QPushButton, "btn8").clicked.connect(lambda: self.btn_event(7))
        self.findChild(QPushButton, "btn9").clicked.connect(lambda: self.btn_event(8))
        self.findChild(QPushButton, "btn10").clicked.connect(lambda: self.btn_event(9))
        self.findChild(QPushButton, "btn11").clicked.connect(lambda: self.btn_event(10))
        self.findChild(QPushButton, "btn12").clicked.connect(lambda: self.btn_event(11))
        self.findChild(QPushButton, "btn13").clicked.connect(lambda: self.btn_event(12))
        
        #自分のID
        yourID = QLabel("You are Player_", self)
        yourID.setObjectName("yourid")
        yourID.setStyleSheet("font-size: 20pt;")
        yourID.move(390,700)

        #Passボタン
        pass_btn = QPushButton("Pass!!", self)
        pass_btn.setStyleSheet("font-size: 30pt; background-color: white; color: black;")
        pass_btn.setGeometry(600, 700, 100, 30)
        pass_btn.clicked.connect(lambda: self.btn_event(-1))

        #ロードGIF
        movie = QMovie('img/dog0.gif')
        movie.setScaledSize(QSize(900, 800))#画像の大きさを調整
        label1 = QLabel(self)
        label1.setGeometry(0,0,900,800)#画像の位置を調整
        label1.setMovie(movie)
        label1.setObjectName("gif")
        movie.start()
    
    def enemy_reload_data(self, n1, n2, n3, n4, top, winer):
        player = [1, 2, 3, 4]
        player.remove(self.myid+1)
        num = [n1, n2, n3, n4]

        # 残り枚数の更新
        for i in range(4):
            target =  self.findChild(QLabel, "number{}P".format(str(i+1)))
            if num[i] == 0:
                target.setText(str(winer.index(i)+1)+"着")
                target.setStyleSheet("color: red; background-color: white; font-size: 20pt;")
            else:
                target.setText("残り"+str(num[i])+"枚")

        # ターンの表示
        for i in range(4):
            self.findChild(QLabel, "P"+str(i+1)).setText('Player{}  '.format(str(i+1)))
        self.findChild(QLabel, "P"+str(self.turn+1)).setText('Player{}◀︎'.format(str(self.turn+1)))

        # 場に出ているカードの更新
        if top == "T14":
            pix = QPixmap("./card_img/card_back.png")
        else:
            pix = QPixmap("./card_img/" + top)
        pix = pix.scaledToWidth(150) # 大きさの変更
        self.findChild(QLabel, "nowcard").setPixmap(pix)

        # 敵のカードの描画       
        for i in range(len(player)):
            p = player[i]
            if num[p-1] < self.numberofcards[p-1]:
                self.findChild(QLabel, "enemy{}_cards{}".format(str(i+1), str(self.numberofcards[p-1]))).deleteLater()
                self.numberofcards[p-1] -= 1

    def reload_mycard(self, cards):
        if self.first_trigger == True:
            self.findChild(QLabel, "gif").deleteLater()
            self.first_trigger = False
        
        self.findChild(QLabel, "yourid").setText("You are Player"+str(self.myid+1))
        if len(cards) < self.numberofcards[self.myid]:
            self.findChild(QLabel, "my_cards"+str(self.numberofcards[self.myid])).deleteLater()
            self.findChild(QPushButton, "btn"+str(self.numberofcards[self.myid])).deleteLater()
            self.numberofcards[self.myid] -= 1
        for i in range(len(cards)):
            pix = QPixmap("./card_img/" + cards[i]).scaledToWidth(100)
            self.findChild(QLabel, "my_cards"+str(i+1)).setPixmap(pix)


    @Slot(str)
    def reload_field(self, server_data):
        data  = json.loads(server_data)

        # プレイヤーのIDとTOPカード,ターン,勝者の受け取り
        self.myid = data["player_id"]
        top_card = data["field_card"]
        self.turn = data["turn"]
        winer = data["winer"]

        # 残り枚数の受け取り
        card1P = data["remaining_number_list"][0]
        card2P = data["remaining_number_list"][1]
        card3P = data["remaining_number_list"][2]
        card4P = data["remaining_number_list"][3]
        
        # 残り枚数とステータスの表示
        self.enemy_reload_data(card1P, card2P, card3P, card4P, top_card, winer)

        # 自分のカードの受け取り
        mycards = data["my_card_list"]

        # 自分のカードの表示
        self.reload_mycard(mycards)

        """
        if (data["field_card"] != ''):

            # 場に出ているカードの受け取り
            Now_card = "./card_img/" + data["field_card"]

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
        if (data["my_card_list"] != []):
            card = data["my_card_list"]

            # 前の手札カードを削除
            for x in range(len(self.label_my_card)):
                self.label_my_card[x].deleteLater()

            self.label_my_card.clear()

            # 前の手札カードのボタンの削除
            for x in range(len(self.btn)):
                self.btn[x].deleteLater()

            self.btn.clear()

            #カードと照合する
            for x in range(int(len(card))):
            
                if 'c1' in card[x]:
                    pix = QPixmap('./card_img/c1.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                    
                
                if 'c2' in card[x]:
                    pix = QPixmap('./card_img/c2.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                
                if 'c3' in card[x]:
                    pix = QPixmap('./card_img/c3.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 'c4' in card[x]:
                    pix = QPixmap('./card_img/c4.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 'c5' in card[x]:
                    pix = QPixmap('./card_img/c5.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                    
                if 'c6' in card[x]:
                    pix = QPixmap('./card_img/c6.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'c7' in card[x]:
                    pix = QPixmap('./card_img/c7.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'c8' in card[x]:
                    pix = QPixmap('./card_img/c8.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 'c9' in card[x]:
                    pix = QPixmap('./card_img/c9.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                    
                if 'c10' in card[x]:
                    pix = QPixmap('./card_img/c10.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 'c11' in card[x]:
                    pix = QPixmap('./card_img/c11.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'c12' in card[x]:
                    pix = QPixmap('./card_img/c12.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'c13' in card[x]:
                    pix = QPixmap('./card_img/c13.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 'd1' in card[x]:
                    pix = QPixmap('./card_img/d1.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'd2' in card[x]:
                    pix = QPixmap('./card_img/d2.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'd3' in card[x]:
                    pix = QPixmap('./card_img/d3.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 'd4' in card[x]:
                    pix = QPixmap('./card_img/d4.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 'd5' in card[x]:
                    pix = QPixmap('./card_img/d5.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                    
                if 'd6' in card[x]:
                    pix = QPixmap('./card_img/d6.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'd7' in card[x]:
                    pix = QPixmap('./card_img/d7.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'd8' in card[x]:
                    pix = QPixmap('./card_img/d8.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 'd9' in card[x]:
                    pix = QPixmap('./card_img/d9.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                    
                if 'd10' in card[x]:
                    pix = QPixmap('./card_img/d10.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 'd11' in card[x]:
                    pix = QPixmap('./card_img/d11.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'd12' in card[x]:
                    pix = QPixmap('./card_img/d12.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'd13' in card[x]:
                    pix = QPixmap('./card_img/d13.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 'h1' in card[x]:
                    pix = QPixmap('./card_img/h1.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'h2' in card[x]:
                    pix = QPixmap('./card_img/h2.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'h3' in card[x]:
                    pix = QPixmap('./card_img/h3.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 'h4' in card[x]:
                    pix = QPixmap('./card_img/h4.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 'h5' in card[x]:
                    pix = QPixmap('./card_img/h5.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                    
                if 'h6' in card[x]:
                    pix = QPixmap('./card_img/h6.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'h7' in card[x]:
                    pix = QPixmap('./card_img/h7.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'h8' in card[x]:
                    pix = QPixmap('./card_img/h8.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 'h9' in card[x]:
                    pix = QPixmap('./card_img/h9.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 'h10' in card[x]:
                    pix = QPixmap('./card_img/h10.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 'h11' in card[x]:
                    pix = QPixmap('./card_img/h11.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'h12' in card[x]:
                    pix = QPixmap('./card_img/h12.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'h13' in card[x]:
                    pix = QPixmap('./card_img/h13.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 's1' in card[x]:
                    pix = QPixmap('./card_img/s1.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 's2' in card[x]:
                    pix = QPixmap('./card_img/s2.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 's3' in card[x]:
                    pix = QPixmap('./card_img/s3.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 's4' in card[x]:
                    pix = QPixmap('./card_img/s4.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 's5' in card[x]:
                    pix = QPixmap('./card_img/s5.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                    
                if 's6' in card[x]:
                    pix = QPixmap('./card_img/s6.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 's7' in card[x]:
                    pix = QPixmap('./card_img/s7.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 's8' in card[x]:
                    pix = QPixmap('./card_img/s8.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 's9' in card[x]:
                    pix = QPixmap('./card_img/s9.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                    
                if 's10' in card[x]:
                    pix = QPixmap('./card_img/s10.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更

                if 's11' in card[x]:
                    pix = QPixmap('./card_img/s11.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 's12' in card[x]:
                    pix = QPixmap('./card_img/s12.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                if 'c13' in card[x]:
                    pix = QPixmap('./card_img/c13.png') # 画像を読み込むQPixmap
                    pix = pix.scaledToWidth(90) # 大きさの変更
                
                # カードの表示
                self.label_my_card.append(QLabel(self)) # 画像を置くQLabel
                self.label_my_card[x].move(170 + x*35, 550)
                self.label_my_card[x].setPixmap(pix)


            # ボタンの表示
            self.btn = [0]*len(card)
            for x in range(int(len(card))):
                self.btn[x]= QPushButton('',self)
                self.btn[x].setStyleSheet("QPushButton {background-color: transparent}")
                self.btn[x].setGeometry(170 + x*35, 555, 50, 125)
                
            # 押されたカードを出力
            self.btn[0].clicked.connect(lambda: print(card[0])) 
            if len(card) >= 2: 
                self.btn[1].clicked.connect(lambda: print(card[1]))
            if len(card) >= 3:
                self.btn[2].clicked.connect(lambda: print(card[2]))
            if len(card) >= 4:
                self.btn[3].clicked.connect(lambda: print(card[3]))
            if len(card) >= 5:
                self.btn[4].clicked.connect(lambda: print(card[4]))
            if len(card) >= 6:
                self.btn[5].clicked.connect(lambda: print(card[5]))
            if len(card) >= 7:
                self.btn[6].clicked.connect(lambda: print(card[6]))
            if len(card) >= 8:
                self.btn[7].clicked.connect(lambda: print(card[7]))
            if len(card) >= 9:
                self.btn[8].clicked.connect(lambda: print(card[8]))
            if len(card) >= 10:
                self.btn[9].clicked.connect(lambda: print(card[9]))
            if len(card) >= 11:
                self.btn[10].clicked.connect(lambda: print(card[10]))
            if len(card) >= 12:
                self.btn[11].clicked.connect(lambda: print(card[11]))
            if len(card) >= 13:
                self.btn[12].clicked.connect(lambda: print(card[12]))
        """
def start_client(gui):
    global put_card
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, PORT))
        server_data = s.recv(BUFFER_SIZE).decode()

        while True:
            server_data = s.recv(BUFFER_SIZE).decode()
            json_obj  = json.loads(server_data)

            gui.realod_signal.emit(server_data)

            my_card_list = json_obj['my_card_list']
            player_id = int(json_obj['player_id'])
            turn = int(json_obj['turn'])
            field_card = json_obj['field_card']
            revolution = json_obj['revolution']
            winer = json_obj["winer"]

            if len(winer) == 3:
                break
            
            #player_idとturnが一緒なら自分の手札を表示
            if player_id == turn:
                #自分が出すカードをインデックスで指定
                while True:
                    if put_card != -2:
                        if int(put_card) == -1 or check_strength(field_card, my_card_list[int(put_card)], revolution):
                            break
                        print("このカードは出せません")
                        put_card = -2
                #サーバーに自分の出したカードのデータをエンコードして送信
                s.send(str(put_card).encode())
                put_card = -2

if __name__ == "__main__":
    qAp = QApplication(sys.argv)
    mado = main()
    thread = threading.Thread(target=start_client, args=(mado,))
    thread.start()
    mado.create_field()
    mado.show()
    qAp.exec()