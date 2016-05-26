'''
Created on 12 Apr 2016

@author: Dev2
'''

#     # we have to wait for the page to refresh, the last thing that seems to be updated is the title
#     WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
# 
#     # You should see "cheese! - Google Search"
#     print driver.title


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import time

class TitlePage(object):
    '''
    classdocs
    '''
    def __init__(self,web_driver):
        '''
        @attention: the web driver
        '''
        self.driver=web_driver.driver
        
    def navigate(self):
        self.driver.get('https://vodportal-test.awf.bskyb.com/#/adi/new')
        
    def title(self):
        #may need a wait condition/function here
        return self.driver.find_element_by_xpath('//*[@id="admin-panel"]/md-toolbar/div/h2[1]/span/span')
    
    def send_text(self,text):
        actions = ActionChains(self.driver)
        actions.send_keys(text)
        actions.perform()
    
    '''
    @note: Sub Menu lables
    '''
   
    def label_start(self):
        return self.driver.find_element_by_xpath('//*[@id="admin-panel-content-view"]/ui-view/div/div/div/div/md-tabs/md-tabs-wrapper/md-tabs-canvas/md-pagination-wrapper/md-tab-item[1]/span[2]')
    
    def label_title(self): 
        #wait = WebDriverWait(self.driver, 10)
        time.sleep(5)
        #element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="admin-panel-content-view"]/ui-view/div/div/div/div/md-toolbar/div/h2[1]')))
        #WebDriverWait(self.driver, 10)
        return self.driver.find_element_by_xpath('//*[@id="admin-panel-content-view"]/ui-view/div/div/div/div/md-toolbar/div/h2[1]')
    
    def label_video(self):
        return self.driver.find_element_by_xpath('//*[@id="admin-panel-content-view"]/ui-view/div/div/div/div/md-tabs/md-tabs-wrapper/md-tabs-canvas/md-pagination-wrapper/md-tab-item[3]/span[2]')
    
    def label_images_subs(self):
        return self.driver.find_element_by_xpath('//*[@id="admin-panel-content-view"]/ui-view/div/div/div/div/md-tabs/md-tabs-wrapper/md-tabs-canvas/md-pagination-wrapper/md-tab-item[4]/span[2]')
    
    def label_offer(self):
        return self.driver.find_element_by_xpath('//*[@id="admin-panel-content-view"]/ui-view/div/div/div/div/md-tabs/md-tabs-wrapper/md-tabs-canvas/md-pagination-wrapper/md-tab-item[5]/span[2]')
    
    
    '''
    @note: 01 START
    '''
    
    '''
    @note: text fields
    '''
    def textfield_id(self):
        time.sleep(1)
        return self.driver.find_element_by_name('baseId')
    
    def drop_down_channel(self):
        time.sleep(1)
        #Look for all elements with the tag name 'md-option' and store in a list
        element_md_select = self.driver.find_elements_by_tag_name('md-select')
        #loop through the list until you find your rating then click
        for md_select in element_md_select:
            if md_select.get_attribute('aria-label')=='Pick a channel...':
                md_select.click()
                '''If channel is found click the value'''
                return True
            
        return False
    
    '''Select a channel'''
    def select_channel(self,_channel):
        #Wait for the drop down to load
        time.sleep(2)
        #Look for all elements with the tag name 'md-option' and store in a list
        element_md_options = self.driver.find_elements_by_tag_name('md-option')
        #loop through the list until you find your rating then click
        for md_option in element_md_options:
            print md_option.text
            if md_option.text==_channel:
                '''If channel is found click the value'''
                md_option.click()
                '''return true'''
                return True
            
        return False
    
    def textfield_part_series(self):
        return self.driver.find_element_by_xpath('//*[@id="select_12"]')
    
    '''
    @note: Buttons
    '''
    def button_edit_id(self):
        return self.driver.find_element_by_xpath('/html/body/div/div/div/md-content/div/ui-view/div/div/div/div/md-tabs/md-tabs-content-wrapper/md-tab-content[1]/div/div/form/div/div[2]/div[1]/md-icon[2]')
    
    def button_get_new_id(self):
        return self.driver.find_element_by_xpath('//*[@id="tab-content-2"]/div/div/form/div/div[2]/div[1]/md-icon[1]')
    
    def button_previous(self):
        return self.driver.find_element_by_xpath('//*[@id="admin-panel-content-view"]/ui-view/div/div/div/div/div/button[1]/span')
    
    def button_create(self):
        return self.driver.find_element_by_xpath('//*[@id="admin-panel-content-view"]/ui-view/div/div/div/div/div/button[2]')
    
    def button_01_next(self):
        time.sleep(5)
        return self.driver.find_element_by_xpath('/html/body/div/div/div/md-content/div/ui-view/div/div/div/div/div/button[3]')
    
    def button_submit(self):
        return self.driver.find_element_by_xpath('//*[@id="admin-panel-content-view"]/ui-view/div/div/div/div/div/button[4]/md-icon')
    
    
    '''
    @note: 02 TITLE
    '''
    def textfield_title(self):
        time.sleep(2)
        return self.driver.find_element_by_name('titleBrief')
    
    def textfield_summary(self):
        return self.driver.find_element_by_name('summaryBrief')
    
    def textfield_actors(self):
        return self.driver.find_element_by_name('actors')
    
    def textfield_warning(self):
        return self.driver.find_element_by_name('titleWarning')
    
    def textfield_display_runtime(self):
        return self.driver.find_element_by_name('displayRuntime')
    
    '''
    Drop down for Genre
    '''
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
    
    '''rating drop down'''
    def drop_down_rating(self):
        return self.driver.find_element_by_name('rating')
    
    '''Search through all the md-options to find the rating for the test'''
    def select_rating(self,_rating='All Ages'):
        #Wait for the drop down to load
        time.sleep(2)
        #Look for all elements with the tag name 'md-option' and store in a list
        element_md_options = self.driver.find_elements_by_tag_name('md-option')
        #loop through the list until you find your rating then click
        for md_option in element_md_options:
            if md_option.text==_rating:
                md_option.click()
                '''If rating is found click the value'''
                return True
            
        return False
    
    def textfield_broadcast_date(self):
        return self.driver.find_element_by_class_name('md-datepicker-input')
    
    def textfield_production_year(self):
        return self.driver.find_element_by_name('year')
    
    def textfield_studio(self):
        return self.driver.find_element_by_name('studioDisplay')
    
    def button_02_next(self):
        time.sleep(5)
        return self.driver.find_element_by_xpath('/html/body/div[1]/div/div/md-content/div/ui-view/div/div/div/div/div/button[3]')
     
    '''
    @note: 03 VIDEO
    '''

    def drop_down_video_file(self):
        return self.driver.find_element_by_name('media')
    
    '''Search through all the md-options to find the specified media for the test'''
    def select_video(self,media='auto_test_media_asset_01.mxf'):
        #Wait for the drop down to load
        time.sleep(2)
        #Look for all elements with the tag name 'md-option' and store in a list
        element_md_options = self.driver.find_elements_by_tag_name('md-option')
        #loop through the list until you find your rating then click
        for md_option in element_md_options:
            if md_option.text==media:
                md_option.click()
                time.sleep(2)
                '''If media is found click the value'''
                return True
            
        '''If nothing is found return false'''   
        return False
    
    def button_clear_video(self):
        element_md_icons = self.driver.find_elements_by_tag_name('md-icon')
        for md_icon in element_md_icons:
            if md_icon.get_attribute('lx-tooltip')=='Clear video file':
                md_icon.click()
                
                
    def button_next_step(self):
        element_buttons = self.driver.find_elements_by_tag_name('button')
        for button in element_buttons:
            if button.get_attribute('aria-label')=='next step':
                button.click()
        
    '''
    @note: 04 IMAGES & SUBS
    '''
    def button_subtitles(self):
        return self.driver.find_element_by_name('SUBS')
   
    def button_image_16by9_1920by1080(self):
        return self.driver.find_element_by_name('LAND_16_9')
    
    def button_image_4by3_1024by730(self):
        return self.driver.find_element_by_name('LAND_N_4_3')
    
    def button_image_box_art_image_1080by1600(self):
        return self.driver.find_element_by_name('BOXART')
   
    