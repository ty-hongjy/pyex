'''
Description: gf-keda
Autor: name
Date: 2024-08-30 17:24:50
LastEditors: hongjy
LastEditTime: 2024-08-30 17:29:22
'''
from PyQt5.QtWidgets import QApplication
from window import GomokuWindow
from game import Gomoku
import sys


def main():
    # g = Gomoku()
    # g.play()
    app = QApplication(sys.argv)
    ex = GomokuWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
