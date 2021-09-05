import csv
import glob
import os

class Player:

    name = ""
    position = ""
    seasonData = []

    def __init__(self, name, position, seasonData):
        self.name = name
        self.position = position
        self.seasonData = seasonData

class Season:

    fgPerc = 0.0
    threesMade = 0
    adjustedFG = 0.0
    freeThrowPerc = 0.0
    rebounds = 0
    assists = 0
    steals = 0
    blocks = 0
    turnovers = 0
    ptsPerGame = 0

    def __init__(self, fgPerc, threesMade, adjustedFG, freeThrowPerc, rebounds, assists, steals, blocks, turnovers, ptsPerGame):
        self.fgPerc = fgPerc
        self.threesMade = threesMade
        self.adjustedFG = adjustedFG
        self.freeThrowPerc  = freeThrowPerc
        self.rebounds  = rebounds
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers
        self.ptsPerGame = ptsPerGame

def printPlayers(players):
    for player in players:
        print(player.name)

def checkPlayer(players, playerName):
    for player in players:
        if(player == playerName):
            return 1

    return -1

def createPlayers():

    players = []

    files = glob.glob("*.csv")
    for file in files:

        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            next(csv_reader)
            next(csv_reader)

            for line in csv_reader:

                szn = Season(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9])

                x = checkPlayer(players, line[0])

                if (x == -1):
                    # New player
                    newPlayer = Player(line[0], line[1], [])
                    newPlayer.seasonData.append(szn)
                    players.append(newPlayer)

                else:
                    # player exists
                    prevSeason = players[x].seasonData
                    prevSeason.append(szn)
                    players[x].seasonData = prevSeason

        return players

def trimNames(players):
    for i in range(len(players)):
        name = players[i].name
        terminator = name.index("\\")
        trimmedName = name[:terminator]
        players[i].name = trimmedName

def main():

    players = createPlayers()

    trimNames(players)


main()