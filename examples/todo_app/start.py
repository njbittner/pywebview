import os
import webview

"""
An example of serverless app architecture using webview.start() function
"""


class Api():
    def addItem(self, title):
        print('Added item %s' % title)

    def removeItem(self, item):
        print('Removed item %s' % item)

    def editItem(self, item):
        print('Edited item %s' % item)

    def toggleItem(self, item):
        print('Toggled item %s' % item)


if __name__ == '__main__':
    api = Api()
    webview.start('Todos magnificos', 'assets/index.html', js_api=api, options={'min_size': (600, 450)})

