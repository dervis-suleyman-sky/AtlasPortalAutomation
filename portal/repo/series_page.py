'''
Created on 25 May 2016

@author: Satish Tailor
'''

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import SendKeys
import os

class SeriesPage(object):
    '''
    classdocs
    '''
    def __init__(self, web_driver):
        '''
        @attention: the web driver
        '''
        self.driver = web_driver.driver
        
    def send_text(self,text):
        actions = ActionChains(self.driver)
        actions.send_keys(text)
        actions.perform()
    
    '''
    Keyboard actions - sends key strokes to an active field 
    '''
    def send_keystrokes(self,text):
        SendKeys.SendKeys(text)
    
    def navigate(self):
        self.driver.get('https://vodportal-test.awf.bskyb.com/#/assets/series')

    def title(self):
        '''wait for all elements to load'''
        h2_elements = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        '''look thorugh all the H2 Tags for Seris'''
        h2_elements = self.driver.find_elements_by_tag_name('h2')
        for h2 in h2_elements:
            if h2.text=='Series':
                return True
        
        
        return False
    
    def button_add_series(self):
        '''wait for all elements to load'''
        button_elements = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'button')))
        '''look thorugh all the button Tags'''
        button_elements = self.driver.find_elements_by_tag_name('button')
        for button in button_elements:
            if button.get_attribute('lx-tooltip')=='Add Series':
                time.sleep(10)
                return button
    
    
    '''Add series pop up'''
    def label_add_series(self):
        '''wait for all elements to load'''
        h2_elements = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        '''search for add series and return True'''
        h2_elements = self.driver.find_elements_by_tag_name('h2')
        for h2 in h2_elements:
            if h2.text=='Add Series':
                return True
            
        return False

    def button_edit_id(self):
        return self.driver.find_element_by_xpath('/html/body/div[4]/md-dialog/md-dialog-content/div/form/div/div[1]/md-icon')
    
    def textfield_id(self):
        time.sleep(2)
        return self.driver.find_element_by_name('seriesId')
    
    '''title'''
    
    def button_expand_title(self):
        #ng-click="vm.advanced.title = !vm.advanced.title"
        span_elements = self.driver.find_elements_by_tag_name('span')
        for span in span_elements:
            if span.get_attribute('ng-click')=='vm.advanced.title = !vm.advanced.title':
                return span
            
        return False

    def textfield_title_brief(self):
        return self.driver.find_element_by_name('titleBrief')
    
    def textfield_title_medium(self):
        return self.driver.find_element_by_name('titleMedium')
    
    def textfield_title_long(self):
        return self.driver.find_element_by_name('titleLong')

    '''expand summary'''
    def button_expand_summary(self):
        #ng-click="vm.advanced.title = !vm.advanced.title"
        span_elements = self.driver.find_elements_by_tag_name('span')
        for span in span_elements:
            if span.get_attribute('ng-click')=='vm.advanced.summary = !vm.advanced.summary':
                return span
            
        return False
   
    def textfield_summary_brief(self):
        return self.driver.find_element_by_name('summaryBrief')
    
    def textfield_summary_short(self):
        return self.driver.find_element_by_name('summaryShort')
    
    def textfield_summary_medium(self):
        return self.driver.find_element_by_name('summaryMedium')
    
    def textfield_summary_long(self):
        return self.driver.find_element_by_name('summaryLong')

    def drop_down_genre(self):
        return self.driver.find_element_by_name('genre')
    
    '''Search through all the md-options to find the genre for the test'''
    def select_genre(self,_genre='Sports:Extreme'):
        #Wait for the drop down to load
        time.sleep(2)
        #Look for all elements with the tag name 'md-option' and store in a list
        element_md_options = self.driver.find_elements_by_tag_name('md-option')
        #loop through the list until you find your rating then click
        for md_option in element_md_options:
            if md_option.text==_genre:
                md_option.click()
                '''If Genre is found click the value'''
                return True
            
        return False
        
    def textfield_studio_display(self):
        return self.driver.find_element_by_name('studioDisplay')

    '''Add image load elements'''

    def upload_image_16by9_1920by1080(self,image):
        '''Need to wait for input dialog to appear'''
        time.sleep(1)
        self.driver.find_element_by_name('LAND_16_9_SERIES').click()
        time.sleep(1)
        self.send_keystrokes(os.path.abspath("")+image)
        '''Simulate the action of pressing enter'''
        SendKeys.SendKeys('{ENTER}')
    
    def upload_image_4by3_1024by730(self,image):
        '''Need to wait for input dialog to appear'''
        time.sleep(1)
        self.driver.find_element_by_name('LAND_N_4_3_SERIES').click()
        time.sleep(1)
        self.send_keystrokes(os.path.abspath("")+image)
        '''Simulate the action of pressing enter'''
        SendKeys.SendKeys('{ENTER}')

    '''Add OK an CANCEL buttons'''

    def button_cancel(self):
        element_buttons = self.driver.find_elements_by_tag_name('button')
        for button in element_buttons:
            if button.get_attribute('aria-label')=='Cancel':
                return button

    def button_ok(self):
        element_buttons = self.driver.find_elements_by_tag_name('button')
        for button in element_buttons:
            if button.get_attribute('aria-label')=='OK':
                return button
