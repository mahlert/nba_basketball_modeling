import csv

class Player:

    name = ""
    position = ""
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

    def __init__(self, name, position, fgPerc, threesMade, adjustedFG, freeThrowPerc, rebounds, assists, steals, blocks, turnovers, ptsPerGame):
        self.name = name
        self.position = position
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

def main():

    # Array of players
    players = []

    with open('2017_2018.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Start at line 3
        next(csv_reader)
        next(csv_reader)

        for line in csv_reader:

            # Cut characters after backslash
            name = line[0]
            terminator = name.index('\\')

            # Create new player in arrays
            x = Player(name[:terminator],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11])
            players.append(x)

    for i in players:
        print(i.name)


main()