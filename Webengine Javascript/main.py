from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import QObject, pyqtSlot, QUrl, QVariant
import os

class CallHandler(QObject):


    @pyqtSlot(result=QVariant)
    def Send(self):
        return QVariant("PyQt5 to Js")
    

    @pyqtSlot(QVariant, result=QVariant)
    def Receive(self, args):
      print(args)


class WebView(QWebEngineView):

    def __init__(self):
        super(WebView, self).__init__()

        self.channel = QWebChannel()
        self.handler = CallHandler()
        self.channel.registerObject('handler', self.handler)
        self.page().setWebChannel(self.channel)

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
        local_url = QUrl.fromLocalFile(file_path)
        self.load(local_url)


if __name__ == "__main__":
  app = QApplication([])
  view = WebView()
  view.show()
  app.exec_()