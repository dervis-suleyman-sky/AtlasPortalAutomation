'''
Created on 12 Apr 2016

@author: Dev2
'''

# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
# from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

class LoginPage():
    '''
    classdocs
    '''
    def __init__(self,web_driver):
        '''
        @attention: the web driver
        '''
        self.driver=web_driver.driver
        
    def navigate(self):
        self.driver.get('https://vodportal-test.awf.bskyb.com/#/login')
        
    def title(self):
        #may need a wait condition/function here
        return self.driver.find_element_by_xpath('//*[@id="ui-login"]/div/div/md-card/md-toolbar/div[1]/div/img')
    
    def textfield_username(self):
        return self.driver.find_element_by_xpath('//*[@id="username"]')
   
    def textfield_password(self):
        return self.driver.find_element_by_xpath('//*[@id="password"]')
   
    def button_login(self):
        return self.driver.find_element_by_xpath('//*[@id="ui-login"]/div/div/md-card/md-content/form/button')
    
    def notification_invalid_username_password(self):
        #//*[@id="ui-login"]/div/div/md-card/md-content/form/div/div/div
        return self.driver.find_element_by_xpath('//*[@id="ui-login"]/div/div/md-card/md-content/form/div/div/div')
    
    
    
    