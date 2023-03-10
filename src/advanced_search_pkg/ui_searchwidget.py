# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchwidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_searchwidget(object):
    def setupUi(self, searchwidget):
        searchwidget.setObjectName("searchwidget")
        searchwidget.resize(713, 668)
        self.gridLayout = QtWidgets.QGridLayout(searchwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(searchwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pathedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.pathedit.setMinimumSize(QtCore.QSize(0, 25))
        self.pathedit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pathedit.setObjectName("pathedit")
        self.verticalLayout.addWidget(self.pathedit)
        self.tree = QtWidgets.QTreeWidget(self.layoutWidget)
        self.tree.setHeaderHidden(True)
        self.tree.setObjectName("tree")
        self.verticalLayout.addWidget(self.tree)
        self.about = QtWidgets.QPushButton(self.layoutWidget)
        self.about.setObjectName("about")
        self.verticalLayout.addWidget(self.about)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchedit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.searchedit.setMinimumSize(QtCore.QSize(0, 25))
        self.searchedit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.searchedit.setObjectName("searchedit")
        self.horizontalLayout_2.addWidget(self.searchedit)
        self.clearsearchedit = QtWidgets.QPushButton(self.layoutWidget1)
        self.clearsearchedit.setMinimumSize(QtCore.QSize(25, 25))
        self.clearsearchedit.setMaximumSize(QtCore.QSize(25, 25))
        self.clearsearchedit.setText("")
        self.clearsearchedit.setObjectName("clearsearchedit")
        self.horizontalLayout_2.addWidget(self.clearsearchedit)
        self.statebutton = QtWidgets.QPushButton(self.layoutWidget1)
        self.statebutton.setMinimumSize(QtCore.QSize(25, 25))
        self.statebutton.setMaximumSize(QtCore.QSize(25, 25))
        self.statebutton.setText("")
        self.statebutton.setObjectName("statebutton")
        self.horizontalLayout_2.addWidget(self.statebutton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dircb = QtWidgets.QCheckBox(self.layoutWidget1)
        self.dircb.setMaximumSize(QtCore.QSize(16777215, 25))
        self.dircb.setChecked(True)
        self.dircb.setObjectName("dircb")
        self.horizontalLayout.addWidget(self.dircb)
        self.filescb = QtWidgets.QCheckBox(self.layoutWidget1)
        self.filescb.setMaximumSize(QtCore.QSize(16777215, 25))
        self.filescb.setChecked(True)
        self.filescb.setObjectName("filescb")
        self.horizontalLayout.addWidget(self.filescb)
        self.systemcb = QtWidgets.QCheckBox(self.layoutWidget1)
        self.systemcb.setObjectName("systemcb")
        self.horizontalLayout.addWidget(self.systemcb)
        self.hiddencb = QtWidgets.QCheckBox(self.layoutWidget1)
        self.hiddencb.setChecked(True)
        self.hiddencb.setObjectName("hiddencb")
        self.horizontalLayout.addWidget(self.hiddencb)
        self.recursecb = QtWidgets.QCheckBox(self.layoutWidget1)
        self.recursecb.setMaximumSize(QtCore.QSize(16777215, 25))
        self.recursecb.setChecked(True)
        self.recursecb.setObjectName("recursecb")
        self.horizontalLayout.addWidget(self.recursecb)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.resultslist = QtWidgets.QListWidget(self.layoutWidget1)
        self.resultslist.setObjectName("resultslist")
        self.verticalLayout_3.addWidget(self.resultslist)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(searchwidget)
        self.clearsearchedit.clicked.connect(self.searchedit.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(searchwidget)

    def retranslateUi(self, searchwidget):
        _translate = QtCore.QCoreApplication.translate
        searchwidget.setWindowTitle(_translate("searchwidget", "Form"))
        self.tree.headerItem().setText(0, _translate("searchwidget", "1"))
        self.about.setText(_translate("searchwidget", "About"))
        self.dircb.setText(_translate("searchwidget", "Dirs"))
        self.filescb.setText(_translate("searchwidget", "Files"))
        self.systemcb.setText(_translate("searchwidget", "System"))
        self.hiddencb.setText(_translate("searchwidget", "Hidden"))
        self.recursecb.setText(_translate("searchwidget", "Recurse"))
