from player import Player
from season import Season
import scrapeCSV as sCSV

def main():

    players = sCSV.createPlayers()

    playerDB = sCSV.playerDatabase(players)

    sCSV.printPlayers(playerDB)

main()