class Season:

    def __init__(self, year, fgPerc, threesMade, adjustedFG, freeThrowPerc, rebounds, assists, steals, blocks, turnovers, ptsPerGame):
        self.year = year
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

    def getYear(self):
        return self.year

    def getFGPerc(self):
        return self.fgPerc

    def getThreesMade(self):
        return self.threesMade

    def getAdjustedFG(self):
        return self.adjustedFG

    def getFreeThrowPerc(self):
        return self.freeThrowPerc

    def getRebounds(self):
        return self.rebounds

    def getAssists(self):
        return self.assists

    def getSteals(self):
        return self.steals

    def getBlocks(self):
        return self.blocks

    def getTurnovers(self):
        return self.turnovers

    def getPtsPerGame(self):
        return self.ptsPerGame