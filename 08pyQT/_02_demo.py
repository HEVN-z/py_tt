import sys
from PyQt5.QtWidgets import QApplication, QWidget, QBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5 import uic

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('08pyQT/_02_gui.ui', self)
        self.setWindowTitle('My App')
        self.button.clicked.connect(self.sayHello)

        # self.input.setText('Hello World')

    def sayHello(self):
        inputText = self.input.text()
        self.output.setText('Hello {0}'.format(inputText))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet('''
    #     QWidget{
    #         font-size: 30px
    #     }
    # ''')
    MyApp = MyApp()
    MyApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window ...')