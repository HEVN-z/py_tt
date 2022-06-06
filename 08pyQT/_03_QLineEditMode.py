import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.Window_width, self.Window_height = 300,200
        self.resize(self.Window_width,self.Window_height)
        self.setWindowTitle('QLineEdit Mode')

        layout = QVBoxLayout()
        self.setLayout(layout)

        lineEdits = {}

        lineEdits['NoEcho'] = QLineEdit()
        lineEdits['NoEcho'].setPlaceholderText('No Echo')
        lineEdits['NoEcho'].setEchoMode(QLineEdit.EchoMode.NoEcho)
        lineEdits['NoEcho'].textChanged.connect(self.printValue)
        layout.addWidget(lineEdits['NoEcho'])

        lineEdits['Normal'] = QLineEdit()
        lineEdits['Normal'].setPlaceholderText('Normal')
        lineEdits['Normal'].setEchoMode(QLineEdit.EchoMode.Normal)
        lineEdits['Normal'].textChanged.connect(self.printValue)

        lineEdits['Password'] = QLineEdit()
        lineEdits['Password'].setPlaceholderText('Password')
        lineEdits['Password'].setEchoMode(QLineEdit.EchoMode.Password)
        lineEdits['Password'].textChanged.connect(self.printValue)

        lineEdits['PasswordEchoOnEdit'] = QLineEdit()
        lineEdits['PasswordEchoOnEdit'].setPlaceholderText('PasswordEchoOnEdit')
        lineEdits['PasswordEchoOnEdit'].setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        lineEdits['PasswordEchoOnEdit'].textChanged.connect(self.printValue)

        for _, item in lineEdits.items():
            layout.addWidget(item)

    def printValue(self,v):
        print(v)
        
if __name__ == '__main__':
    # don't auto scale when drag app to different monitor.
    # QGuiApplication.setGighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget{
            font=size" 17px
        }
    ''')
    App = MyApp()
    App.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing window...')