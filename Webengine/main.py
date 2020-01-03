from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import QObject, pyqtSlot, QUrl, QVariant
import os


class WebView(QWebEngineView):

    def __init__(self):
        super(WebView, self).__init__()

        self.channel = QWebChannel()
        self.page().setWebChannel(self.channel)
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
        local_url = QUrl.fromLocalFile(file_path)
        self.load(local_url)


if __name__ == "__main__":
  app = QApplication([])
  view = WebView()
  view.showFullScreen()
  app.exec_()