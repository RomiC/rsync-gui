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
from datetime import datetime
from subprocess import Popen, PIPE

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
		self.buttonSave = QtGui.QPushButton(self.centralwidget)
		self.buttonSave.setGeometry(QtCore.QRect(120, 235, 71, 32))
		self.buttonSave.setObjectName(_fromUtf8("buttonSave"))
		self.inputFolder = QtGui.QLineEdit(self.centralwidget)
		self.inputFolder.setGeometry(QtCore.QRect(130, 10, 131, 23))
		self.inputFolder.setObjectName(_fromUtf8("inputFolder"))
		self.buttonSelectFolder = QtGui.QToolButton(self.centralwidget)
		self.buttonSelectFolder.setGeometry(QtCore.QRect(263, 10, 27, 23))
		self.buttonSelectFolder.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
		self.buttonSelectFolder.setAutoRaise(False)
		self.buttonSelectFolder.setArrowType(QtCore.Qt.NoArrow)
		self.buttonSelectFolder.setObjectName(_fromUtf8("buttonSelectFolder"))
		self.labelFolder = QtGui.QLabel(self.centralwidget)
		self.labelFolder.setGeometry(QtCore.QRect(10, 13, 101, 16))
		self.labelFolder.setObjectName(_fromUtf8("labelFolder"))
		self.inputLogin = QtGui.QLineEdit(self.centralwidget)
		self.inputLogin.setGeometry(QtCore.QRect(130, 40, 161, 23))
		self.inputLogin.setObjectName(_fromUtf8("inputLogin"))
		self.inputPassword = QtGui.QLineEdit(self.centralwidget)
		self.inputPassword.setGeometry(QtCore.QRect(130, 70, 161, 23))
		self.inputPassword.setObjectName(_fromUtf8("inputPassword"))
		self.labelLogin = QtGui.QLabel(self.centralwidget)
		self.labelLogin.setGeometry(QtCore.QRect(10, 42, 62, 16))
		self.labelLogin.setObjectName(_fromUtf8("labelLogin"))
		self.labelPassword = QtGui.QLabel(self.centralwidget)
		self.labelPassword.setGeometry(QtCore.QRect(10, 72, 62, 16))
		self.labelPassword.setObjectName(_fromUtf8("labelPassword"))
		self.output = QtGui.QPlainTextEdit(self.centralwidget)
		self.output.setEnabled(True)
		self.output.setGeometry(QtCore.QRect(10, 100, 281, 131))
		self.output.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
		self.output.setFrameShape(QtGui.QFrame.StyledPanel)
		self.output.setReadOnly(True)
		self.output.setObjectName(_fromUtf8("output"))
		font = QtGui.QApplication.font()
		font.setPointSize(11)
		self.output.setFont(font)
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		self.connectSignals()
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "TDS Dropbox setup", None, QtGui.QApplication.UnicodeUTF8))
		self.buttonSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
		self.buttonSelectFolder.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
		self.labelFolder.setText(QtGui.QApplication.translate("MainWindow", "Folder to sync", None, QtGui.QApplication.UnicodeUTF8))
		self.labelLogin.setText(QtGui.QApplication.translate("MainWindow", "Login", None, QtGui.QApplication.UnicodeUTF8))
		self.labelPassword.setText(QtGui.QApplication.translate("MainWindow", "Password", None, QtGui.QApplication.UnicodeUTF8))

	def connectSignals(self):
		QtCore.QObject.connect(self.buttonSelectFolder, QtCore.SIGNAL("clicked()"), self.selectFolder)
		QtCore.QObject.connect(self.centralwidget, QtCore.SIGNAL("folderIsSet(PyQt_PyObject)"), self.setFolder)
		QtCore.QObject.connect(self.buttonSave, QtCore.SIGNAL("clicked()"), self.validateData)
		

	def selectFolder(self):
		folder = QtGui.QFileDialog.getExistingDirectory(self.centralwidget, "Choose folder to sync", os.getenv("HOME"))
		QtCore.QObject.emit(self.centralwidget, QtCore.SIGNAL("folderIsSet(PyQt_PyObject)"), folder)

	def setFolder(self, folder):
		self.inputFolder.setText(folder)

	def validateData(self):
		validate = True
		if (len(self.inputFolder.text()) == 0):
			self.error("You haven't choose the dir to sync!")
			validate = False
		if (len(self.inputLogin.text()) == 0):
			self.error("You havent enter the login!")
			validate = False
		if (len(self.inputPassword.text()) == 0):
			self.error("You haven't enter the password!")
			validate = False
		if (validate):
			self.setupSync({"folder": self.inputFolder.text(), "login": self.inputLogin.text(), "password": self.inputPassword.text()})

	def setupSync(self, data):
		self.out("setup start")
		self.out("you will be prompted when proccess will have been finished")
		#p = Popen(["/bin/sh", "./lettsync.sh", "-u", data["login"], "-p", data["password"], data["folder"]], stdout=PIPE)
		print data
		p = Popen(["./letssync.sh", "-u%(login)s" % data, "-p%(password)s" % data, "%(folder)s" % data])
		if (p.wait() != 0):
			self.error("an error occuring during setup!")
		else:
			self.out("setup complete!")	

	def error(self, message):
		self.out("ERROR: {}".format(message))

	def out(self, message):
		self.output.appendPlainText("{0} :: {1}".format(datetime.now().strftime("%H:%M"), message))

app = QtGui.QApplication(sys.argv)
w = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(w)
w.show()
app.exec_()
