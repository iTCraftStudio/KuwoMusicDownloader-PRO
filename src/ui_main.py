# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(410, 272)
        self.actionGo_to_kuwo_cn = QAction(MainWindow)
        self.actionGo_to_kuwo_cn.setObjectName(u"actionGo_to_kuwo_cn")
        self.actionAbout_Us = QAction(MainWindow)
        self.actionAbout_Us.setObjectName(u"actionAbout_Us")
        self.actionDocs = QAction(MainWindow)
        self.actionDocs.setObjectName(u"actionDocs")
        self.actionGo_to_itcraft_tk = QAction(MainWindow)
        self.actionGo_to_itcraft_tk.setObjectName(u"actionGo_to_itcraft_tk")
        self.actionChick_Update = QAction(MainWindow)
        self.actionChick_Update.setObjectName(u"actionChick_Update")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.urlEdit = QLineEdit(self.groupBox)
        self.urlEdit.setObjectName(u"urlEdit")

        self.horizontalLayout.addWidget(self.urlEdit)

        self.sendButton = QPushButton(self.groupBox)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.sendButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.urlView = QLabel(self.groupBox)
        self.urlView.setObjectName(u"urlView")

        self.verticalLayout_2.addWidget(self.urlView)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.musicName = QLabel(self.groupBox)
        self.musicName.setObjectName(u"musicName")

        self.gridLayout.addWidget(self.musicName, 0, 1, 1, 1)

        self.musicId = QLabel(self.groupBox)
        self.musicId.setObjectName(u"musicId")

        self.gridLayout.addWidget(self.musicId, 0, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.savePath = QLineEdit(self.groupBox)
        self.savePath.setObjectName(u"savePath")
        self.savePath.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.savePath)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.progressBar = QProgressBar(self.groupBox_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.progressBar)

        self.startDown = QPushButton(self.groupBox_2)
        self.startDown.setObjectName(u"startDown")
        self.startDown.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.startDown)


        self.verticalLayout.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 410, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionGo_to_kuwo_cn)
        self.menu.addSeparator()
        self.menu.addAction(self.actionAbout_Us)
        self.menu.addAction(self.actionDocs)
        self.menu.addSeparator()
        self.menu.addAction(self.actionGo_to_itcraft_tk)
        self.menu.addAction(self.actionChick_Update)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Kuwo Music Downloader Pro 2.0", None))
        self.actionGo_to_kuwo_cn.setText(QCoreApplication.translate("MainWindow", u"Go to kuwo.cn", None))
        self.actionAbout_Us.setText(QCoreApplication.translate("MainWindow", u"About Us", None))
        self.actionDocs.setText(QCoreApplication.translate("MainWindow", u"Docs", None))
        self.actionGo_to_itcraft_tk.setText(QCoreApplication.translate("MainWindow", u"Go to home", None))
        self.actionChick_Update.setText(QCoreApplication.translate("MainWindow", u"Chick Update", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u4e50\u94fe\u63a5\uff1a", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))
        self.urlView.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h2 align=\"center\" style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700;\">\u6b4c\u66f2\u4fe1\u606f</span></h2></body></html>", None))
        self.musicName.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u66f2\u540d\uff1a\u672a\u77e5", None))
        self.musicId.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u4e50ID\uff1a\u672a\u77e5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bd5\u542c\u94fe\u63a5\uff1a\u672a\u77e5", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u51c6\u5907\u72b6\u6001\uff1a<span style=\"color:orange\">\u672a\u5f00\u59cb</span>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4f4d\u7f6e\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u8fdb\u5ea6\uff1a", None))
        self.startDown.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u4e0b\u8f7d", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

