import sys
from PyQt5.QtWidgets import QMainWindow,QVBoxLayout,QWidget,QApplication
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl
app=QApplication(sys.argv)

mainWindow=QMainWindow()
widget=QWidget()

web=QWebEngineView()
web.load(QUrl("http://google.co.th"))

verticalLayout=QVBoxLayout()
verticalLayout.addWidget(web)

widget.setLayout(verticalLayout)
mainWindow.setCentralWidget(widget)
mainWindow.show()

sys.exit(app.exec_())