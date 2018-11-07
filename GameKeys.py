import sqlite3
from sqlite3 import Error
import CreateGamesDB
# ----- #


# Creates connection to DB
def createConnection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None


# Add a game to the database
def addGame():
    UserInput = True
    GamePlatform = 0
    UserConf = False
    while UserInput is True:
        print("Please enter the games name:\n")
        GameName = str(input())
        print("\n\nPlease enter the game key:\n")
        GameKey = str(input())
        while GamePlatform == 0:
            choosePlatform()
        while UserConf is not True:
            print("Your game is called: ", GameName, "\n")
            print("They key you entered was: ", GameKey, "\n")
            print("The Platform you chose for this game was:", GamePlatform, "\n")
            print("Is this all correct? y/n")
            UserConf = str(input())
            if UserConf == "y":
                print("Great, adding to the database!\n")
                UserInput = False
                # add code to do that
            else:
                print("What do you need to change?\n")
                print("1. Game Name\n2. Game Key\n3. Platform\n4. Everything\n")
                changeInput = int(input())
                if changeInput == 1:
                    print("\nInsert new game name:\n")
                    GameName = str(input())
                elif changeInput == 2:
                    print("Insert new key:\n")
                    GameKey = str(input())
                elif changeInput == 3:
                    choosePlatform()
                elif changeInput == 4:
                    UserConf = False
                    GamePlatform = False
                    UserInput = True
                    break


def choosePlatform():
    print("Please select platform:\n")
    print("1. Steam\n2. Origin\n3. UPlay")
    GamePlatform = int(input())
    if GamePlatform == 1:
        GamePlatform = "Steam"
    elif GamePlatform == 2:
        GamePlatform = "Origin"
    elif GamePlatform == 3:
        GamePlatform = "UPlay"
    else:
        print("\nIncorrect entry")
    return GamePlatform


# search the database for input
def searchDB(dataType, userInput):
    if dataType == "Name":
        return None


# Menu
def menu():
    print("What do you want to do?\n\n")
    print("1. Add a game\n")
    print("2. Search for a game\n")
    print("3. (Re)Create Database WARNING: This will likely delete all data\n")

    userIn = int(input())
    if userIn == 1:
        addGame()
    if userIn == 3:
        print("This is likely to delete all data do you wish to continue? y/n\n")
        confirm = input()
        if confirm == "y":
            CreateGamesDB.main()


if __name__ == '__main__':
    menu()
