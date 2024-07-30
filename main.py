from browser import GalaxyBrowser
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = GalaxyBrowser()
    browser.show()
    sys.exit(app.exec_())
