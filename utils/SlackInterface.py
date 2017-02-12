from slackclient import SlackClient
from datetime import datetime
import json
import os

class SlackInterface():
    def __init__(self, config_file = os.path.dirname(os.path.abspath(__file__)) + '/config'):

        _file = open(config_file, 'r')
        _conf = json.loads(_file.read())
        _file.close()

        self.sclient = SlackClient(_conf['token'])
        self.channel = _conf['channel']


    def updateImgUrl(self):
        
        history = self.sclient.api_call( 
                "channels.history",
                channel=self.channel
            )

        # the second iteration contains the front room url
        imgurl = history['messages'][1]['text']
        imgurl = imgurl.split('<')[1]
        imgurl = imgurl.split('>')[0]
        self.imgurl = imgurl

    
        timestamp = float(history['messages'][1]['ts'])
        self.timestamp = datetime.fromtimestamp(timestamp)
        
        return self.imgurl

    def getUrl(self):
        return self.imgurl

    def getTimeStamp(self):
        return self.timestamp

if __name__ == '__main__':
    example = SlackInterface()
    print example.updateImgUrl()
