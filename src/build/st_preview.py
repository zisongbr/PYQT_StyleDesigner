# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Lib\Layout\st_preview.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Preview(object):
    def setupUi(self, Preview):
        Preview.setObjectName("Preview")
        Preview.resize(601, 623)
        Preview.setMinimumSize(QtCore.QSize(601, 623))
        self.centralwidget = QtWidgets.QWidget(Preview)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setMinimumSize(QtCore.QSize(298, 195))
        self.tabWidget_2.setMaximumSize(QtCore.QSize(16777215, 195))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setAutoRepeat(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setCheckable(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setAutoRepeat(True)
        self.radioButton_3.setAutoExclusive(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 2, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox.setEnabled(True)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 4, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_4)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_3.addWidget(self.plainTextEdit, 2, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_10.addWidget(self.lineEdit_2, 0, 0, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(self.tab_8)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 30))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_10.addWidget(self.progressBar, 1, 0, 1, 1)
        self.dial = QtWidgets.QDial(self.tab_8)
        self.dial.setObjectName("dial")
        self.gridLayout_10.addWidget(self.dial, 1, 1, 2, 1)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.tab_8)
        self.horizontalScrollBar.setMinimumSize(QtCore.QSize(0, 30))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.gridLayout_10.addWidget(self.horizontalScrollBar, 2, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.gridLayout_7.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.Tex = QtWidgets.QWidget()
        self.Tex.setObjectName("Tex")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Tex)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toolButton = QtWidgets.QToolButton(self.Tex)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setMinimumSize(QtCore.QSize(262, 40))
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 4, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.Tex)
        self.pushButton_2.setMinimumSize(QtCore.QSize(240, 40))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.Tex)
        self.pushButton_3.setMinimumSize(QtCore.QSize(240, 40))
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.Tex)
        self.buttonBox.setMinimumSize(QtCore.QSize(240, 60))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 5, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.Tex)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setMinimumSize(QtCore.QSize(240, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.Tex)
        self.pushButton.setMinimumSize(QtCore.QSize(240, 40))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.Tex)
        self.commandLinkButton.setMinimumSize(QtCore.QSize(240, 41))
        self.commandLinkButton.setAutoDefault(False)
        self.commandLinkButton.setDefault(False)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.gridLayout_2.addWidget(self.commandLinkButton, 6, 0, 1, 1)
        self.tabWidget_3.addTab(self.Tex, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 400))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.gridLayout_11.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_5, "")
        self.gridLayout_7.addWidget(self.tabWidget_3, 1, 0, 1, 1)
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.listWidget = QtWidgets.QListWidget(self.tab_6)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout_8.addWidget(self.listWidget, 0, 0, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.tab_6)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.gridLayout_8.addWidget(self.treeWidget, 1, 0, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_2.setRowCount(6)
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.gridLayout_8.addWidget(self.tableWidget_2, 2, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.listView = QtWidgets.QListView(self.tab_7)
        self.listView.setObjectName("listView")
        self.gridLayout_9.addWidget(self.listView, 0, 0, 1, 1)
        self.treeView = QtWidgets.QTreeView(self.tab_7)
        self.treeView.setObjectName("treeView")
        self.gridLayout_9.addWidget(self.treeView, 1, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.tab_7)
        self.tableView.setObjectName("tableView")
        self.gridLayout_9.addWidget(self.tableView, 2, 0, 1, 1)
        self.columnView = QtWidgets.QColumnView(self.tab_7)
        self.columnView.setObjectName("columnView")
        self.gridLayout_9.addWidget(self.columnView, 3, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_7, "")
        self.gridLayout_7.addWidget(self.tabWidget_4, 0, 1, 2, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setMinimumSize(QtCore.QSize(561, 251))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setMinimumSize(QtCore.QSize(541, 218))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 573, 282))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.toolBox = QtWidgets.QToolBox(self.scrollAreaWidgetContents)
        self.toolBox.setMinimumSize(QtCore.QSize(140, 190))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 158, 193))
        self.page.setObjectName("page")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.progressBar_2 = QtWidgets.QProgressBar(self.page)
        self.progressBar_2.setMinimumSize(QtCore.QSize(140, 30))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout_12.addWidget(self.progressBar_2, 0, 0, 1, 1)
        self.progressBar_3 = QtWidgets.QProgressBar(self.page)
        self.progressBar_3.setMinimumSize(QtCore.QSize(140, 101))
        self.progressBar_3.setProperty("value", 63)
        self.progressBar_3.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_3.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_3.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_3.setObjectName("progressBar_3")
        self.gridLayout_12.addWidget(self.progressBar_3, 1, 0, 1, 1)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 140, 210))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")
        self.gridLayout_6.addWidget(self.toolBox, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setMinimumSize(QtCore.QSize(120, 190))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.lcdNumber = QtWidgets.QLCDNumber(self.page_3)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_17.addWidget(self.lcdNumber, 0, 0, 1, 1)
        self.progressBar_4 = QtWidgets.QProgressBar(self.page_3)
        self.progressBar_4.setMinimumSize(QtCore.QSize(0, 40))
        self.progressBar_4.setProperty("value", 61)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setObjectName("progressBar_4")
        self.gridLayout_17.addWidget(self.progressBar_4, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.page_3)
        self.line.setMinimumSize(QtCore.QSize(0, 20))
        self.line.setLineWidth(6)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_17.addWidget(self.line, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.gridLayout_6.addWidget(self.stackedWidget, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(110, 190))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_13.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame, 0, 2, 1, 1)
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setMinimumSize(QtCore.QSize(110, 190))
        self.widget.setObjectName("widget")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.widget)
        self.openGLWidget.setObjectName("openGLWidget")
        self.gridLayout_14.addWidget(self.openGLWidget, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.widget, 0, 3, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setMinimumSize(QtCore.QSize(560, 260))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_15.setContentsMargins(9, 9, -1, -1)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setMinimumSize(QtCore.QSize(260, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_15.addWidget(self.comboBox, 0, 0, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox_2)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_15.addWidget(self.calendarWidget, 0, 1, 6, 1)
        self.fontComboBox = QtWidgets.QFontComboBox(self.groupBox_2)
        self.fontComboBox.setMinimumSize(QtCore.QSize(260, 30))
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridLayout_15.addWidget(self.fontComboBox, 1, 0, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox_2)
        self.timeEdit.setMinimumSize(QtCore.QSize(260, 30))
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_15.addWidget(self.timeEdit, 2, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateEdit.setMinimumSize(QtCore.QSize(260, 30))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_15.addWidget(self.dateEdit, 3, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox.setMinimumSize(QtCore.QSize(260, 30))
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_15.addWidget(self.spinBox, 4, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox_2)
        self.dateTimeEdit.setMinimumSize(QtCore.QSize(260, 30))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_15.addWidget(self.dateTimeEdit, 5, 0, 1, 1)
        self.gridLayout_16.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        Preview.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Preview)
        self.statusbar.setObjectName("statusbar")
        Preview.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(Preview)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(Preview)
        self.actionClose.setObjectName("actionClose")
        self.actionExit = QtWidgets.QAction(Preview)
        self.actionExit.setObjectName("actionExit")
        self.actionSave = QtWidgets.QAction(Preview)
        self.actionSave.setObjectName("actionSave")
        self.actionBuild = QtWidgets.QAction(Preview)
        self.actionBuild.setObjectName("actionBuild")
        self.actionDocs = QtWidgets.QAction(Preview)
        self.actionDocs.setObjectName("actionDocs")
        self.actionHelp = QtWidgets.QAction(Preview)
        self.actionHelp.setObjectName("actionHelp")
        self.actionInfo = QtWidgets.QAction(Preview)
        self.actionInfo.setObjectName("actionInfo")

        self.retranslateUi(Preview)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_4.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        self.dial.valueChanged['int'].connect(self.progressBar.setValue)
        self.dial.valueChanged['int'].connect(self.horizontalScrollBar.setValue)
        self.progressBar_2.valueChanged['int'].connect(self.timeEdit.selectAll)
        QtCore.QMetaObject.connectSlotsByName(Preview)

    def retranslateUi(self, Preview):
        _translate = QtCore.QCoreApplication.translate
        Preview.setWindowTitle(_translate("Preview", "MainWindow"))
        Preview.setToolTip(_translate("Preview", "QMainWindow"))
        self.centralwidget.setToolTip(_translate("Preview", "QWidget"))
        self.tabWidget.setToolTip(_translate("Preview", "QTabWidget"))
        self.tabWidget_2.setToolTip(_translate("Preview", "QTabWidget"))
        self.tab_3.setToolTip(_translate("Preview", "QWidget"))
        self.radioButton.setToolTip(_translate("Preview", "QRadioButton"))
        self.radioButton.setText(_translate("Preview", "RadioButton"))
        self.radioButton_2.setToolTip(_translate("Preview", "QRadioButton"))
        self.radioButton_2.setText(_translate("Preview", "RadioButton"))
        self.radioButton_3.setToolTip(_translate("Preview", "QRadioButton"))
        self.radioButton_3.setText(_translate("Preview", "RadioButton"))
        self.checkBox.setToolTip(_translate("Preview", "QCheckBox"))
        self.checkBox.setText(_translate("Preview", "CheckBox"))
        self.checkBox_2.setToolTip(_translate("Preview", "QCheckBox"))
        self.checkBox_2.setText(_translate("Preview", "CheckBox"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("Preview", "GroupBox"))
        self.tab_4.setToolTip(_translate("Preview", "QWidget"))
        self.textEdit.setToolTip(_translate("Preview", "QTextEdit"))
        self.textEdit.setHtml(_translate("Preview", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">QTextEdit</p></body></html>"))
        self.lineEdit.setToolTip(_translate("Preview", "QLineEdit"))
        self.lineEdit.setText(_translate("Preview", "QLineEdit"))
        self.plainTextEdit.setToolTip(_translate("Preview", "QPlainTextEdit"))
        self.plainTextEdit.setPlainText(_translate("Preview", "QPlainTextEdit"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Preview", "Text Edit"))
        self.lineEdit_2.setToolTip(_translate("Preview", "QLineEdit"))
        self.lineEdit_2.setText(_translate("Preview", "123456"))
        self.progressBar.setToolTip(_translate("Preview", "QProgressBar"))
        self.dial.setToolTip(_translate("Preview", "<html><head/><body><p>QDial</p></body></html>"))
        self.horizontalScrollBar.setToolTip(_translate("Preview", "<html><head/><body><p>QScrollBar</p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("Preview", "Misc"))
        self.tabWidget_3.setToolTip(_translate("Preview", "QTabWidget"))
        self.Tex.setToolTip(_translate("Preview", "QWidget"))
        self.toolButton.setToolTip(_translate("Preview", "QToolButton"))
        self.toolButton.setText(_translate("Preview", "... Tool ..."))
        self.pushButton_2.setToolTip(_translate("Preview", "QPushButton"))
        self.pushButton_2.setText(_translate("Preview", "PushButton Flat"))
        self.pushButton_3.setToolTip(_translate("Preview", "QPushButton"))
        self.pushButton_3.setText(_translate("Preview", "PushButton Default"))
        self.buttonBox.setToolTip(_translate("Preview", "QDiaogButtonBox"))
        self.pushButton_4.setToolTip(_translate("Preview", "QPushButton"))
        self.pushButton_4.setText(_translate("Preview", "PushButton Disabled"))
        self.pushButton.setToolTip(_translate("Preview", "QPushButton"))
        self.pushButton.setText(_translate("Preview", "PushButton Normal"))
        self.commandLinkButton.setToolTip(_translate("Preview", "QCommandLinkButton"))
        self.commandLinkButton.setText(_translate("Preview", "Command Link Button"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.Tex), _translate("Preview", "Buttons"))
        self.tab_5.setToolTip(_translate("Preview", "QWidget"))
        self.tableWidget.setToolTip(_translate("Preview", "QTableWidget"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Preview", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Preview", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Preview", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Preview", "New Row"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Preview", "New Row"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Preview", "New Row"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Preview", "New Row"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Preview", "New Row"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Preview", "New Row"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Preview", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Preview", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Preview", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Preview", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Preview", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Preview", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Preview", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Preview", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Preview", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Preview", "New Column"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("Preview", "Tab Edit"))
        self.tabWidget_4.setToolTip(_translate("Preview", "QTabWidget"))
        self.tab_6.setToolTip(_translate("Preview", "QWidget"))
        self.listWidget.setToolTip(_translate("Preview", "QListWidget"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Preview", "QListView"))
        item = self.listWidget.item(1)
        item.setText(_translate("Preview", "QListWidget"))
        item = self.listWidget.item(2)
        item.setText(_translate("Preview", "New Item"))
        item = self.listWidget.item(3)
        item.setText(_translate("Preview", "New Item"))
        item = self.listWidget.item(4)
        item.setText(_translate("Preview", "New Item"))
        item = self.listWidget.item(5)
        item.setText(_translate("Preview", "New Item"))
        item = self.listWidget.item(6)
        item.setText(_translate("Preview", "New Item"))
        item = self.listWidget.item(7)
        item.setText(_translate("Preview", "New Item"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget.setToolTip(_translate("Preview", "QTreeWidget"))
        self.treeWidget.headerItem().setText(0, _translate("Preview", "QTreeWidget"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Preview", "New Item"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Preview", "New Item"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("Preview", "New Item"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("Preview", "New Item"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("Preview", "New Item"))
        self.treeWidget.topLevelItem(5).setText(0, _translate("Preview", "New Item"))
        self.treeWidget.topLevelItem(6).setText(0, _translate("Preview", "New Item"))
        self.treeWidget.topLevelItem(7).setText(0, _translate("Preview", "New Item"))
        self.treeWidget.topLevelItem(8).setText(0, _translate("Preview", "New Item"))
        self.treeWidget.topLevelItem(9).setText(0, _translate("Preview", "New Item"))
        self.treeWidget.topLevelItem(10).setText(0, _translate("Preview", "New Item"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tableWidget_2.setToolTip(_translate("Preview", "QTableWidget"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_6), _translate("Preview", "Items"))
        self.tab_7.setToolTip(_translate("Preview", "QWidget"))
        self.listView.setToolTip(_translate("Preview", "QListView"))
        self.treeView.setToolTip(_translate("Preview", "QTreeView"))
        self.tableView.setToolTip(_translate("Preview", "QTableView"))
        self.columnView.setToolTip(_translate("Preview", "QColumnView"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_7), _translate("Preview", "Views"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Preview", "Main Widgets"))
        self.tab_2.setToolTip(_translate("Preview", "QWidget"))
        self.groupBox.setToolTip(_translate("Preview", "QGroupBox"))
        self.groupBox.setTitle(_translate("Preview", "Containers"))
        self.scrollArea.setToolTip(_translate("Preview", "QScrollArea"))
        self.toolBox.setToolTip(_translate("Preview", "QToolBox"))
        self.page.setToolTip(_translate("Preview", "QWidget"))
        self.progressBar_2.setToolTip(_translate("Preview", "QProgressBar"))
        self.progressBar_3.setToolTip(_translate("Preview", "QProgressBar"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Preview", "Page 1"))
        self.page_2.setToolTip(_translate("Preview", "QWidget"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Preview", "Page 2"))
        self.stackedWidget.setToolTip(_translate("Preview", "QStackedWidget"))
        self.page_3.setToolTip(_translate("Preview", "QWidget"))
        self.lcdNumber.setToolTip(_translate("Preview", "QLCDNumber"))
        self.progressBar_4.setToolTip(_translate("Preview", "QProgressBar"))
        self.line.setToolTip(_translate("Preview", "Line"))
        self.page_4.setToolTip(_translate("Preview", "QWidget"))
        self.frame.setToolTip(_translate("Preview", "QFrame"))
        self.graphicsView.setToolTip(_translate("Preview", "QGraphicsView"))
        self.widget.setToolTip(_translate("Preview", "QWidget"))
        self.openGLWidget.setToolTip(_translate("Preview", "QOpenGLWidget"))
        self.groupBox_2.setToolTip(_translate("Preview", "QGroupBox"))
        self.groupBox_2.setTitle(_translate("Preview", "Inputs box"))
        self.comboBox.setToolTip(_translate("Preview", "QComboBox"))
        self.comboBox.setItemText(0, _translate("Preview", "New Item"))
        self.comboBox.setItemText(1, _translate("Preview", "New Item"))
        self.comboBox.setItemText(2, _translate("Preview", "New Item"))
        self.comboBox.setItemText(3, _translate("Preview", "New Item"))
        self.comboBox.setItemText(4, _translate("Preview", "New Item"))
        self.comboBox.setItemText(5, _translate("Preview", "New Item"))
        self.comboBox.setItemText(6, _translate("Preview", "New Item"))
        self.comboBox.setItemText(7, _translate("Preview", "New Item"))
        self.calendarWidget.setToolTip(_translate("Preview", "QCalendarWidget"))
        self.fontComboBox.setToolTip(_translate("Preview", "QFontComboBox"))
        self.timeEdit.setToolTip(_translate("Preview", "QTimeEdit"))
        self.spinBox.setToolTip(_translate("Preview", "QSpinBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Preview", "Misc Widgets"))
        self.statusbar.setToolTip(_translate("Preview", "QStatusBar"))
        self.actionOpen.setText(_translate("Preview", "Open"))
        self.actionClose.setText(_translate("Preview", "Close"))
        self.actionExit.setText(_translate("Preview", "Exit"))
        self.actionSave.setText(_translate("Preview", "Save"))
        self.actionBuild.setText(_translate("Preview", "Build"))
        self.actionDocs.setText(_translate("Preview", "Docs"))
        self.actionHelp.setText(_translate("Preview", "Help"))
        self.actionInfo.setText(_translate("Preview", "Info"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Preview = QtWidgets.QMainWindow()
    ui = Ui_Preview()
    ui.setupUi(Preview)
    Preview.show()
    sys.exit(app.exec_())
