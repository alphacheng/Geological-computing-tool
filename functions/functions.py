import sys
import random
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from collections import OrderedDict


def drawing(x, y, title, path):
    fig = plt.figure()
    fig.tight_layout()
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.grid(None, 'major', 'both')  # 画出网格背景
    plt.plot(x, y, color='green', label='cab 1')
    plt.title(title)
    plt.xlabel('X轴')  # 说明x轴表示经度
    plt.ylabel('Y轴')  # 说明y轴表示纬度
    ax = plt.gca()
    ax.xaxis.set_ticks_position('top')
    ax.invert_xaxis()
    ax.yaxis.set_ticks_position('left')
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    # plt.show()
    plt.savefig(path)


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


class Window(QtWidgets.QWidget):
    def __init__(self, x=[1, 2, 3], y=[3, 2, 3], other=False, x_2=None, y_2=None):
        super(Window, self).__init__()
        self.setWindowTitle('SWPU')
        self.setWindowIcon(QIcon('../input/logo.png'))  # 窗口图标

        self.resize(1254, 651) if other else self.resize(654, 600)

        self.x, self.y = x, y
        self.x_2, self.y_2 = x_2, y_2

        # a figure instance to plot on
        self.figure = plt.figure()
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.count = 2 if other else 1
        self.plot()

        # set the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self):
        ''' plot some random stuff '''
        try:
            # plot data
            ax_1 = plt.subplot(1, self.count, 1)
            plt.sca(ax_1)
            plt.plot(self.x, self.y, '*-')
            plt.xlabel('X轴')  # 说明x轴表示经度
            plt.ylabel('Y轴')  # 说明y轴表示纬度
            plt.title('1')
            ax = plt.gca()
            ax.xaxis.set_ticks_position('top')
            ax.invert_xaxis()
            ax.yaxis.set_ticks_position('left')

            ax_2 = plt.subplot(1, self.count, 2)
            plt.sca(ax_2)
            plt.plot(self.x_2, self.y_2, '*-')
            plt.xlabel('X轴')  # 说明x轴表示经度
            plt.ylabel('Y轴')  # 说明y轴表示纬度
            plt.title('2')

            ax = plt.gca()
            ax.xaxis.set_ticks_position('top')
            ax.invert_xaxis()
            ax.yaxis.set_ticks_position('left')
            #handles, labels = plt.gca().get_legend_handles_labels()
            #by_label = OrderedDict(zip(labels, handles))
            #plt.legend(by_label.values(), by_label.keys())

            # refresh canvas
            self.canvas.draw()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # x, y = read_file('D:/py-code/web-security-check/input/input_data.txt')
    # drawing(x, y, title='输入', path='../output/input_data.png')
    app = QtWidgets.QApplication(sys.argv)
    #main = Window(x=[1, 2, 3], y=[3, 2, 3], other=True, x_2=[1, 2, 3], y_2=[1, 3, 3])
    main = Window(x=[1, 2, 3], y=[3, 2, 3])
    # main = Window()
    main.show()

    sys.exit(app.exec_())
