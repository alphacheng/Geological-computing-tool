# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'four.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.setEnabled(True)
        Form.resize(1254, 651)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabWidgetPage1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 2, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tabWidgetPage1)
        self.label_2.setMinimumSize(QtCore.QSize(500, 400))
        self.label_2.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setStyleSheet("background-color:grey;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setIndent(1)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 4, 4, 1)
        self.label_1 = QtWidgets.QLabel(self.tabWidgetPage1)
        self.label_1.setMinimumSize(QtCore.QSize(500, 400))
        self.label_1.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.label_1.setStyleSheet("background-color:grey;\n"
"")
        self.label_1.setTextFormat(QtCore.Qt.AutoText)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setIndent(0)
        self.label_1.setOpenExternalLinks(False)
        self.label_1.setObjectName("label_1")
        self.gridLayout_2.addWidget(self.label_1, 2, 0, 4, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 3, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.tabWidgetPage1)
        self.toolButton.setMaximumSize(QtCore.QSize(74, 16777215))
        self.toolButton.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"font-size: 30px;\n"
"font-weight: 700;\n"
"border: solid 1px white;")
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 3, 3, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 0, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 0, 4, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 3, 0, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem3, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.import_data_btn = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.import_data_btn.setStyleSheet("")
        self.import_data_btn.setObjectName("import_data_btn")
        self.horizontalLayout_2.addWidget(self.import_data_btn)
        self.export_data_btn = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.export_data_btn.setObjectName("export_data_btn")
        self.horizontalLayout_2.addWidget(self.export_data_btn)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem5, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setMinimumSize(QtCore.QSize(600, 400))
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setStyleSheet("background-color:grey;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setIndent(1)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 1, 7, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 1, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setMinimumSize(QtCore.QSize(269, 0))
        self.lineEdit.setStyleSheet("font-size:30px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_5.addWidget(self.lineEdit, 1, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.compute_button_1 = QtWidgets.QPushButton(self.tab)
        self.compute_button_1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.compute_button_1.setStyleSheet("background-color:#5B9BD5;\n"
"color:white;\n"
"font-size:30px;\n"
"font-weight:900;")
        self.compute_button_1.setObjectName("compute_button_1")
        self.gridLayout_5.addWidget(self.compute_button_1, 1, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 1, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMaximumSize(QtCore.QSize(200, 100))
        self.label.setStyleSheet("font-size:50px;")
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 1, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem8, 0, 7, 1, 1)
        self.export_data_btn_2 = QtWidgets.QPushButton(self.tab)
        self.export_data_btn_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.export_data_btn_2.setObjectName("export_data_btn_2")
        self.gridLayout_5.addWidget(self.export_data_btn_2, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem9, 1, 4, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.compute_btn_3 = QtWidgets.QPushButton(self.tab_3)
        self.compute_btn_3.setMaximumSize(QtCore.QSize(980, 16777215))
        self.compute_btn_3.setObjectName("compute_btn_3")
        self.gridLayout_6.addWidget(self.compute_btn_3, 0, 2, 1, 1, QtCore.Qt.AlignTop)
        self.export_data_btn_3 = QtWidgets.QPushButton(self.tab_3)
        self.export_data_btn_3.setMinimumSize(QtCore.QSize(100, 0))
        self.export_data_btn_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.export_data_btn_3.setObjectName("export_data_btn_3")
        self.gridLayout_6.addWidget(self.export_data_btn_3, 0, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem10, 0, 1, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(207, 200))
        self.lineEdit_2.setStyleSheet("font-size:20px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_7.addWidget(self.lineEdit_2, 2, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_8.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_7.addWidget(self.lineEdit_8, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"border: solid 1px white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_7.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_5.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"border: solid 1px white;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_7.addWidget(self.pushButton_5, 1, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"border: solid 1px white;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_7.addWidget(self.pushButton, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_4.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_7.addWidget(self.lineEdit_4, 2, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_4.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"border: solid 1px white;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_7.addWidget(self.pushButton_4, 1, 3, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_3.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_7.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"border: solid 1px white;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_7.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_5.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_7.addWidget(self.lineEdit_5, 2, 3, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_7.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_7.addWidget(self.lineEdit_7, 3, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_6.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_7.addWidget(self.lineEdit_6, 2, 4, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_10.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_7.addWidget(self.lineEdit_10, 3, 3, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_11.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_7.addWidget(self.lineEdit_11, 3, 4, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_9.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_7.addWidget(self.lineEdit_9, 3, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 2, 0, 1, 3)
        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.radioButton = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton.setStyleSheet("")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_9.addWidget(self.radioButton, 0, 0, 1, 1)
        self.compute_btn_4 = QtWidgets.QPushButton(self.tab_4)
        self.compute_btn_4.setMaximumSize(QtCore.QSize(980, 16777215))
        self.compute_btn_4.setObjectName("compute_btn_4")
        self.gridLayout_9.addWidget(self.compute_btn_4, 0, 2, 1, 1, QtCore.Qt.AlignTop)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem11, 0, 1, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_6.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"border: solid 1px white;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_10.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_7.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"border: solid 1px white;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_10.addWidget(self.pushButton_7, 1, 3, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_8.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"border: solid 1px white;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_10.addWidget(self.pushButton_8, 1, 4, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_9.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"border: solid 1px white;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_10.addWidget(self.pushButton_9, 1, 1, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_12.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_10.addWidget(self.lineEdit_12, 2, 1, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(207, 200))
        self.lineEdit_13.setStyleSheet("font-size:20px;")
        self.lineEdit_13.setText("")
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_10.addWidget(self.lineEdit_13, 2, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_10.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"border: solid 1px white;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_10.addWidget(self.pushButton_10, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_14.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_10.addWidget(self.lineEdit_14, 2, 3, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_15.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_15.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_10.addWidget(self.lineEdit_15, 2, 2, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_16.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_16.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_10.addWidget(self.lineEdit_16, 2, 4, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_17.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_17.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_10.addWidget(self.lineEdit_17, 3, 0, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_18.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_18.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_10.addWidget(self.lineEdit_18, 3, 1, 1, 1)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_19.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_19.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout_10.addWidget(self.lineEdit_19, 3, 2, 1, 1)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_20.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_20.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout_10.addWidget(self.lineEdit_20, 3, 3, 1, 1)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_21.setMinimumSize(QtCore.QSize(0, 200))
        self.lineEdit_21.setStyleSheet("\n"
"font-size: 20px;\n"
"")
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_10.addWidget(self.lineEdit_21, 3, 4, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_10, 2, 0, 1, 3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_2.setStyleSheet("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_9.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.import_data_btn.clicked.connect(self.import_data_btn.show)
        self.export_data_btn.clicked.connect(self.export_data_btn.show)
        self.export_data_btn_2.clicked.connect(self.export_data_btn_2.show)
        self.compute_button_1.clicked.connect(self.compute_button_1.show)
        self.compute_btn_3.clicked.connect(self.compute_btn_3.show)
        self.export_data_btn_3.clicked.connect(self.export_data_btn_3.show)
        self.radioButton.clicked['bool'].connect(self.radioButton.setChecked)
        self.radioButton_2.clicked['bool'].connect(self.radioButton_2.setChecked)
        self.compute_btn_4.clicked.connect(self.compute_btn_4.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SWPU"))
        self.label_2.setText(_translate("Form", "数据未导入"))
        self.label_1.setText(_translate("Form", "数据未导入"))
        self.toolButton.setText(_translate("Form", "=>"))
        self.pushButton_11.setText(_translate("Form", "查看详细"))
        self.pushButton_12.setText(_translate("Form", "查看详细"))
        self.import_data_btn.setText(_translate("Form", "导入数据"))
        self.export_data_btn.setText(_translate("Form", "导出数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("Form", "浅层地层破裂压力计算 "))
        self.label_3.setText(_translate("Form", "数据未导入"))
        self.compute_button_1.setText(_translate("Form", "计算"))
        self.label.setText(_translate("Form", "K="))
        self.export_data_btn_2.setText(_translate("Form", "导出数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "钻井隔水导管极限承载力计算 "))
        self.compute_btn_3.setText(_translate("Form", "计算"))
        self.export_data_btn_3.setText(_translate("Form", "导出数据"))
        self.pushButton_2.setText(_translate("Form", "井口载荷"))
        self.pushButton_5.setText(_translate("Form", "最小入泥深度"))
        self.pushButton.setText(_translate("Form", "油田名"))
        self.pushButton_4.setText(_translate("Form", "摩擦阻力"))
        self.pushButton_3.setText(_translate("Form", "套管自重"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "隔水导管最小入泥深度 "))
        self.radioButton.setText(_translate("Form", "井口载荷=防喷器重量+表层套管重量+表层套管固井水泥浆重量"))
        self.compute_btn_4.setText(_translate("Form", "计算"))
        self.pushButton_6.setText(_translate("Form", "固井水泥浆重"))
        self.pushButton_7.setText(_translate("Form", "防喷器重"))
        self.pushButton_8.setText(_translate("Form", "井口载荷"))
        self.pushButton_9.setText(_translate("Form", "表套重量"))
        self.pushButton_10.setText(_translate("Form", "油田名"))
        self.radioButton_2.setText(_translate("Form", "井口载荷=防喷器重量+表层套管重量+技术套管过提重量"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "井口载荷分析及入泥深度推荐 "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "隔水导管强度校核和稳定性分析 "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "隔水导管轴向失稳临界载荷分析 "))

