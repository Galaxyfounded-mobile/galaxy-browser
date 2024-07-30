import sys
import os
import json
from PyQt5.QtCore import QUrl, QObject, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QToolBar, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWebChannel import QWebChannel

from webhome import get_homepage_html
from settingspage import get_settings_page_html

class WebChannelHandler(QObject):
    @pyqtSlot(str, str, str, list, list)
    def saveSettings(self, searchApi, homepage, theme, bookmarks, plugins):
        # Save settings to file
        settings = {
            'search_api': searchApi,
            'homepage': homepage,
            'theme': theme,
            'bookmarks': bookmarks,
            'plugins': plugins
        }
        with open('settings.json', 'w') as f:
            json.dump(settings, f, indent=4)

class GalaxyBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Galaxy Browser")
        self.setGeometry(100, 100, 1200, 800)
        
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        
        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.perform_search)
        
        self.settings_button = QPushButton('Settings')
        self.settings_button.clicked.connect(self.open_settings)
        
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)
        
        self.load_settings()
        self.setup_toolbar()
        
        self.browser.urlChanged.connect(self.update_url_bar)
        
        # Load the homepage content directly
        self.load_homepage()
        
        # Setup WebChannel
        self.channel = QWebChannel()
        self.web_channel_handler = WebChannelHandler()
        self.channel.registerObject("qt", self.web_channel_handler)
        self.browser.page().setWebChannel(self.channel)
        
    def setup_toolbar(self):
        back_action = QAction(QIcon.fromTheme("go-previous"), "Back", self)
        back_action.triggered.connect(self.browser.back)
        
        forward_action = QAction(QIcon.fromTheme("go-next"), "Forward", self)
        forward_action.triggered.connect(self.browser.forward)
        
        reload_action = QAction(QIcon.fromTheme("view-refresh"), "Reload", self)
        reload_action.triggered.connect(self.browser.reload)
        
        home_action = QAction(QIcon.fromTheme("home"), "Home", self)
        home_action.triggered.connect(self.navigate_home)
        
        self.toolbar.addAction(back_action)
        self.toolbar.addAction(forward_action)
        self.toolbar.addAction(reload_action)
        self.toolbar.addAction(home_action)
        self.toolbar.addWidget(self.url_bar)
        self.toolbar.addWidget(self.search_button)
        self.toolbar.addWidget(self.settings_button)

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())
        
    def navigate_to_url(self):
        text = self.url_bar.text().strip()
        if text.startswith('http://') or text.startswith('https://'):
            q = QUrl(text)
        else:
            q = QUrl(f"http://{text}")
        self.browser.setUrl(q)

    def perform_search(self):
        query = self.url_bar.text().strip()
        if query:
            search_url = f"{self.search_api}?q={query}"
            self.browser.setUrl(QUrl(search_url))

    def navigate_home(self):
        self.load_homepage()

    def open_settings(self):
        settings_html = get_settings_page_html()
        self.browser.setHtml(settings_html)

    def load_homepage(self):
        html_content = get_homepage_html()
        self.browser.setHtml(html_content)

    def load_settings(self):
        settings_file = 'settings.json'
        if os.path.exists(settings_file):
            with open(settings_file, 'r') as f:
                settings = json.load(f)
            self.search_api = settings.get('search_api', 'https://search.brave.com/api/')
            self.homepage = settings.get('homepage', 'webhome.py')
            self.theme = settings.get('theme', 'light')
            self.bookmarks = settings.get('bookmarks', [])
            self.plugins = settings.get('plugins', [])
        else:
            self.search_api = 'https://search.brave.com/api/'
            self.homepage = 'webhome.py'
            self.theme = 'light'
            self.bookmarks = []
            self.plugins = []

    def save_cookies(self):
        cookies = self.browser.page().profile().cookieStore().allCookies()
        with open('galaxycookies.txt', 'w') as f:
            for cookie in cookies:
                f.write(f"{cookie.name()}={cookie.value()}; path={cookie.path()}; domain={cookie.domain()};\n")

    def load_cookies(self):
        if os.path.exists('galaxycookies.txt'):
            with open('galaxycookies.txt', 'r') as f:
                cookies = f.readlines()
                for cookie in cookies:
                    name, rest = cookie.split('=', 1)
                    value, rest = rest.split(';', 1)
                    path, domain = rest.split('path=', 1)[-1].split('domain=', 1)
                    self.browser.page().profile().cookieStore().setCookie(name.strip(), value.strip(), path.strip(), domain.strip())
        else:
            print("No cookies file found.")

def main():
    app = QApplication(sys.argv)
    browser = GalaxyBrowser()
    browser.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
