import csv
import glob
import os
from player import Player
from season import Season

def printPlayers(players):
    for player in players:
        print(player.getName())

def searchPlayer(L, target):
    start = 0
    end = len(L) - 1
    while start <= end:
        middle = (start + end) // 2
        midpoint = L[middle].getName()
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return middle

    return -1

def trimYear(file):
    terminator = file.index(".")
    trimmedYear = file[:terminator]
    return trimmedYear

def trimName(name):
    terminator = name.index("\\")
    trimmedName = name[:terminator]
    return trimmedName

def insertNewPlayer(players, newPlayer):
    index = -1
    for i in range(len(players)):
        if players[i].getName() > newPlayer.getName():
            index = i
            break

    players = players[:index] + [newPlayer] + players[index:]
    return players

def createPlayers():

    players = []

    files = glob.glob("*.csv")

    for file in files:

        # Open the file to reader
        with open(file, 'r') as csv_file:

            # Create a line reader
            csv_reader = csv.reader(csv_file)

            # Move to third line of file (Skipping example and blank line)
            next(csv_reader)
            next(csv_reader)

            # Store string of csv file name to store as season name in a player
            year = trimYear(file)

            # for each line of player data in a CSV file
            for line in csv_reader:

                # Store current values of line with year file and the data values
                szn = Season(year, line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9],line[10], line[11])

                # Store the value of the trimmed player name for reading ease
                trimmedName = trimName(line[0])

                # Store temporary new player with trimmed name, position and stored season date
                newPlayer = Player(trimmedName, line[1], szn)

                index = searchPlayer(players, newPlayer.getName())

                if(index == -1):
                    # Add new player to sorted list
                    players = insertNewPlayer(players, newPlayer)

                else:

                    players[index].addSeason(szn)


    return players

def main():

    # players = createPlayers()

    # printPlayers(players)

    directory_path = os.getcwd()
    print("My current directory is : " + directory_path)
    folder_name = os.path.basename(directory_path)
    print("My directory name is : " + folder_name)
    csvPath = directory_path + "/csv_files"
    print(csvPath)

main()