from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import GameKeys

root = Tk()
firstSearch = True
previousResultCount = 0
def SearchBegin():
    global firstSearch
    global previousResultCount
    searchString = searchbox.get()
    checkInput = len(searchString)
    if checkInput < 1:
        messagebox.showerror(title = "No Input", message = "Please put something into the search box")
    else:
        games = GameKeys.gameSearch(searchString)
        resultCount = len(games) #Check how many results are returned
        if resultCount < 1: #If there is less than one result create an error dialog
            messagebox.showinfo(title = "No games found", message= "No games found")
            previousResultCount = resultCount
        elif firstSearch is True: #if this is the first search since boot (gloabl variable)
                firstSearch = False
                i = 0
                for x in games:
                    if x[3] != 1: #Check game isn't flagged as redeemed
                        uniqueID = f"Game{i}"
                        resultsTree.insert("","end", iid=uniqueID, values = [x[0], x[1], x[2]] )
                        i = i + 1
                    elif x[3] != 0: #If games were found but were all flagged as redeemed
                        previousResultCount = 0
                previousResultCount = resultCount
        else: #First we must clear the list before adding new games to it
            currentNoResults = len(resultsTree.get_children())
            i = 0
            while currentNoResults > 0:
                uniquedelID = f"Game{i}"
                resultsTree.delete(uniquedelID)
                i = i + 1
                currentNoResults = currentNoResults - 1
            if i > 0: 
                i = 0 #reset i to 0
            for x in games:
                    if x[3] != 1: #Check game isn't flagged as redeemed
                        uniqueID = f"Game{i}"
                        resultsTree.insert("","end", iid=uniqueID, values = [x[0], x[1], x[2]] )
                        i = i + 1
                    elif x[3] != 0 and resultCount == 1 and previousResultCount < 1: #If games were found but were all flagged as redeemed AND previous search also had no results
                        resultCount = 0
                        messagebox.showinfo(title = "No games found", message= "No unredeemed games found")
                    elif x[3] != 0 and resultCount > 1:
                        resultCount = resultCount - 1
            previousResultCount = resultCount

#Double click copy to clipboard and set redeemed
def CopyKey(a):
    selection = resultsTree.focus()
    print (resultsTree.item(selection, "values"))
    gameInfo = (resultsTree.item(selection, "values"))
    key = gameInfo[1]
    print (key)
    resultsTree.clipboard_append(gameInfo)
    GameKeys.setRedeemed(gameInfo[0], key)

## Add game from entry in form

def addGameBegin ():
    gName = gameName.get()
    gKey = gameKey.get()
    gPlatform = platformVar.get()
    GameKeys.addGame(gName, gKey, gPlatform)


## Add games from excel file
def LoadKeysFile ():
    print("add keys from file")


#Menus
topmenu = Menu(tearoff = 0, title = "File")


#Tabs
notebook = ttk.Notebook(root)
notebook.pack()



#Create frames to add to notebook
searchFrame = ttk.Frame(notebook, padding = 5)
addFrame = ttk.Frame(notebook, padding = 5)
notebook.add(searchFrame, text = "Search")
notebook.add(addFrame, text = "Add Game")

#Search Frame
searchbox = ttk.Entry(searchFrame, width = 30)
searchbox.grid(column = 0, row = 0, columnspan = 3, sticky = "ew")
searchButton = ttk.Button(searchFrame, text = "Search", command = SearchBegin)
searchButton.grid(column = 3, row = 0, columnspan = 2)

#Tree menu for results of search
resultsTree = ttk.Treeview(searchFrame, columns= ("Game", "Key", "Platform"))
resultsTree.grid(column = 0, row = 1, columnspan = 4)
resultsTree.column("#0", width = 20, stretch = False)
resultsTree.column("Game", stretch = True)
resultsTree.column("Key", stretch = True)
resultsTree.column("Platform", stretch = True)
resultsTree.heading("Game", text = "Game")
resultsTree.heading("Key", text = "Key")
resultsTree.heading("Platform", text = "Platform")
#Search scroll bar
searchScroll = ttk.Scrollbar(searchFrame, orient = VERTICAL, command = resultsTree.yview)
searchScroll.grid(column = 4, row = 1, rowspan = 3, sticky = "ns")
resultsTree.config(yscrollcommand = searchScroll.set)

### Add game UI

##Platforms
platformVar = StringVar(root) ##Tk Variable
Platforms = {"Steam", "UPlay", "Origin"} #Platforms 
platformVar.set ("Steam")

##Add Game Frame
gameNameLabel = ttk.Label(addFrame, text = "Game Name:")
gameNameLabel.grid(column = 0, row = 0, padx = "2", pady = "5")
gameName = ttk.Entry(addFrame, width = 60)
gameName.grid(column = 1, row = 0, columnspan = 2, sticky = "ew", padx = "10", pady = "5")
gameKeyLabel = ttk.Label(addFrame, text = "Key:")
gameKeyLabel.grid(column = 0, row = 2, padx = "2", pady = "5")
gameKey = ttk.Entry(addFrame, width = 60)
gameKey.grid(column = 1, row = 2, columnspan = 2, stick = "ew", padx = "10", pady = "5" )
gamePlatformLabel = ttk.Label(addFrame, text = "Platform:")
gamePlatformLabel.grid(column = 0, row = 3, padx = "2", pady = "5")
gamePlatform = OptionMenu(addFrame, platformVar, *Platforms)
gamePlatform.grid(column = 1, row = 3, columnspan = "2", padx = "10", pady = "5", sticky = "ew")
gameaddButton = ttk.Button(addFrame, text = "Add Game", command = addGameBegin)
gameaddButton.grid(column = 1, row = 4, sticky = "ew")
addFromFileButton = ttk.Button(addFrame, text = "Add from file", command = LoadKeysFile)
addFromFileButton.grid(column = 2, row = 4, sticky = "ew")


#Mouse interactions

resultsTree.bind("<Double-Button-1>", CopyKey) #On double click of key

#Results
#games = [("Game 1", "2839801732"),("Game 11", "2839801732"),("Game 10", "2839801732"),("Game 9", "2839801732"),("Game 8", "2839801732"),("Game 7", "2839801732"),("Game 6", "2839801732"),("Game 5", "2839801732"),("Game 4", "2839801732"),("Game 3", "2839801732"),("Game 2", "2839801732"),]

#for x in games:
    
   # resultsTree.insert("","end", iid=None, values = [x[0], x[1]] )
    
    

root.mainloop()