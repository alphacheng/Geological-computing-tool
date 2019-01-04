import sys
from PyQt5 import QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from collections import OrderedDict


class Window(QtWidgets.QDialog):
    def __init__(self, x=[1, 2, 3], y=[3, 2, 3]):
        super(Window, self).__init__()

        self.x = x
        self.y = y

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.plot()

        # set the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot(self):
        ''' plot some random stuff '''
        try:
            # random data

            # create an axis
            # ax = self.figure.add_subplot(111)

            # discards the old graph
            # ax.hold(False)

            # plot data
            plt.plot(self.x, self.y, '*-')
            plt.xlabel('X轴')  # 说明x轴表示经度
            plt.ylabel('Y轴')  # 说明y轴表示纬度
            ax = plt.gca()
            ax.xaxis.set_ticks_position('top')
            ax.invert_xaxis()
            ax.yaxis.set_ticks_position('left')
            handles, labels = plt.gca().get_legend_handles_labels()
            by_label = OrderedDict(zip(labels, handles))
            plt.legend(by_label.values(), by_label.keys())

            # refresh canvas
            self.canvas.draw()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
