'''
Created on 12 Apr 2016

@author: Dev2
'''
import time

class AdminToolBar(object):
    '''
    classdocs
    '''

    def __init__(self,web_driver):
        '''
        Constructor
        '''
        self.driver=web_driver.driver
    
    def drop_down_menu_provider(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath('/html/body/div[1]/div/div/md-toolbar/div/md-select/md-select-value/span[2]')
    
    def provider_1(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath('//*[@id="select_option_5"]/div[1]')
    
    def provider_2(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath('//*[@id="select_option_6"]/div[1]')
    
    def provider_3(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath('//*[@id="select_option_7"]/div[1]')
    
    def provider_4(self):
        time.sleep(1)
        return self.driver.find_element_by_xpath('//*[@id="select_option_8"]/div[1]')
    
    def label_recent_media_delivered_from_Test_Provider(self):
        return self.driver.find_element_by_xpath('#//*[@id="admin-panel-content-view"]/div[2]/md-card[1]/md-card-content/h2')
    