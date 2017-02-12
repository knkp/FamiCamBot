from utils.SlackInterface import SlackInterface
from utils.FaceFinder import FaceFinder
import urllib2
import os
import json

class App():
    def __init__(self, config_file = os.path.dirname(os.path.abspath(__file__)) + '/utils/config'):

        _file = open(config_file, 'r')
        _conf = json.loads(_file.read())
        _file.close()

        self.img = _conf['img']
        self.si = SlackInterface()
        self.ff = FaceFinder()
        self.url = ''
        self.facecount = 0

    def doAllTheThings(self):
        self.updateUrl()
        #self.updateTempImg()
        self.countTheFaces()
        print self.facecount
    

    def updateUrl(self):
        self.url = self.si.updateImgUrl()
        self.ff.useImgUrl(self.url)
        self.ff.setImage()

    def updateTempImg(self):
        tmpimg = open(self.img, 'w')
        response = urllib2.urlopen(self.url)
        content = response.read()
        tmpimg.write(content)
        tmpimg.close()
        response.close()

    def countTheFaces(self):
        self.facecount = self.ff.countFaces()


if __name__ == '__main__':
    app = App()
    app.doAllTheThings()
