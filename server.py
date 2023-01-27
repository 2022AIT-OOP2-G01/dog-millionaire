import threading
import socket
import random
import json

PORT = 50000
IP = "localhost"
BUFFER_SIZE = 1024
#AF_INET=アドレスファミリーを示す関数　SOCK_STREAM=ソケットタイプを示す関数

player = 4
top_card = ["T14", 0]
revolution = False

#[0] 0:処理なし, 1:データ送信, 2:データ受信
#[1] 出したカード
send_content = [[0, 0], [0, 0], [0, 0], [0, 0]]

player_list = []
rank = []
turn = 0
order = [i for i in range(player)]
random.shuffle(order)

class PlayerData():
    def __init__(self, id, card):
        self.player_id = id
        self.card_list = card

    def getCardList(self):
        return self.card_list

    def getId(self):
        return self.player_id

    def getNumberOfCards(self):
        return len(self.card_list)
    
    def deleteCard(self, index):
        del self.card_list[index]
    
    def setCard(self, card):
        self.card_list = card
    
    def setId(self, id):
        self.player_id = id
    
    def __str__(self):
        return "ID: " + str(self.player_id) + " CARDS: " + ', '.join(self.card_list) + " NOC: " + str(len(self.card_list))

def get_server_data(id):
    server_data = {
        #プレイヤーID
        "player_id": id,
        #革命状態
        "revolution": revolution,
        #場に出ているカード
        "field_card": top_card[0],
        #誰のターンか
        "turn": order[turn%player],
        #誰が買ったか
        "winer": rank,
        #それぞれのプレイヤーの残り枚数
        "remaining_number_list":[player_list[0].getNumberOfCards(), player_list[1].getNumberOfCards(), player_list[2].getNumberOfCards(), player_list[3].getNumberOfCards()],
        #自分の持っているカード
        "my_card_list": player_list[id].getCardList()
    } 

    return json.dumps(server_data)

def distribute_cards():
    initial = ['c', 'd', 'h', 's']
    card_list = [initial[i] + str(j+1) for i in range(4) for j in range(13)]
    random.shuffle(card_list)
    
    #カードの総枚数が人数で割り切れない場合は一人だけ枚数が少なくなる(要修正?)
    # num = math.ceil(52/player)
    # cards = [card_list[i:i + num] for i in range(0, len(card_list), num)]

    #↑の修正案
    num_split = [(len(card_list) + i) // player for i in range(player)]
    start = 0
    end = 0
    cards = []
    for i in range(player):
        end += num_split[i]
        c_buf = card_list[start:end]
        cards.append(sorted(c_buf, key=lambda num: int(num[1:])))
        start+=num_split[i]

    #テスト用
    #cards = [["d3", "c1"], ["c6", "c5"], ["c3", "s0"], ["k5", "k8"]]

    return cards

def check_strength(top, put):
    st = [12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
    if st[int(top[1:])-1] < st[int(put[1:])-1] and not revolution:
        return True
    elif st[int(top[1:])-1] > st[int(put[1:])-1] and revolution:
        return True
    else:
        return False

def recv_client(sock, addr, id):
    global send_content
    print('Player{} connected. {}'.format(id, addr))

    while send_content[id][0] == 0:
        pass

    sock.send(get_server_data(id).encode())
    send_content[id][0] = 0

    while True:
        if send_content[id][0] == 1:
            sock.send(get_server_data(id).encode())
            send_content[id][0] = 0
            if order[turn%player] == id:
                send_content[id][1] = sock.recv(BUFFER_SIZE).decode()
                send_content[id][0] = 2

def main():
    global revolution, player, player_list, rank, turn, send_content
    cards = distribute_cards()

    for i in range(player):
        player_list += [PlayerData(i, cards[i])]
        #print(player_list[i])

    #クライアントとの接続処理
    #４人繋がるまでここで待つ
    #4人繋がったら下の処理を行う

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        #ソケット登録   
        s.bind((IP, PORT))
        #ソケット接続待機
        s.listen()

        for i in range(4):
            (connection, client) = s.accept()
                # スレッドクラスのインスタンス化
            thread = threading.Thread(target=recv_client, args=(connection, client, i))
            # スレッド処理開始
            thread.start()
    
    for i in range(4):
        send_content[i][0] = 1

    while send_content[0][0] or send_content[1][0] or send_content[2][0] or send_content[3][0]:
        pass
    print("GameStart")

    #この先未テスト

    while True:
        now = order[turn%player]
        if len(rank) == player-1:
            break

        if top_card[1] == now:
            top_card[0] = "T14"
            revolution = False

        if not now in rank:
            # 一斉送信
            for i in range(4):
                send_content[i][0] = 1
        
            while send_content[now][0] != 2:
                pass
            #一斉送信＆レシーブ終了

            put_card_index = int(send_content[now][1])

            if put_card_index == -1:
                print("Player{} Pass!!".format(now))
            else:
                put_card = player_list[now].getCardList()[put_card_index]

                if player_list[now].getNumberOfCards() == 1:
                    #終了処理
                    rank.append(now)
                    top_card[1] = order[(turn-1)%player]
                    print("Turn{}: Player{} Finish!!!".format(turn, now))
                else:
                    if int(put_card[1:]) == 8:
                        turn-=1
                    if int(put_card[1:]) == 11:
                        revolution = True
                    
                    top_card[1] = now
                    print("Turn{}: Player{} put {}".format(turn, now, put_card))
                
                top_card[0] = put_card
                player_list[now].deleteCard(put_card_index)
        turn+=1

    # while True:
    #     now = order[turn%player]
    #     if len(rank) == player-1:
    #         break

    #     #誰もカードを出さなかったら初期値T14に変更
    #     if top_card[1] == now:
    #         top_card[0] = "T14"
    #         revolution = False
            
    #     print("ID: " + str(now) + "のターン")
    #     print("Revolution: " + str(revolution))
    #     print("TOP: " + top_card[0])
    #     print("CARDS: " + ', '.join(player_list[now].getCardList()))

    #     if not now in rank:
    #         while True:
    #             send_content[id][0] = 1
    #             put_card_index = int(input("何を出す(index)>"))
    #             put_card = player_list[now].getCardList()[put_card_index]
    #             if put_card_index == -1:
    #                 print("Pass!!")
    #                 break
    #             elif check_strength(top_card[0], put_card):
    #                 if player_list[now].getNumberOfCards() == 1:
    #                     #終了処理
    #                     rank.append(now)
    #                 else:
    #                     if int(put_card[1:]) == 8:
    #                         turn-=1
                        
    #                     if int(put_card[1:]) == 11:
    #                         revolution = True
                    
    #                 top_card[0] = put_card
    #                 top_card[1] = now
    #                 player_list[now].deleteCard(put_card_index)
    #                 break
    #             print("出せないっす")

    #     print()
    #     turn+=1
    # print("終了")

if __name__ == "__main__":
    main()