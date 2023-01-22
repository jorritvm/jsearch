'''
############################################################################
#    Copyright (C) 2009 by Jorrit Vander Mynsbrugge                        #
#    jorrit.vm@telenet.be                                                  #
#                                                                          #
#    This program is free software; you can redistribute it and#or modify  #
#    it under the terms of the GNU General Public License as published by  #
#    the Free Software Foundation; either version 2 of the License, or     #
#    (at your option) any later version.                                   #
#                                                                          #
#    This program is distributed in the hope that it will be useful,       #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#    GNU General Public License for more details.                          #
#                                                                          #
#    You should have received a copy of the GNU General Public License     #
#    along with this program; if not, write to the                         #
#    Free Software Foundation, Inc.,                                       #
#    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             #
############################################################################
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from searchwidget import *

class main(QWidget):

    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        
        #klasse-velden
        self.searchlist = list()
        
        #shortcuts
        self.newtab = QShortcut(QKeySequence("Ctrl+T"),self)
        self.closeactivetab = QShortcut(QKeySequence("Ctrl+W"),self)
        
        #ui opstarten
        self.setWindowIcon(QIcon("appicon.ico"))
        self.setupUi()
        self.setupSlots()
        
        #self.createsearchwidget()
        
        
    def setupUi(self):
        self.setWindowTitle("Advanced Search Engine by Jorrit Vander Mynsbrugge")
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
        QObject.connect(self.newtab,SIGNAL("activated()"),self.createsearchwidget)
        QObject.connect(self.closeactivetab,SIGNAL("activated()"),self.deletesearchwidget)
    
    def test(self):
        print "klqsdfklqmdfj"
    

    