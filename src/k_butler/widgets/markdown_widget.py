from PyQt6.QtWebEngineWidgets import QWebEngineView


class TabWidget(QWebEngineView):

    def __init__(self):
        self.page().setWebChannel()

# TODO: https://forum.qt.io/topic/123736/qwebengineview-how-load-local-index-html
