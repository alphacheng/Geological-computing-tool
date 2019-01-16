import sys
import random
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


def read_file(file):
    with open(file, 'r') as f:
        data = f.readlines()
    x, y = [], []
    for line in data:
        list_ = line.split()
        x.append(float(list_[0]))
        y.append(float(list_[1]))
    return x, y


def compute_1(x: list, y: list):
    new_x, new_y = [], []
    new_x = x
    for i in y:
        new_y.append(i - float(random.uniform(0, 50)))
    return new_x, new_y


def compute_2(x: list, y: list) -> tuple:
    new_x, new_y = [], []
    new_x = x
    for i in y:
        new_y.append(i - float(random.uniform(0, 50)))
    return new_x, new_y


def compute_3(x: float, y: float, z: float) -> float:
    return (x + y) / z


def compute_4_1(x: float, y: float, z: float) -> float:
    return (x + y) / z


def compute_4_2(x: float, y: float, z: float) -> float:
    x = x + 1
    return (x + y) / z


class Drawing(QtWidgets.QWidget):
    window_title = 'SWPU'
    window_icon = '../input/logo.png'

    def __init__(self, x=[1, 2, 3], y=[3, 2, 3], other=False, x_2=None, y_2=None, title_1=None, title_2=None):
        super(Drawing, self).__init__()
        self.setWindowTitle(self.window_title)
        self.setWindowIcon(QIcon(self.window_icon))  # 窗口图标
        # 设置子窗口大小
        self.resize(1254, 651) if other else self.resize(654, 600)
        # 获取参数
        self.x, self.y = x, y
        self.x_2, self.y_2 = x_2, y_2
        self.title_1, self.title_2 = title_1, title_2
        # 设置中文
        self.figure = plt.figure()
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.other = other
        self.count = 2 if other else 1
        self.plot()

        # 布局
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self):
        ''' plot some random stuff '''
        try:
            ax_1 = plt.subplot(1, self.count, 1)
            plt.sca(ax_1)
            plt.plot(self.x, self.y, '*-')
            plt.xlabel('X轴')
            plt.ylabel('Y轴')
            plt.title(self.title_1)
            ax = plt.gca()
            ax.xaxis.set_ticks_position('top')
            ax.invert_xaxis()
            ax.yaxis.set_ticks_position('left')

            if self.other:
                ax_2 = plt.subplot(1, self.count, 2)
                plt.sca(ax_2)
                plt.plot(self.x_2, self.y_2, '*-')
                plt.xlabel('X轴')
                plt.ylabel('Y轴')
                plt.title(self.title_2)

            ax = plt.gca()
            ax.xaxis.set_ticks_position('top')
            ax.invert_xaxis()
            ax.yaxis.set_ticks_position('left')
            self.canvas.draw()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # x, y = read_file('D:/py-code/web-security-check/input/input_data.txt')
    app = QtWidgets.QApplication(sys.argv)
    main = Drawing(x=[-1, -2, -1], y=[-1, -2, -3], other=True, x_2=[1, 2, 3], y_2=[1, 3, 3])
    # main = Window(x=[1, 2, 3], y=[3, 2, 3], title_1='Test')
    # main = Window()
    main.show()

    sys.exit(app.exec_())
