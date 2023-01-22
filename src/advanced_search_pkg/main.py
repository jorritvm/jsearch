from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from .searchwidget import *

class main(QWidget):

    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        
        #klasse-velden
        self.searchlist = list()
        
        #shortcuts
        self.newtab = QShortcut(QKeySequence("Ctrl+T"), self)
        self.closeactivetab = QShortcut(QKeySequence("Ctrl+W"), self)
        
        #ui opstarten
        self.setWindowIcon(QIcon("resources/appicon.ico"))
        self.setupUi()
        self.setupSlots()

        
    def setupUi(self):
        self.setWindowTitle("jsearch: a local file search app")
        self.resize(QSize(809,618))
        
        self.tabwidget = QTabWidget()
        self.createsearchwidget()
        
        layout = QGridLayout()
        layout.addWidget(self.tabwidget)
        self.setLayout(layout)

        
    def createsearchwidget(self,parent=None):
        x = searchwidget(parent)
        self.searchlist.append(x)
        size = len(self.searchlist)
        self.tabwidget.addTab(x, "SEARCH "+str(size))
        self.tabwidget.setCurrentIndex(size-1)     
        
    def deletesearchwidget(self):
        index = self.tabwidget.currentIndex()
        self.tabwidget.removeTab(index)
        self.searchlist.pop(index)
        
        if len(self.searchlist) == 0:
            self.createsearchwidget()

    def setupSlots(self):
        self.newtab.activated.connect(self.createsearchwidget)
        self.closeactivetab.activated.connect(self.deletesearchwidget)