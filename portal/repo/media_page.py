'''
Created on 12 Apr 2016

@author: Dev2
'''
from portal.config_module import PortalConfig

class MediaPage(object):

    def __init__(self,web_driver):
        '''
        @attention: the web driver
        '''
        self.driver=web_driver.driver
        config=PortalConfig()
        self.driver=web_driver.driver
        self.url=config.url()+'/#/media'
        
    def navigate(self):
        self.driver.get(self.url)
        #self.driver.get('https://vodportal-stage.awf.bskyb.com/#/media')
        
    def label_media(self):
        return self.driver.find_element_by_xpath('//*[@id="admin-panel"]/md-toolbar/div/h2/span/span')         