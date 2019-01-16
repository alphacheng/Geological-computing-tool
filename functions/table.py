# QTableView组件的使用
import sys
from PyQt5.QtWidgets import (QAbstractItemView, QAction, QTableView, QHeaderView,
                             QVBoxLayout, QWidget, QApplication, QMainWindow,
                             QMessageBox)
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon


def compute_3(x: float, y: float, z: float) -> float:
    return (x + y) / z


class Table(QMainWindow):
    window_title = 'SWPU'
    window_icon = '../input/logo.png'
    # 如果集成QMainWindow 则self.setLayout(self.layout) 替换成
    """
        widget=QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
    """

    # 即可， 注意集成QWidget和集成QMainWindow时候区别

    def __init__(self, headers=['1', '2', '3', '4', '5']):
        super(Table, self).__init__()
        self.resize(654, 300)
        self.setWindowTitle(self.window_title)
        self.setWindowIcon(QIcon(self.window_icon))  # 窗口图标
        self.layout = QVBoxLayout()
        self.model = QStandardItemModel(2, 2)  # 存储任意结构数据
        self.model.setHorizontalHeaderLabels(headers)

        # 设置计算公式
        self.formula = None

        # 保存计算数据
        self.data = {'n': None, 'x': None, 'y': None, 'z': None, 'r': None}

        # 初始化数据
        for row in range(1):
            for column in range(1):
                i = QStandardItem("油田{}".format(row + 1))
                self.model.setItem(row, column, i)

        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        self.layout.addWidget(self.tableView)

        # 继承QMainWidow使用下面三行代码
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        # 继承QWidget则使用下面这样代码
        # self.setLayout(self.layout)

        # 设置表格充满这个布局QHeaderView
        # self.tableView.horizontalHeader().setStretchLastSection(True)#最后一列决定充满剩下的界面
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面

        # 添加menu菜单栏,注意：QMainWindow 才可以有菜单栏，QWidget没有，因此上面只能采用继承QMainWIndow
        tool = self.addToolBar("File")  # 这里尝试使用QmenuBar，则此时会卡死，无法完成下面appedRow操作（猜测：可能是因为本身不允许menuBar完成这种操作）
        self.action = QAction("添加", self)
        self.action2 = QAction("删除", self)
        self.action3 = QAction("计算", self)
        self.action4 = QAction("清除", self)
        tool.addAction(self.action)
        tool.addAction(self.action2)
        tool.addAction(self.action3)
        tool.addAction(self.action4)
        tool.actionTriggered[QAction].connect(self.process_trigger)

        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中一行
        # self.tableView.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只有行选中

    def alert(self, msg: str):
        QMessageBox.information(self, "警告",
                                self.tr(msg))

    def set_data(self):
        row_count = self.model.rowCount()
        n, x, y, z, r = [], [], [], [], []

        def func(item):
            if not item:
                return 'None'
            else:
                return item.text()

        for row in range(row_count):
            n.append(func(self.model.item(row, 0)))
            x.append(func(self.model.item(row, 1)))
            y.append(func(self.model.item(row, 2)))
            z.append(func(self.model.item(row, 3)))
            r.append(func(self.model.item(row, 4)))
        self.data = {'n': n, 'x': x, 'y': y, 'z': z, 'r': r}
        # print(self.data)

    def calculate(self):
        row_count = self.model.rowCount()
        result = None
        for i in range(row_count):
            data = []
            try:
                for x in range(1, 4):
                    item = self.model.item(i, x)
                    if item:
                        data.append(float(item.text()))
                if len(data) == 3:
                    result = self.formula(*data)
                    r = QStandardItem("{}".format(result))
                    self.model.setItem(i, 4, r)
            except Exception as e:
                self.alert("数据输入不正确或输入框未失去焦点！")
                print(e)
        if not result:
            self.alert("数据输入不正确或输入框未失去焦点！")
        self.set_data()

    def clear_data(self):
        row_count = self.model.rowCount()
        for i in range(0, row_count):
            self.model.removeRow(0)

    def process_trigger(self, action):
        if action.text() == "添加":
            row_count = self.model.rowCount()
            self.model.appendRow([
                QStandardItem('油田{}'.format(row_count + 1)),
                QStandardItem(),
                QStandardItem(),
                QStandardItem(),
                QStandardItem(),
            ])
        if action.text() == "删除":
            r = self.tableView.selectionModel().selectedRows()  # 获取被选中行
            print(r)  # 被选中行的列表，每个元素是ModelIndex对象
            # indexs = self.tableView.selectionModel().selection().indexes()#返回结果是QModelIndex类对象，里面有row和column方法获取行列索引
            # print(indexs[0].row())
            if r:
                # 下面删除时，选中多行中的最后一行，会被删掉；不选中，则默认第一行删掉
                index = self.tableView.currentIndex()
                # print(index.row())
                self.model.removeRow(index.row())
        if action.text() == "计算":
            self.calculate()

        if action.text() == "清除":
            self.clear_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Table()
    win.formula = compute_3
    win.show()
    sys.exit(app.exec_())
