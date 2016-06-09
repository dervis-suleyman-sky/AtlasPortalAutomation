'''
Created on 12 Apr 2016

@author: Dev2
'''

from portal.config_module import PortalConfig

class DashBoardPage(object):

    def __init__(self,web_driver):
        config=PortalConfig()
        self.driver=web_driver.driver
        self.url=config.url()+'/#/dashboard'
        
    def navigate(self):
        self.driver.get(self.login_url)
        
    def label_dashboard(self):
        return self.driver.find_element_by_xpath('//*[@id="admin-panel"]/md-toolbar/div/h2[1]/span/span')
    
    def widget_unattached_media(self):
        return self.driver.find_element_by_xpath('//*[@id="admin-panel-content-view"]/div[1]/div/div[1]/div[1]')
    
    def widget_unattached_titles(self):
        return self.driver.find_element_by_xpath('//*[@id="admin-panel-content-view"]/div[1]/div/div[2]/div[1]/div[2]')
    
    def widget_in_progress(self):
        return self.driver.find_element_by_xpath('//*[@id="admin-panel-content-view"]/div[1]/div/div[3]/div[1]')
    
    def widget_requiring_attention(self):
        return self.driver.find_element_by_xpath('//*[@id="admin-panel-content-view"]/div[1]/div/div[4]/div[1]')
        