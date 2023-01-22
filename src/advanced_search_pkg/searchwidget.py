from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from .ui_searchwidget import *
from .items import *

class searchwidget(QWidget, Ui_searchwidget):
    
    def __init__(self, parent=None):
        super(searchwidget, self).__init__(parent)
        
        self.setupUi(self)
        self.statebutton.setIcon(QIcon("resources/done.png"))
        self.clearsearchedit.setIcon(QIcon("resources/clear.ico"))
        
        self.searchbot = searchbot(self)
        
        self.setupSlots()
        
        self.top = None
        self.buildbrowser()
        self.aboutlabel = QLabel("<h2>A local file search app by jvm</h2>Shortcuts:<br />ctrl+t: new tab<br />ctrl+w: close current tab")

           
    def setupSlots(self):
        self.tree.itemExpanded.connect(lambda x: self.updatebrowser(x))
        self.tree.itemActivated.connect(lambda x, y: self.updatepath(x, y))
        self.tree.itemClicked.connect(lambda x, y: self.updatepath(x, y))
        self.pathedit.returnPressed.connect(self.browsertofolder)
        self.searchedit.returnPressed.connect(self.preparesearch)
        self.searchbot.foundone.connect(lambda x: self.updateresults(x))
        self.searchbot.finished.connect(self.finishsearch)
        self.statebutton.clicked.connect(self.stopnow)
        self.about.clicked.connect(self.showabout)

    def getroot(self):
        browser = QDir("/")
        alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        root = list()
        for letter in alfabet:
            path = letter + ":"
            if browser.cd(path) == 1:
                root.append(path)
        return root

    def buildbrowser(self):
        listing = self.getroot()
        thiscomp = treeitem(self.tree)
        thiscomp.settext("My Computer")
        thiscomp.seticon("resources/desktop.ico")
        thiscomp.setpath("my_computer")
        thiscomp.toggle_expanded()
        self.tree.setCurrentItem(thiscomp)
        self.pathedit.setText("my_computer")
        self.top = thiscomp
        
        for item in listing:
            x = treeitem(thiscomp)
            x.settext(item)
            x.seticon(QIcon("resources/drive.jpg"))
            x.setpath(item)
            x.fetchchildren()
    
    def updatebrowser(self, item):
        i = 0
        while i < item.childCount():
            item.child(i).fetchchildren()
            i += 1
    
    def browsertofolder(self):
        path = self.pathedit.text()
        path = path.replace("\\", "/")
        pathpieces = path.split("/")
        
        parent = self.top
        for piece in pathpieces:
            if str(piece).strip() == "":
                break
            x = self.findpiece(piece, parent)
            if x == None:
                self.pathedit.setText("PATH NOT FOUND")
                break
            else:
                self.tree.setCurrentItem(x)
                parent = x
    
    
    def findpiece(self, text, parent):
        i = 0
        while i < parent.childCount():
            if str(parent.child(i).gettext()).lower() == str(text).lower():
                return parent.child(i)
            i += 1
        return None
          
    def updatepath(self, item, index):
        self.pathedit.setText(item.path)
    
    def preparesearch(self):
        self.resultslist.clear()
        
        flags = None
        x=0
        if self.dircb.isChecked():
            x += 1
            if flags:
                flags = flags|QDir.Dirs
            else:
                flags = QDir.Dirs
        if self.filescb.isChecked():
            x += 1
            if flags:
                flags = flags|QDir.Files
            else:
                flags = QDir.Files
        if self.hiddencb.isChecked():
            x += 1
            if flags:
                flags = flags|QDir.Hidden
            else:
                flags = QDir.Hidden
        if self.systemcb.isChecked():
            x += 1
            if flags:
                flags = flags|QDir.System
            else:
                flags = QDir.System
        if x == 0:      
            self.searchedit.setText("SELECT AT LEAST ONE CHECKBOX")
        else:
            path = self.pathedit.text()
            if path == "my_computer":
                self.searchedit.setText("CAN'T SEARCH IN 'MY COMPUTER' - SELECT DRIVE")
            else:
                keywords = self.searchedit.text().split(" ")
                self.startsearch(keywords, path, flags)
        
    def startsearch(self, keywords, path, flags):
        self.statebutton.setIcon(QIcon("resources/searching.png"))
        self.searchbot.setupbot(self.resultslist, self.recursecb, keywords, path, flags)
        self.searchbot.wait()
        self.searchbot.start()
    
    def updateresults(self, abspath):
        entry = QFileInfo(abspath)
        a = resultitem(entry, self.resultslist)
        
    def stopnow(self):
        self.searchbot.stop = True
    
    def finishsearch(self):
        self.statebutton.setIcon(QIcon("resources/done.png"))

    def showabout(self):
        self.aboutlabel.show()

        
class searchbot(QThread):
    # create my custom signals
    foundone = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, parent=None):
        super(searchbot, self).__init__(parent)
        self.stop = False

    def setupbot(self, resultslist, recursecb, keywords, path, flags):
        self.resultslist = resultslist
        self.recursecb = recursecb
        self.keywords = keywords
        self.path = path
        self.flags = flags
        self.stop = False
      
    def startsearch(self, keywords, path, flags):
        if self.stop:
            return False
        
        dir = QDir(path)
        listing = dir.entryInfoList(flags, QDir.DirsFirst)
    
        for entry in listing:
            e = entry.fileName().lower()
            x = 0
            for key in keywords:
                k = key.lower()
                if k in e:
                    x +=1
            if x == len(keywords):
                #all keywords found
                if entry.fileName() != "." and entry.fileName() != "..":
                    stringtoreturn = entry.absoluteFilePath()
                    self.foundone.emit(stringtoreturn)
        
        for entry in listing:
            if entry.fileName() != "." and entry.fileName() != "..":
                if entry.isDir() and self.recursecb.isChecked():
                    self.startsearch(keywords, entry.filePath(), flags)
        
    def run(self):
        self.startsearch(self.keywords, self.path, self.flags)
        self.finished.emit()
        