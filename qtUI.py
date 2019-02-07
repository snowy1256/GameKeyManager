from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import GameKeys

## --- UI Creation -- ##

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 342)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 751, 291))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.searchTab = QtWidgets.QWidget()
        self.searchTab.setObjectName("searchTab")
        self.layoutWidget = QtWidgets.QWidget(self.searchTab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 721, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.searchBoxInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.searchBoxInput.setObjectName("searchBoxInput")
        self.gridLayout.addWidget(self.searchBoxInput, 0, 0, 1, 1)
        self.searchScroll = QtWidgets.QScrollBar(self.layoutWidget)
        self.searchScroll.setOrientation(QtCore.Qt.Vertical)
        self.searchScroll.setObjectName("searchScroll")
        self.gridLayout.addWidget(self.searchScroll, 1, 2, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.layoutWidget)
        self.searchButton.setTabletTracking(False)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 0, 1, 1, 1)
        self.searchTable = QtWidgets.QTableWidget(self.layoutWidget)
        self.searchTable.setObjectName("searchTable")
        self.searchTable.setColumnCount(4)
        self.searchTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.searchTable, 1, 0, 1, 2)
        
        self.tabWidget.addTab(self.searchTab, "")
        self.addGameTab = QtWidgets.QWidget()
        self.addGameTab.setObjectName("addGameTab")
        self.layoutWidget1 = QtWidgets.QWidget(self.addGameTab)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 711, 231))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gameInput = QtWidgets.QLineEdit(self.layoutWidget1)
        self.gameInput.setObjectName("gameInput")
        self.gridLayout_2.addWidget(self.gameInput, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.keyInput = QtWidgets.QLineEdit(self.layoutWidget1)
        self.keyInput.setText("")
        self.keyInput.setObjectName("keyInput")
        self.gridLayout_2.addWidget(self.keyInput, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 5, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 5, 1, 1, 1)
        self.tabWidget.addTab(self.addGameTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 26))
        self.menubar.setObjectName("menubar")
        self.menuGame_Key_Manager = QtWidgets.QMenu(self.menubar)
        self.menuGame_Key_Manager.setObjectName("menuGame_Key_Manager")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuGame_Key_Manager.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Game Key Manager"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        item = self.searchTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Game"))
        item = self.searchTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Key"))
        item = self.searchTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Platform"))
        item = self.searchTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Redeemed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchTab), _translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Game Name:"))
        self.label_2.setText(_translate("MainWindow", "Key:"))
        self.label_3.setText(_translate("MainWindow", "Platform:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Steam"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Origin"))
        self.comboBox.setItemText(2, _translate("MainWindow", "UPlay"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Other"))
        self.pushButton.setText(_translate("MainWindow", "Add Game"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addGameTab), _translate("MainWindow", "Add Game"))
        self.menuGame_Key_Manager.setTitle(_translate("MainWindow", "File"))


firstSearch = True

## Search Box
def searchBegin():
    global firstSearch
    searchString = ui.searchBoxInput.text()
    checkinput = len(searchString)
    if checkinput < 1:
        nogamebox = QtWidgets.QMessageBox()
        nogamebox.setText("Please put something into the searchbox")
        nogamebox.exec()
    else:
        games = GameKeys.gameSearch(searchString)
        resultCount = len(games) #Check how many results are returned
        if resultCount < 1: 
            nogamebox.setText("No game found")
            nogamebox.exec()
        elif firstSearch is True:
            firstSearch = False
            i = 0
            rowCount = resultCount
            currentRow = -1
            for x in games:
                if x[3] != 1: #check game isn't flagged as redeemed
                    currentRow = currentRow + 1
                    rowCount = currentRow + 1
                    ui.searchTable.setRowCount(rowCount) #Create the required number of rows
                    ui.searchTable.setItem(currentRow, 0, QTableWidgetItem(x[0]))
                    ui.searchTable.setItem(currentRow, 1, QTableWidgetItem(x[1]))
                    ui.searchTable.setItem(currentRow, 2, QTableWidgetItem(x[2]))
                    redeemedBox = QTableWidgetItem()
                    redeemedBox.setCheckState(False)
                    ui.searchTable.setItem(currentRow, 3, redeemedBox)
                    ui.searchTable.resizeColumnsToContents()
                    



## Database search

## Program ru
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.searchButton.clicked.connect(searchBegin)
    app.exec_()
    