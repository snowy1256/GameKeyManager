import sqlite3
from sqlite3 import Error
import CreateGamesDB
# ----- #
# ---- Database Interactions ---- #


# Creates connection to DB
def createConnection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None


# Insert Game into database
def insertGameData(values):
    # Name, Key and Platform are defined in addGame
    # conn is connection to db defined in createConnection
    # Connect to the db
    conn = createConnection("gameKeys.db")
    # Simplify cursor to a single letter because why not
    c = conn.cursor()
    # Tell sqlite that we want to insert the three values into the DB
    sql = "insert into Games (Name, Key, Platform) values (?,?,?)"
    # Excute the addition then commit
    c.execute(sql, values)
    conn.commit


# ---- User Interactions ---- #
# Defining game to add to database
def addGame():
    UserInput = True
    UserConf = False
    while UserInput is True:
        print("Please enter the games name:\n")
        GameName = str(input())
        print("\n\nPlease enter the game key:\n")
        GameKey = str(input())
        GamePlatform = choosePlatform()
        while UserConf is not True:
            print("Your game is called: ", GameName, "\n")
            print("They key you entered was: ", GameKey, "\n")
            print("The Platform you chose for this game was:", GamePlatform, "\n")
            print("Is this all correct? y/n")
            UserConf = str(input())
            if UserConf == "y":
                print("Great, adding to the database!\n")
                UserInput = False
                UserConf = True
                gameInfo = (GameName, GameKey, GamePlatform)
                insertGameData(gameInfo)
                break
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
                    GamePlatform = choosePlatform()
                    break
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
