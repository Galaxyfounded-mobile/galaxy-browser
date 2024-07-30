from PyQt5.QtWidgets import QPushButton, QToolBar, QAction, QMenuBar
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, Qt

def create_buttons(navigate_func, bookmark_func, custom_site_func):
    search_button = QPushButton("Search")
    search_button.setIcon(QIcon("icons/search.png"))
    search_button.setStyleSheet("background-color: #007BFF; color: white; border-radius: 5px; padding: 5px;")
    search_button.clicked.connect(navigate_func)

    bookmark_button = QPushButton("Bookmark")
    bookmark_button.setIcon(QIcon("icons/bookmark.png"))
    bookmark_button.setStyleSheet("background-color: #28A745; color: white; border-radius: 5px; padding: 5px;")
    bookmark_button.clicked.connect(bookmark_func)

    custom_site_button = QPushButton("Custom Site")
    custom_site_button.setIcon(QIcon("icons/custom_site.png"))
    custom_site_button.setStyleSheet("background-color: #FFC107; color: white; border-radius: 5px; padding: 5px;")
    custom_site_button.clicked.connect(custom_site_func)

    return search_button, bookmark_button, custom_site_button

def setup_toolbar(toolbar, browser):
    back_action = QAction(QIcon("icons/back.png"), "Back", browser)
    back_action.setToolTip("Go Back")
    back_action.triggered.connect(browser.browser.back)

    forward_action = QAction(QIcon("icons/forward.png"), "Forward", browser)
    forward_action.setToolTip("Go Forward")
    forward_action.triggered.connect(browser.browser.forward)

    reload_action = QAction(QIcon("icons/reload.png"), "Reload", browser)
    reload_action.setToolTip("Reload Page")
    reload_action.triggered.connect(browser.browser.reload)

    home_action = QAction(QIcon("icons/home.png"), "Home", browser)
    home_action.setToolTip("Home Page")
    home_action.triggered.connect(browser.go_home)

    toolbar.addAction(back_action)
    toolbar.addAction(forward_action)
    toolbar.addAction(reload_action)
    toolbar.addAction(home_action)
    toolbar.setStyleSheet("background-color: #343A40;")  # Toolbar color

def setup_menubar(browser, menubar):
    settings_action = QAction(QIcon("icons/settings.png"), "Settings", browser)
    settings_action.setToolTip("Open Settings")
    settings_action.triggered.connect(browser.open_settings_dialog)

    file_menu = menubar.addMenu("File")
    file_menu.addAction(settings_action)

def setup_styles(browser):
    browser.setStyleSheet("""
        QMainWindow {
            background-color: #F8F9FA;  # Main window background color
        }
        QLineEdit {
            border: 1px solid #CED4DA;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton {
            border: 1px solid #CED4DA;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #0056b3;
        }
    """)
