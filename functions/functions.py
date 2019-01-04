import random
import matplotlib.pyplot as plt
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


if __name__ == '__main__':
    x, y = read_file('D:/py-code/web-security-check/input/input_data.txt')
    drawing(x, y, title='输入', path='../output/input_data.png')
