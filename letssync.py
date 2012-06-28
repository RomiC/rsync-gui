#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'letssync.ui'
#
# Created: Sun Jun 24 22:56:45 2012
#	  by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!
import sys, os
from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(300, 270)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.saveButton = QtGui.QPushButton(self.centralwidget)
		self.saveButton.setGeometry(QtCore.QRect(120, 235, 71, 32))
		self.saveButton.setObjectName(_fromUtf8("saveButton"))
		self.lineEdit = QtGui.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(130, 10, 131, 23))
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
		self.toolButton = QtGui.QToolButton(self.centralwidget)
		self.toolButton.setGeometry(QtCore.QRect(263, 10, 27, 23))
		self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
		self.toolButton.setAutoRaise(False)
		self.toolButton.setArrowType(QtCore.Qt.NoArrow)
		self.toolButton.setObjectName(_fromUtf8("toolButton"))
		self.label_2 = QtGui.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(10, 13, 101, 16))
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.scrollArea = QtGui.QScrollArea(self.centralwidget)
		self.scrollArea.setGeometry(QtCore.QRect(10, 105, 281, 121))
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
		self.scrollAreaWidgetContents = QtGui.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 119))
		self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
		self.lineEdit_2.setGeometry(QtCore.QRect(130, 40, 161, 23))
		self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
		self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
		self.lineEdit_3.setGeometry(QtCore.QRect(130, 70, 161, 23))
		self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
		self.label_3 = QtGui.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(10, 42, 62, 16))
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.label_4 = QtGui.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(10, 72, 62, 16))
		self.label_4.setObjectName(_fromUtf8("label_4"))
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		self.connectSignals()
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "TDS dropbox", None, QtGui.QApplication.UnicodeUTF8))
		self.saveButton.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
		self.toolButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Folder to sync", None, QtGui.QApplication.UnicodeUTF8))
		self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Login", None, QtGui.QApplication.UnicodeUTF8))
		self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Password", None, QtGui.QApplication.UnicodeUTF8))

	def connectSignals(self):
		QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL("clicked()"), self.selectFolder)
		QtCore.QObject.connect(self.centralwidget, QtCore.SIGNAL("folderIsSet(PyQt_PyObject)"), self.setFolder)

	def selectFolder(self):
		folder = QtGui.QFileDialog.getExistingDirectory(self.centralwidget, "Choose folder to sync", os.getenv("HOME"))
		QtCore.QObject.emit(self.centralwidget, QtCore.SIGNAL("folderIsSet(PyQt_PyObject)"), folder)

	def setFolder(self, folder):
		self.lineEdit.setText(folder)

	def validateData(self, folder):
		print "validating..."

app = QtGui.QApplication(sys.argv)
w = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(w)
w.show()
app.exec_()
