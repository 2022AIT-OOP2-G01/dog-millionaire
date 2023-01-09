import threading
import socket
import random
import math

player = 4

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
        return "ID: " + str(self.player_id) + " CARDS: " + ', '.join(self.card_list)

def distribute_cards():
    initial = ['c', 'd', 'h', 's']
    card_list = [initial[i] + str(j+1) for i in range(4) for j in range(13)]
    random.shuffle(card_list)
    
    #カードの総枚数が人数で割り切れない場合は一人だけ枚数が少なくなる(要修正?)
    num = math.ceil(52/player)
    cards = [card_list[i:i + num] for i in range(0, len(card_list), num)]
    
    return cards

def main():
    cards = distribute_cards()
    player_list = []
    for i in range(player):
        player_list += [PlayerData(i, cards[i])]
    
    print(player_list)

if __name__ == "__main__":
    main()