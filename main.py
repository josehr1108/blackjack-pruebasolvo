import random
from functools import reduce

MAZE_MAX_VALUE = 21
DECK_CARDS_AMOUNT = 52

cardValues = ('A',2,3,4,5,6,7,8,9,'J','Q','K')
cardTypes = ('Hearts','Diamonds','Clubs','Spades')
initialDeck = [(random.choice(cardValues),random.choice(cardTypes)) for x in range(DECK_CARDS_AMOUNT)]
players = []

def distributeCards(numPlayers):
    for i in range(numPlayers):   #initially distribute 2 cards per player, each player has a maze or deck
        player = {"name": f"Player {i+1}", "maze": initialDeck[:2]}   
        del initialDeck[:2]
        players.append(player)

def beginGame():
    for player in players:
        response = input(f"({player['name']})You want a card?(y/n)")
        while response != 'n':
            if response == 'y':
                player['maze'] += [initialDeck.pop()]
            else:
                print("Invalid option")
                response = input(f"({player['name']})You want another card?(y/n)")
                continue
            response = input(f"({player['name']})You want another card?(y/n)")

def getCardValue(cardVal):
    if cardVal in ('J','Q','K',):
        return 10
    elif cardVal == 'A':
        return (1,11)[random.randrange(0,2) == 1]
    else:
        return cardVal

def getMazeValue(maze):
    return reduce(lambda accumulator,card: accumulator + getCardValue(card[0]),maze,0)

def getWinner():
    resultsList = [tup for tup in ((player,getMazeValue(player['maze'])) for player in players) if tup[1] <= 21]
    resultsList.sort(key = lambda obj: obj[1], reverse=True) #sort by final score 
    winner = None
    winnerScore = 0
    for result in resultsList[:3]:      #iterate through 3 highest scores
        if result[1] > winnerScore:     #compare scores to max score
             winner = result[0]         #winner dict (name and maze keys)
             winnerScore = result[1]    #winner maze value
        elif result[1] == winnerScore and len(result[0]['maze']) == 5:
            winner = result[0]
    if winner != None:
        print(f"Winner is: {winner['name']}")
        printMaze(winner['maze'])
    else:
        print("No one wins")

def printMaze(maze):
    print("Winner maze:")
    for card in maze:
        print(f"{card[0]} of {card[1]}")

if  __name__ == "__main__":     #call from terminal with python main.py
    numPlayers = int(input("How many players you want? "))
    distributeCards(numPlayers)
    beginGame()
    getWinner()