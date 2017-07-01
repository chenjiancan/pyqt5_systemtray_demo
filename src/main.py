"""
    PyQt 系统托盘示例代码
    1. 以 QDialog 为基类 MainWindow 主界面
    2. 以 QSystemTrayIcon 为基类定义 SystemTrayIcon 类，设置右键菜单，定义信号
    3. 为 MainWindow 类实例化一个 SystemTrayIcon
    4. 关联 MainWindow 和 SystemTrayIcon 的信号槽
"""
import sys

from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QDialog, QCheckBox

from src.rc.rc_img import *
from src.ui.ui_main_window import Ui_Dialog


class SystemTrayIcon(QSystemTrayIcon):
    show_window = pyqtSignal()  # show action
    quit = pyqtSignal()         # quit action

    def __init__(self, parent=None):
        super(SystemTrayIcon, self).__init__(parent)
        self.setIcon(QIcon("../res/glyphicons-social-26-quora.png"))
        self.setToolTip("托盘tooltip")

        self.tray_menu = None
        self.setup_menu()

        # 点击信号处理
        self.messageClicked.connect(self.on_message_clicked)
        self.activated.connect(self.on_activated)

    def setup_menu(self):
        self.tray_menu = QMenu()  # 右键菜单

        action_show = QAction(self)
        action_quit = QAction(self)
        action_setting = QAction(self)
        action_about = QAction(self)

        # 设置右键菜单图标
        action_show.setIcon(QIcon("../res/glyphicons-social-26-quora.png"))
        action_quit.setIcon(QIcon("../res/glyphicons-389-exit.png"))
        action_setting.setIcon(QIcon("../res/glyphicons-281-settings.png"))
        action_about.setIcon(QIcon("../res/glyphicons-195-question-sign.png"))

        # -- 二级菜单
        self.sub_menu = QMenu()
        action_setting_setting1 = QAction(self)
        action_setting_setting1.setText("sub setting")
        # action_setting_setting1.setIcon(QIcon("../res/glyphicons-281-settings.png"))
        action_setting_setting1.setIcon(QIcon(":/img/about"))

        self.sub_menu.addAction(action_setting_setting1)
        action_setting.setMenu(self.sub_menu)

        # 设置菜单文本
        action_show.setText("显示")
        action_quit.setText("退出")
        action_setting.setText("设置")
        action_about.setText("关于")

        self.tray_menu.addAction(action_show)
        self.tray_menu.addAction(action_quit)
        self.tray_menu.addAction(action_setting)
        self.tray_menu.addAction(action_about)

        self.setContextMenu(self.tray_menu)
        action_show.triggered.connect(self.show_window)
        action_quit.triggered.connect(self.quit)
        action_about.triggered.connect(self.welcome)

    def on_activated(self, reason):
        """托盘图标被点击
            有三种情况：左单击，左双击，右单击
        """

        print("on_activated {}".format(reason))
        if reason == QSystemTrayIcon.DoubleClick:
            # self.showMessage("activated: ", "左双击")
            print("左双击")
        elif reason == QSystemTrayIcon.Trigger:
            # self.showMessage("activated: ", "左单击")
            print("左单击")

        elif reason == QSystemTrayIcon.Context :
            # self.showMessage("activated: ", "右单击")
            print("右单击")


    def on_message_clicked(self):
        """弹出消息被点击"""
        print("on messaged clicked")
        self.show_window.emit()

    def welcome(self):
        self.showMessage("托盘标题", "托盘消息内容", msecs=1000)

    def show(self):
        super(SystemTrayIcon, self).show()
        QTimer.singleShot(1000, self.welcome)


class MainWindow(QDialog, Ui_Dialog):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.checkBoxIsShowTray.setChecked(True)
        self.checkBoxIsShowTray.show()

        self.system_tray = SystemTrayIcon(self)
        self.system_tray.show()

        # signal & slot
        self.system_tray.show_window.connect(self.showMaximized)
        self.system_tray.quit.connect(self.close)
        self.checkBoxIsShowTray.toggled.connect(lambda show: self.system_tray.show() if show else self.system_tray.hide())

    def showNormal1(self):
        print("showNormal1")

def main_entry():
    app = QApplication(sys.argv)
    # setup_systemtrayicon()

    mw = MainWindow()
    mw.show()

    app.exec()


if __name__ == '__main__':
    main_entry()



