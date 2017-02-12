import SimpleCV
import json
import os

#for now this will use the HaarCascade method to look for face's

class FaceFinder():
    def __init__(self, config_file = os.path.dirname(os.path.abspath(__file__)) + '/config'):
        _file = open(config_file, 'r')
        _conf = json.loads(_file.read())
        _file.close()

        self.img = _conf['img']
        self.faceTrainer = '/usr/local/lib/python2.7/dist-packages/SimpleCV/Features/HaarCascades/face2.xml'

    def useImgUrl(self, _url):
        self.img = _url

    def setImage(self):
        self.image = SimpleCV.Image(self.img)

    def countFaces(self):
        matches = 0
        facedetect = self.image.findHaarFeatures(self.faceTrainer)
        for faces in facedetect:
            matches += 1
        return matches
