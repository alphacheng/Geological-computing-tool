# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
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
        Form.resize(1389, 146)
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.import_data_btn = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.import_data_btn.setStyleSheet("")
        self.import_data_btn.setObjectName("import_data_btn")
        self.horizontalLayout_2.addWidget(self.import_data_btn, 0, QtCore.Qt.AlignVCenter)
        self.export_data_btn = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.export_data_btn.setObjectName("export_data_btn")
        self.horizontalLayout_2.addWidget(self.export_data_btn, 0, QtCore.Qt.AlignVCenter)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setMinimumSize(QtCore.QSize(269, 0))
        self.lineEdit.setStyleSheet("font-size:30px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_5.addWidget(self.lineEdit, 1, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.export_data_btn_2 = QtWidgets.QPushButton(self.tab)
        self.export_data_btn_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.export_data_btn_2.setObjectName("export_data_btn_2")
        self.gridLayout_5.addWidget(self.export_data_btn_2, 0, 1, 1, 1)
        self.compute_button_1 = QtWidgets.QPushButton(self.tab)
        self.compute_button_1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.compute_button_1.setStyleSheet("background-color:#5B9BD5;\n"
"color:white;\n"
"font-size:30px;\n"
"font-weight:900;")
        self.compute_button_1.setObjectName("compute_button_1")
        self.gridLayout_5.addWidget(self.compute_button_1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 1, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMaximumSize(QtCore.QSize(200, 100))
        self.label.setStyleSheet("font-size:50px;")
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 1, 5, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.export_data_btn_3 = QtWidgets.QPushButton(self.tab_3)
        self.export_data_btn_3.setObjectName("export_data_btn_3")
        self.gridLayout_6.addWidget(self.export_data_btn_3, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.compute_btn_3 = QtWidgets.QPushButton(self.tab_3)
        self.compute_btn_3.setMaximumSize(QtCore.QSize(980, 16777215))
        self.compute_btn_3.setObjectName("compute_btn_3")
        self.gridLayout_6.addWidget(self.compute_btn_3, 0, 1, 1, 2, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem5, 0, 6, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem6, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.export_data_btn_4 = QtWidgets.QPushButton(self.tab_4)
        self.export_data_btn_4.setObjectName("export_data_btn_4")
        self.gridLayout_9.addWidget(self.export_data_btn_4, 0, 4, 1, 1)
        self.compute_btn_4 = QtWidgets.QPushButton(self.tab_4)
        self.compute_btn_4.setMaximumSize(QtCore.QSize(980, 16777215))
        self.compute_btn_4.setObjectName("compute_btn_4")
        self.gridLayout_9.addWidget(self.compute_btn_4, 0, 3, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton.setStyleSheet("")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_9.addWidget(self.radioButton, 0, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_2.setStyleSheet("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_9.addWidget(self.radioButton_2, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem7, 0, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem8, 0, 0, 1, 1)
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
        self.radioButton.clicked['bool'].connect(self.radioButton.setChecked)
        self.radioButton_2.clicked['bool'].connect(self.radioButton_2.setChecked)
        self.compute_btn_4.clicked.connect(self.compute_btn_4.show)
        self.export_data_btn_2.clicked.connect(self.export_data_btn_2.show)
        self.compute_button_1.clicked.connect(self.compute_button_1.show)
        self.export_data_btn_3.clicked.connect(self.export_data_btn_3.show)
        self.compute_btn_3.clicked.connect(self.compute_btn_3.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SWPU"))
        self.import_data_btn.setText(_translate("Form", "导入数据"))
        self.export_data_btn.setText(_translate("Form", "导出数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("Form", "浅层地层破裂压力计算 "))
        self.export_data_btn_2.setText(_translate("Form", "导出数据"))
        self.compute_button_1.setText(_translate("Form", "计算"))
        self.label.setText(_translate("Form", "K="))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "钻井隔水导管极限承载力计算 "))
        self.export_data_btn_3.setText(_translate("Form", "导出"))
        self.compute_btn_3.setText(_translate("Form", "打开"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "隔水导管最小入泥深度 "))
        self.export_data_btn_4.setText(_translate("Form", "导出"))
        self.compute_btn_4.setText(_translate("Form", "打开"))
        self.radioButton.setText(_translate("Form", "井口载荷=防喷器重量+表层套管重量+表层套管固井水泥浆重量"))
        self.radioButton_2.setText(_translate("Form", "井口载荷=防喷器重量+表层套管重量+技术套管过提重量"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "井口载荷分析及入泥深度推荐 "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "隔水导管强度校核和稳定性分析 "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "隔水导管轴向失稳临界载荷分析 "))

