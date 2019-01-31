import sqlite3
from sqlite3 import Error
import sys
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
    sql = "INSERT INTO Games (Name, Key, Platform, Redeemed) values (?,?,?,0)"
    # Excute the addition then commit
    c.execute(sql, values)
    conn.commit()

def setRedeemed(Name, Key):
    #Connect
    conn = createConnection("gameKeys.db")
    c = conn.cursor()
    sql = '''UPDATE Games 
    SET Redeemed = ? 
    WHERE Key = ?'''
    redeemed = 1
    values = (redeemed, Key)
    print(values)
    c.execute(sql, values)
    conn.commit()
    


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


def gameSearch(Name):
    #searching = True
    #while searching is True:
     conn = createConnection("gameKeys.db")
     c = conn.cursor()
     c.execute('''SELECT Name, Key, Platform, Redeemed FROM Games WHERE Name LIKE ? COLLATE NOCASE''', ('%'+Name+'%',))
     all_rows = c.fetchall()
     resultCount = len(all_rows) #check length of all_rows
     if resultCount < 1: #If no games are found
         return all_rows
     else:
         return all_rows


# CURRENT NOT IN USE search the database for input
def searchDB(dataType, userInput):
    if dataType == "Name":
        return None


# Used to chose/change platform of game when adding games
# In the future this should probably allow for the addition of extra platforms
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


# Menu
def menu():
    exit = False
    while exit is not True:
        print("What do you want to do?\n\n")
        print("1. Add a game\n")
        print("2. Search for a game\n")
        print("3. (Re)Create Database WARNING: This will likely delete all data\n")
        print("4. Exit")

        userIn = input()
        if userIn == "1":
            addGame()
        if userIn == "2":
            print("What game are you looking for?")
            GameName = str(input())
            GameName = GameName.lower()
            gameSearch(GameName)
        if userIn == "3":
            print("This is likely to delete all data do you wish to continue? y/n\n")
            confirm = input()
            if confirm == "y":
                CreateGamesDB.main()
        if userIn == "4":
            print("Thanks for playing!")
            exit = True
        else:
            print("Invalid entry, try again")
    else:
        print("Goodbye!")


def main():
   menu()

if __name__ == '__main__': main()
