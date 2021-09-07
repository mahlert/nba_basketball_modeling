class Player:

    def __init__(self, name, position, seasonData):
        self.name = name
        self.position = position
        self.seasonData = [seasonData]

    def addSeason(self, season):
        self.seasonData.append(season)

    def getName(self):
        return self.name

    def getPosition(self):
        return self.position

    def getSeasonData(self):
        return self.seasonData

    def setName(self, name):
        self.name = name