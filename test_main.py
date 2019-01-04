import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QDesktopWidget
from QTdesigner.four import Ui_Form
from functions.functions import *
from test import Window


class MyPyQT_Form(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)
        self.x = []
        self.y = []
        self.result_x = []
        self.result_y = []

        # 重写点击事件
        # page1
        self.import_data_btn.clicked.connect(self.import_data)
        self.export_data_btn.clicked.connect(self.export_data)
        self.pushButton_11.clicked.connect(self.detail_1_1)
        self.pushButton_12.clicked.connect(self.detail_1_2)
        # page2
        self.export_data_btn_2.clicked.connect(self.export_data_page_2)
        self.compute_button_1.clicked.connect(self.compute_page_2)
        # page3
        self.export_data_btn_3.clicked.connect(self.export_data_page_3)
        self.compute_btn_3.clicked.connect(self.compute_page_3)
        # page4
        self.radioButton.clicked['bool'].connect(self.choosed_1)
        self.radioButton_2.clicked['bool'].connect(self.choosed_2)
        self.compute_btn_4.clicked.connect(self.compute_page_4)
        # page4选用公式
        self.formula = None

        self.setWindowTitle('浅层地层破裂压力计算工具')  # 窗口标题
        self.setWindowIcon(QIcon('./input/logo.png'))  # 窗口图标
        self.center()  # 初始化时窗口居中

    def center(self):
        """窗口居中"""
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width() - 300) / 2,
                  (screen.height() - size.height() - 200) / 2)

    def import_data(self):
        """导入数据"""
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, '导入数据', './input', ('*.txt'))
        if file_path[0]:
            try:
                self.x, self.y = read_file(file_path[0])
                drawing(self.x, self.y, title='输入', path='./output/input_data.png')
                img_1 = QPixmap('./output/input_data.png')
                self.label_1.setPixmap(img_1)
                self.label_1.setScaledContents(True)

                new_x, new_y = compute_1(self.x, self.y)
                drawing(new_x, new_y, title='结果', path='./output/result.png')
                img_2 = QPixmap('./output/result.png')
                self.label_2.setPixmap(img_2)
                self.label_2.setScaledContents(True)
                self.result_x = new_x
                self.result_y = new_y
            except Exception as e:
                print(e)
                raise e
        else:
            print('No such file')

    def export_data(self):
        """导出数据"""
        file_path = QtWidgets.QFileDialog.getSaveFileName(self, "save file", "./output",
                                                          "('*.txt)")
        if file_path[0]:
            try:
                with open(file_path[0], 'w') as f:
                    for i in range(0, len(self.result_x)):
                        f.write(str(self.result_x[i]))
                        f.write(' ' + str(self.result_y[i]) + '\n')
            except Exception as e:
                print(e)
                raise e
        else:
            print('No such file')

    def closeEvent(self, event):
        """退出确认"""
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def export_data_page_2(self):
        """page2导出数据"""
        file_path = QtWidgets.QFileDialog.getSaveFileName(self, "save file", "./output",
                                                          "('*.txt)")
        if file_path[0]:
            try:
                with open(file_path[0], 'w') as f:
                    for i in range(0, len(self.result_x)):
                        f.write(str(self.result_x[i]))
                        f.write(' ' + str(self.result_y[i]) + '\n')
            except Exception as e:
                print(e)
                raise e
        else:
            print('No such file')

    def export_data_page_3(self):
        """page3导出数据"""
        file_path = QtWidgets.QFileDialog.getSaveFileName(self, "save file", "./output",
                                                          "('*.txt)")
        if file_path[0]:
            try:
                with open(file_path[0], 'w') as f:
                    for i in range(0, len(self.result_x)):
                        f.write(str(self.result_x[i]))
                        f.write(' ' + str(self.result_y[i]) + '\n')
            except Exception as e:
                print(e)
                raise e
        else:
            print('No such file')

    def compute_page_2(self):
        key = self.lineEdit.text()
        if key and key.isnumeric() and self.result_x and self.result_y:
            new_x, new_y = compute_2(self.result_x, self.result_y)
            drawing(new_x, new_y, title='结果', path='./output/result_2.png')
            img_3 = QPixmap('./output/result_2.png')
            self.label_3.setPixmap(img_3)
            self.label_3.setScaledContents(True)
        else:
            self.alert('计算变量不能为空！')

    def compute_page_3(self):
        a1 = self.lineEdit_3.text()
        b1 = self.lineEdit_4.text()
        c1 = self.lineEdit_5.text()
        a2 = self.lineEdit_8.text()
        b2 = self.lineEdit_9.text()
        c2 = self.lineEdit_10.text()
        ready = True
        variables = [a1, b1, c1, a2, b2, c2]
        for x in variables:
            if x and x.isnumeric():
                continue
            else:
                ready = False
                self.alert('计算变量不能为空！')
                break
        if ready:
            try:
                d1 = compute_3(float(a1), float(b1), float(c1))
                d2 = compute_3(float(a2), float(b2), float(c2))
                self.lineEdit_6.setText(str(d1))
                self.lineEdit_11.setText(str(d2))
            except Exception as e:
                print(e)

    def compute_page_4(self):
        a1 = self.lineEdit_12.text()
        b1 = self.lineEdit_15.text()
        c1 = self.lineEdit_14.text()
        a2 = self.lineEdit_18.text()
        b2 = self.lineEdit_19.text()
        c2 = self.lineEdit_20.text()
        ready = True
        if not self.formula:
            self.alert('请先选择计算方式！')
            return 0
        variables = [a1, b1, c1, a2, b2, c2]
        for x in variables:
            if x and x.isnumeric():
                continue
            else:
                ready = False
                self.alert('计算变量不能为空！')
                break
        if ready:
            try:
                d1 = self.formula(float(a1), float(b1), float(c1))
                d2 = self.formula(float(a2), float(b2), float(c2))
                self.lineEdit_16.setText(str(d1))
                self.lineEdit_21.setText(str(d2))
            except Exception as e:
                print(e)

    def alert(self, msg: str):
        QMessageBox.information(self, "警告",
                                self.tr(msg))

    def choosed_1(self):
        self.formula = compute_4_1

    def choosed_2(self):
        self.formula = compute_4_2

    def detail_1_1(self):
        f = Window(self.x, self.y)
        f.show()

    def detail_1_2(self):
        f = Window(self.result_x, self.result_y)
        f.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    import datetime

    d1 = datetime.datetime(2018, 12, 23)
    d2 = datetime.datetime.now()
    count = (d2 - d1).days
    if count > 15:
        my_pyqt_form.alert('RunOut!')
        sys.exit()
    else:
        my_pyqt_form.show()
    sys.exit(app.exec_())
