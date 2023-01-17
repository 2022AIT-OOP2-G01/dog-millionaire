import threading
import socket
import random

player = 4
top_card = ["T14", 0]
revolution = False

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

    return cards

def check_strength(top, put):
    st = [12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
    if st[int(top[1:])-1] < st[int(put[1:])-1] and not revolution:
        return True
    elif st[int(top[1:])-1] > st[int(put[1:])-1] and revolution:
        return True
    else:
        return False

def main():
    global revolution
    cards = distribute_cards()
    player_list = []

    for i in range(player):
        player_list += [PlayerData(i, cards[i])]
        #print(player_list[i])
    
    order = [i for i in range(player)]
    random.shuffle(order)

    #サーバーとの接続処理

    turn = 0
    while True:
        now = order[turn%player]

        #誰もカードを出さなかったら初期値T14に変更
        if top_card[1] == now:
            top_card[0] = "T14"
            revolution = False
            
        print("ID: " + str(now) + "のターン")
        print("Revolution: " + str(revolution))
        print("TOP: " + top_card[0])
        print("CARDS: " + ', '.join(player_list[now].getCardList()))

        while True:
            put_card_index = int(input("何を出す(index)>"))
            put_card = player_list[now].getCardList()[put_card_index]
            if put_card_index == -1:
                print("Pass!!")
                break
            elif check_strength(top_card[0], put_card):
                if int(put_card[1:]) == 8:
                    turn-=1
                
                if int(put_card[1:]) == 11:
                    revolution = True
                
                top_card[0] = put_card
                top_card[1] = now
                player_list[now].deleteCard(put_card_index)
                break
            print("出せないっす")

        print()
        turn+=1

if __name__ == "__main__":
    main()