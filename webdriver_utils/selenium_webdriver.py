'''
Created on 17 Feb 2016

@author: Dev2

@note: Install command for python pip install selenium If you want to use Chrome you need to download the latest driver

'''

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

'''
Created on 11 Apr 2016

@author: Dev2
'''
import os

class WebDriver():
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        print(" initialise");
        self.driver=None
        
    '''
    Set to Chrome driver
    '''
    def set_chrome_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        #options.add_argument("user-data-dir=C:\\Path")
        self.driver = webdriver.Chrome(executable_path=os.path.abspath("")+'/chromedriver_win32/chromedriver',chrome_options=options)
        self.driver.implicitly_wait(20)
        
    '''
    Set to Firefox driver
    '''
    def set_firefox_driver(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        
    '''
    Set to IE driver
    '''
    def set_IE_driver(self):
        self.driver = webdriver.Ie('C:/workspace/DebugGUI/chromedriver_win32/chromedriver')
            