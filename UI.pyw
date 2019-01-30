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
        resultCount = len(games)
        if resultCount < 1:
            messagebox.showinfo(title = "No games found", message= "No games found")
        elif firstSearch is True:
                firstSearch = False
                i = 0
                for x in games:
                    if x[3] != 1: #Check game isn't flagged as redeemed
                        uniqueID = f"Game{i}"
                        resultsTree.insert("","end", iid=uniqueID, values = [x[0], x[1], x[2]] )
                        i = i + 1
                previousResultCount = resultCount
        else: #First we must clear the list before adding new games to it
            i = 0
            loopCount = 0
            while loopCount != previousResultCount and previousResultCount > 0:
                uniqueID = f"Game{i}"
                resultsTree.delete(uniqueID)
                i = i + 1
                loopCount = loopCount + 1
            i = 0 #reset i to 0
            for x in games:
                    if x[3] != 1: #Check game isn't flagged as redeemed
                        uniqueID = f"Game{i}"
                        resultsTree.insert("","end", iid=uniqueID, values = [x[0], x[1], x[2]] )
                        i = i + 1
            previousResultCount = resultCount


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


#Results
#games = [("Game 1", "2839801732"),("Game 11", "2839801732"),("Game 10", "2839801732"),("Game 9", "2839801732"),("Game 8", "2839801732"),("Game 7", "2839801732"),("Game 6", "2839801732"),("Game 5", "2839801732"),("Game 4", "2839801732"),("Game 3", "2839801732"),("Game 2", "2839801732"),]

#for x in games:
    
   # resultsTree.insert("","end", iid=None, values = [x[0], x[1]] )
    
    

root.mainloop()