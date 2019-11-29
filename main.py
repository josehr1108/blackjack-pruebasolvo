import random
import functools

cardsValue = ['A',2,3,4,5,6,7,8,9,'J','Q','K']
typeValue = ['Hearts','Diamonds','Treboles','Picas']
initialDeck = []
players = []
deckCardsAmount = 52

class Player():
    def __init__(self,name):
        self.name = name
        self.maze = []
        self.mazeValue = 0

def initDeck():
    for i in range(deckCardsAmount):
        cardIndex = random.randint(0, len(cardsValue) - 1)
        typeIndex = random.randint(0, len(typeValue) - 1)
        initialDeck.append({'card': cardsValue[cardIndex], 'type': typeValue[typeIndex]})

def distributeCards(numPlayers):
    for i in range(numPlayers):
        player = Player("Player " + str(i+1))
        player.maze.append(initialDeck.pop())
        player.maze.append(initialDeck.pop())
        players.append(player)

if  __name__ == "__main__":
    numPlayers = int(input("Ingrese la cantidad deseada de jugadores"))
    initDeck()
    distributeCards(numPlayers)
