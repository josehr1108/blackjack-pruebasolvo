import random

cardsValue = ['A',2,3,4,5,6,7,8,9,'J','Q','K']
typeValue = ['Hearts','Diamonds','Clubs','Spades']
initialDeck = []
players = []
deckCardsAmount = 52
mazeValueGoal = 21

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

def beginGame():
    currentPlayerIndex = 0
    while currentPlayerIndex != len(players):
        currentPlayer = players[currentPlayerIndex]
        response = input(f"({currentPlayer.name})You want another card?(s/n)")
        if response == 's':
            newCard = initialDeck.pop()
            currentPlayer.maze.append(newCard)
        elif response == 'n':
            currentPlayerIndex += 1
        else:
            print("Invalid option")
            continue

def getMazeValue(maze):
    sum = 0
    for card in maze:
        cardValue = card['card']
        if cardValue in ('J','Q','K',):
            sum += 10
        elif cardValue == 'A':
            tempSum = sum + 11
            if tempSum > 21:
                sum += 1
            else:
                sum += 11
        else:
            sum += cardValue
    return sum

def getWinner():
    winnerValue = 0
    winner = None
    for player in players:
        playerMazeValue = getMazeValue(player.maze)
        if playerMazeValue > 21:
            print(f"{player.name} lose")
        else:
            if playerMazeValue > winnerValue:
                winnerValue = playerMazeValue
                winner = player
            elif playerMazeValue == winnerValue and len(player.maze) == 5:
                winner = player
    if winner != None:
        print(f"Winner is: {winner.name}")
        printPlayerMaze(winner)
    else:
        print(f"No one wins")

def printPlayerMaze(player):
    print("Winner maze:")
    for card in player.maze:
        print(f"{card['card']} of {card['type']}")

if  __name__ == "__main__":
    numPlayers = int(input("How many players you want? "))
    initDeck()
    distributeCards(numPlayers)
    beginGame()
    getWinner()