#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'letssync.ui'
#
# Created: Sun Jun 24 22:56:45 2012
#	  by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!
import sys, os
from PyQt4.QtCore import QRect, Qt, QMetaObject, QObject, QString, SIGNAL
from PyQt4.QtGui import QWidget, QMainWindow, QPushButton, QToolButton, QLineEdit, QLabel, QPlainTextEdit, QApplication, QCursor, QFileDialog
from datetime import datetime
from subprocess import Popen, PIPE

try:
	_fromUtf8 = QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(300, 270)
		self.centralwidget = QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.buttonSave = QPushButton(self.centralwidget)
		self.buttonSave.setGeometry(QRect(120, 235, 71, 32))
		self.buttonSave.setObjectName(_fromUtf8("buttonSave"))
		self.inputFolder = QLineEdit(self.centralwidget)
		self.inputFolder.setGeometry(QRect(130, 10, 131, 23))
		self.inputFolder.setObjectName(_fromUtf8("inputFolder"))
		self.buttonSelectFolder = QToolButton(self.centralwidget)
		self.buttonSelectFolder.setGeometry(QRect(263, 10, 27, 23))
		self.buttonSelectFolder.setToolButtonStyle(Qt.ToolButtonIconOnly)
		self.buttonSelectFolder.setAutoRaise(False)
		self.buttonSelectFolder.setArrowType(Qt.NoArrow)
		self.buttonSelectFolder.setObjectName(_fromUtf8("buttonSelectFolder"))
		self.labelFolder = QLabel(self.centralwidget)
		self.labelFolder.setGeometry(QRect(10, 13, 101, 16))
		self.labelFolder.setObjectName(_fromUtf8("labelFolder"))
		self.inputLogin = QLineEdit(self.centralwidget)
		self.inputLogin.setGeometry(QRect(130, 40, 161, 23))
		self.inputLogin.setObjectName(_fromUtf8("inputLogin"))
		self.inputPassword = QLineEdit(self.centralwidget)
		self.inputPassword.setGeometry(QRect(130, 70, 161, 23))
		self.inputPassword.setObjectName(_fromUtf8("inputPassword"))
		self.labelLogin = QLabel(self.centralwidget)
		self.labelLogin.setGeometry(QRect(10, 42, 62, 16))
		self.labelLogin.setObjectName(_fromUtf8("labelLogin"))
		self.labelPassword = QLabel(self.centralwidget)
		self.labelPassword.setGeometry(QRect(10, 72, 62, 16))
		self.labelPassword.setObjectName(_fromUtf8("labelPassword"))
		self.output = QPlainTextEdit(self.centralwidget)
		self.output.setEnabled(True)
		self.output.setGeometry(QRect(10, 100, 281, 131))
		self.output.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
		self.output.setReadOnly(True)
		self.output.setObjectName(_fromUtf8("output"))
		font = QApplication.font()
		font.setPointSize(11)
		self.output.setFont(font)
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		self.connectSignals()
		QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QApplication.translate("MainWindow", "TDS Dropbox setup", None, QApplication.UnicodeUTF8))
		self.buttonSave.setText(QApplication.translate("MainWindow", "Save", None, QApplication.UnicodeUTF8))
		self.buttonSelectFolder.setText(QApplication.translate("MainWindow", "...", None, QApplication.UnicodeUTF8))
		self.labelFolder.setText(QApplication.translate("MainWindow", "Folder to sync", None, QApplication.UnicodeUTF8))
		self.labelLogin.setText(QApplication.translate("MainWindow", "Login", None, QApplication.UnicodeUTF8))
		self.labelPassword.setText(QApplication.translate("MainWindow", "Password", None, QApplication.UnicodeUTF8))

	def connectSignals(self):
		QObject.connect(self.buttonSelectFolder, SIGNAL("clicked()"), self.selectFolder)
		QObject.connect(self.centralwidget, SIGNAL("folderIsSet(PyQt_PyObject)"), self.setFolder)
		QObject.connect(self.buttonSave, SIGNAL("clicked()"), self.validateData)
		

	def selectFolder(self):
		folder = QFileDialog.getExistingDirectory(self.centralwidget, "Choose folder to sync", os.getenv("HOME"))
		QObject.emit(self.centralwidget, SIGNAL("folderIsSet(PyQt_PyObject)"), folder)

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
			self.lockGui()
			self.out("setup start")
			self.setupSync({"folder": self.inputFolder.text(), "login": self.inputLogin.text(), "password": self.inputPassword.text()})
			self.unlockGui()

	def lockGui(self):
		self.inputFolder.setReadOnly(True)
		self.inputLogin.setReadOnly(True)
		self.inputPassword.setReadOnly(True)
		self.buttonSave.setDisabled(True)
		self.buttonSelectFolder.setDisabled(True)

	def unlockGui(self):
		self.inputFolder.setReadOnly(False)
		self.inputLogin.setReadOnly(False)
		self.inputPassword.setReadOnly(False)
		self.buttonSave.setDisabled(False)
		self.buttonSelectFolder.setDisabled(False)

	def setupSync(self, data):
		p = Popen(["./letssync.sh", "-u%(login)s" % data, "-p%(password)s" % data, "%(folder)s" % data])
		if (p.wait() != 0):
			self.error("an error occuring during setup!")
		else:
			self.out("setup complete!")

	def error(self, message):
		self.out("ERROR: {}".format(message))

	def out(self, message):
		self.output.appendPlainText("{0} :: {1}".format(datetime.now().strftime("%H:%M"), message))

app = QApplication(sys.argv)
w = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(w)
w.show()
app.exec_()
