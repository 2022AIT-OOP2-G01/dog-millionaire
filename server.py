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

def main():
    pass

if __name__ == "__main__":
    main()