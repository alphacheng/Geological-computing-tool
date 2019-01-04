# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '03.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1271, 685)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1271, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_one = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_one.setObjectName("pushButton_one")
        self.horizontalLayout.addWidget(self.pushButton_one)
        self.pushButton_two = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_two.setObjectName("pushButton_two")
        self.horizontalLayout.addWidget(self.pushButton_two)
        self.pushButton_three = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_three.setObjectName("pushButton_three")
        self.horizontalLayout.addWidget(self.pushButton_three)
        self.pushButton_four = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_four.setObjectName("pushButton_four")
        self.horizontalLayout.addWidget(self.pushButton_four)
        self.pushButton_five = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_five.setObjectName("pushButton_five")
        self.horizontalLayout.addWidget(self.pushButton_five)
        self.pushButton_six = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_six.setObjectName("pushButton_six")
        self.horizontalLayout.addWidget(self.pushButton_six)
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(0, 30, 1271, 16))
        self.tableView.setStyleSheet("width:1px;\n"
"background-color:grey;")
        self.tableView.setObjectName("tableView")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 40, 1271, 641))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 195, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.import_data_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.import_data_btn.setStyleSheet("")
        self.import_data_btn.setObjectName("import_data_btn")
        self.horizontalLayout_2.addWidget(self.import_data_btn)
        self.export_data_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.export_data_btn.setObjectName("export_data_btn")
        self.horizontalLayout_2.addWidget(self.export_data_btn)
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(550, 330, 131, 51))
        self.toolButton.setStyleSheet("background-color:#5B9BD5;\n"
"color:white;\n"
"font-size:30px;\n"
"font-weight:900;")
        self.toolButton.setObjectName("toolButton")
        self.label_1 = QtWidgets.QLabel(self.frame)
        self.label_1.setGeometry(QtCore.QRect(0, 160, 521, 321))
        self.label_1.setStyleSheet("background-color:grey;\n"
"")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(720, 160, 561, 331))
        self.label_2.setStyleSheet("background-color:grey;")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        self.pushButton_one.clicked.connect(self.frame.lower)
        self.pushButton_two.clicked.connect(self.frame.hide)
        self.pushButton_three.clicked.connect(self.frame.lower)
        self.pushButton_four.clicked.connect(self.frame.close)
        self.pushButton_five.clicked.connect(self.frame.repaint)
        self.pushButton_six.clicked.connect(self.frame.show)
        self.import_data_btn.clicked.connect(self.import_data_btn.show)
        self.export_data_btn.clicked.connect(self.export_data_btn.hide)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_one.setText(_translate("Form", "浅层地层破裂压力计算"))
        self.pushButton_two.setText(_translate("Form", "钻井隔水导管极限承载力计算"))
        self.pushButton_three.setText(_translate("Form", "隔水导管最小入泥深度"))
        self.pushButton_four.setText(_translate("Form", "井口载荷分析及入泥深度推荐"))
        self.pushButton_five.setText(_translate("Form", "隔水导管强度校核和稳定性分析"))
        self.pushButton_six.setText(_translate("Form", "隔水导管轴向失稳临界载荷分析"))
        self.import_data_btn.setText(_translate("Form", "导入数据"))
        self.export_data_btn.setText(_translate("Form", "导出数据"))
        self.toolButton.setText(_translate("Form", "=>"))
        self.label_1.setText(_translate("Form", "                         数据未导入"))
        self.label_2.setText(_translate("Form", "                           数据未导入"))

