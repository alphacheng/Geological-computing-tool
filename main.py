from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QDesktopWidget
from QTdesigner.UI import Ui_Form
from functions.functions import *
from functions.table import *


class MyPyQT_Form(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)
        self.x = []
        self.y = []
        self.result_x = []
        self.result_y = []
        self.position_x = -100
        self.position_y = 80

        # 重写点击事件
        # page1
        self.import_data_btn.clicked.connect(self.import_data_page_1)
        self.export_data_btn.clicked.connect(self.export_data_page_1)
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

        # 设置父窗口标题、图标
        self.setWindowTitle('浅层地层破裂压力计算工具')  # 窗口标题
        self.setWindowIcon(QIcon('./input/logo.png'))  # 窗口图标
        # 初始化时窗口居中
        # self.center()

        # 初始化位置左上角
        self.move(0, 0)

        # 设置子窗口标题、图标
        Drawing.window_title = 'SWPU'
        Drawing.window_icon = 'logo.png'
        Table.window_title = 'SWPU'
        Table.window_icon = 'logo.png'

    def center(self):
        """窗口居中"""
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width() - 300) / 2,
                  (screen.height() - size.height() - 200) / 2)

    def alert(self, msg: str):
        QMessageBox.information(self, "警告",
                                self.tr(msg))

    def change_position(self) -> (int, int):
        """每次新建子窗口时更改位置"""
        self.position_x += 100
        self.position_y += 100
        return self.position_x, self.position_y

    def closeEvent(self, event):
        """退出确认"""
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def import_data_page_1(self):
        """导入数据"""
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, '导入数据', './input', ('*.txt'))
        if file_path[0]:
            try:
                self.x, self.y = read_file(file_path[0])
                new_x, new_y = compute_1(self.x, self.y)
                child_win = Drawing(self.x, self.y, other=True, x_2=new_x, y_2=new_y, title_1='输入', title_2='结果')
                child_win.move(*self.change_position())
                child_win.show()

                self.result_x = new_x
                self.result_y = new_y
            except Exception as e:
                print(e)
                raise e
        else:
            print('No such file')

    def export_data_page_1(self):
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

    def compute_page_2(self):
        """page2的计算按钮"""
        key = self.lineEdit.text()
        if key and key.isdigit() and self.result_x and self.result_y:
            new_x, new_y = compute_2(self.result_x, self.result_y)
            child_win = Drawing(new_x, new_y, title_1='结果')
            child_win.move(*self.change_position())
            child_win.show()
        else:
            self.alert('计算变量不能为空！')

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

    def compute_page_3(self):
        """page3的计算按钮"""
        try:
            self.table_page_3 = Table(['油田名', '井口载荷', '套管自重', '摩擦阻力', '最小入泥深度'])
            self.table_page_3.formula = compute_3
            self.table_page_3.show()
        except Exception:
            print(Exception)

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

    def compute_page_4(self):
        """page4的计算按钮"""
        try:
            self.table_page_4 = Table(['油田名', '表套重量', '固井水泥浆重', '防喷器重', '井口载荷'])
            self.table_page_4.formula = self.formula
            self.table_page_4.show()
        except Exception:
            print(Exception)

    # 选择page4所用的的计算公式
    def choosed_1(self):
        self.formula = compute_4_1

    def choosed_2(self):
        self.formula = compute_4_2


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())
