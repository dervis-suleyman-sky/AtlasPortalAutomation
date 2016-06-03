'''
Created on 24 May 2016

@author: Satish Tailor
'''
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import SendKeys
import os

class SeasonsPage(object):
    '''
    @summary: Element repo for season page
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
        self.driver.get('https://vodportal-test.awf.bskyb.com/#/assets/seasons')

    def title(self):
        '''wait for all elements to load'''
        h2_elements = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        '''look thorugh all the H2 Tags for Seasons'''
        h2_elements = self.driver.find_elements_by_tag_name('h2')
        for h2 in h2_elements:
            if h2.text=='Seasons':
                return True
        
        return False
    
    def button_add_season(self):
        '''wait for all elements to load'''
        button_elements = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'button')))
        '''look thorugh all the button Tags'''
        button_elements = self.driver.find_elements_by_tag_name('button')
        for button in button_elements:
            if button.get_attribute('lx-tooltip')=='Add Season':
                time.sleep(10)
                return button
    
    
    '''Add season pop up'''
    def label_add_season(self):
        '''wait for all elements to load'''
        h2_elements = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        '''search for add series and return True'''
        h2_elements = self.driver.find_elements_by_tag_name('h2')
        for h2 in h2_elements:
            if h2.text=='Add Season':
                return True
            
        return False
    
    '''drop down add series'''
   
    def drop_down_series(self):
        return self.driver.find_element_by_name('series')
    
    def select_series(self,_series='Friends3'):
        #Wait for the drop down to load
        time.sleep(2)
        #Look for all elements with the tag name 'md-option' and store in a list
        element_md_options = self.driver.find_elements_by_tag_name('md-option')
        #loop through the list until you find your rating then click
        for md_option in element_md_options:
            if md_option.text==_series:
                md_option.click()
                '''If Genre is found click the value'''
                return True
            
        return False

    '''
    @summary: Search through all the tags containing MD_ICON
    '''
    def button_edit_id(self):
        #Wait for the drop down to load
        time.sleep(2)
        #Look for all elements with the tag name 'md-option' and store in a list
        element_md_icons = self.driver.find_elements_by_tag_name('md-icon')
        #loop through the list until you find your rating then click
        for md_icon in element_md_icons:
            if md_icon.get_attribute('lx-tooltip')=='Leave this on auto if you would like the system to generate a series ID for you':
                return md_icon
            
        return False
    
    def textfield_id(self):
        time.sleep(2)
        return self.driver.find_element_by_name('seasonId')
    
    '''title'''
    
    def button_expand_title(self):
        #ng-click="vm.advanced.title = !vm.advanced.title"
        span_elements = self.driver.find_elements_by_tag_name('span')
        for span in span_elements:
            if span.get_attribute('ng-click')=='vm.advanced.title = !vm.advanced.title':
                return span
            
        return False

    def textfield_title_brief(self):
        return self.driver.find_element_by_name('seasonBrief')
    
    def textfield_title_medium(self):
        return self.driver.find_element_by_name('seasonMedium')
    
    def textfield_title_long(self):
        return self.driver.find_element_by_name('seasonLong')

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

    def textfield_season_number(self):
        return self.driver.find_element_by_name('seasonNum')
    
    def textfield_total_episodes(self):
        return self.driver.find_element_by_name('totalEpisodes')
    
    def textfield_production_year(self):
        return self.driver.find_element_by_name('year')

    '''Add image load elements'''

    def upload_image_16by9_1920by1080(self,image):
        '''Need to wait for input dialog to appear'''
        time.sleep(1)
        self.driver.find_element_by_name('LAND_16_9_SEASON').click()
        time.sleep(1)
        self.send_keystrokes(os.path.abspath("")+image)
        '''Simulate the action of pressing enter'''
        SendKeys.SendKeys('{ENTER}')
    
    def upload_image_4by3_1024by730(self,image):
        '''Need to wait for input dialog to appear'''
        time.sleep(1)
        self.driver.find_element_by_name('LAND_N_4_3_SEASON').click()
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

    def find_season(self,season_name):
        element_td_tags = self.driver.find_elements_by_tag_name('td')
        for td in element_td_tags:
            if td.text==season_name:
                return td
            
        return False
            
    def button_incon_delete_season(self):
        element_buttons = self.driver.find_elements_by_tag_name('button')
        for button in element_buttons:
            if button.get_attribute('aria-label')=='delete season':
                return button
            
            
    '''Pop up delete'''
    def label_delete_season(self):
        '''wait for all elements to load'''
        h2_elements = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        '''search for Pop up title and return True'''
        h2_elements = self.driver.find_elements_by_tag_name('h2')
        for h2 in h2_elements:
            if h2.text=='Delete Season':
                return True
            
        return False
    
    
    def button_delete_season_ok(self):
        element_buttons = self.driver.find_elements_by_tag_name('button')
        for button in element_buttons:
            if button.get_attribute('aria-label')=='OK':
                return button
    
    def button_delete_season_cancel(self):
        element_buttons = self.driver.find_elements_by_tag_name('button')
        for button in element_buttons:
            if button.get_attribute('aria-label')=='Cancel':
                return button
    '''
    @author: Dervis Suleyman
    @summary: clicks the drop down on the series page and selects a number of rows to be visible
    '''
    def set_row_number(self,row_number):
        md_select_elements = self.driver.find_elements_by_tag_name('md-select')
        for select in md_select_elements:
            if select.get_attribute('aria-label')=='Rows: 10':
                select.click()
                time.sleep(1)
                div_elements = self.driver.find_elements_by_tag_name('div')
                for div in div_elements:
                    if(div.text==row_number):
                        div.click()
                        time.sleep(2)
