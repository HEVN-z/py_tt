import sys
from PyQt5.QtWidgets import QMainWindow,QVBoxLayout,QWidget,QApplication
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui
from PyQt5.QtCore import QUrl
app=QApplication(sys.argv)

mainWindow=QMainWindow()
mainWindow.setWindowIcon(QtGui.QIcon('08pyQT/google_icon.ico'))
mainWindow.setGeometry(100,100,1280,720)
mainWindow.setWindowTitle('PyQT5 WebView : Google TH')
widget=QWidget()

web=QWebEngineView()
web.history().clear()
profile = QWebEngineProfile.defaultProfile()
cookie_store = profile.cookieStore()
cookie_store.deleteAllCookies()
web.load(QUrl("http://google.co.th"))

verticalLayout=QVBoxLayout()
verticalLayout.addWidget(web)

widget.setLayout(verticalLayout)
mainWindow.setCentralWidget(widget)
mainWindow.show()

sys.exit(app.exec_())
