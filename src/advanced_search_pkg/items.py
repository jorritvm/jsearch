from PyQt4.QtGui import *
from PyQt4.QtCore import *

class treeitem(QTreeWidgetItem):
    def __init__(self, parent = None):
        super(treeitem, self).__init__(parent);
        #QTreeWidgetItem.__init__(parent);
        self.parent = parent
    
    def seticon(self, iconlink):
        self.setIcon(0,QIcon(iconlink))
        
    def toggle_expanded(self):
        if self.isExpanded():
            self.setExpanded(False)
        else:
            self.setExpanded(True)
            
    def settext(self, x):
        self.setText(0,x)
        
    def gettext(self):
        return self.text(0)
        
    def setpath(self, path):
        self.path = path
    
    def fetchchildren(self):
        x = QDir(self.path)
        listing = x.entryInfoList(QDir.Dirs)
        for entry in listing:
            if (entry.fileName() == ".") or (entry.fileName() == ".." ):
                continue 
            child = treeitem(self)
            child.settext(QString(entry.fileName()))
            child.setpath(entry.absoluteFilePath())
            if entry.isDir():
                child.seticon(QIcon("folder.jpg"))
            else:
                child.seticon(QIcon("file.png"))
                
                
class resultitem(QListWidgetItem):
    def __init__(self, entry, parent = None):
        super(resultitem, self).__init__(parent);
        #QTreeWidgetItem.__init__(parent);
        self.parent = parent
        self.fileinfo = entry
        
        if self.fileinfo.isDir():
            self.setIcon(QIcon("folder.jpg"))
        else:
            self.setIcon(QIcon("file.png"))
            
        self.setText(self.fileinfo.fileName())