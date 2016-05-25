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
#         try:
#             return self.driver.find_element_by_xpath('//*[@id="input_19"]')
#         except ElementNotVisibleException as e:
#             print e
        time.sleep(1)
        return self.driver.find_element_by_name('baseId')
    
    def textfield_channel(self):
        return self.driver.find_element_by_xpath('//*[@id="select_10"]')
    
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
    
    def genre_free_preview(self):
        return self.driver.find_element_by_xpath('/html/body/div[3]/md-select-menu/md-content/md-option[2]/div[1]')
    
    def genre_entertainment_action(self):
        return self.driver.find_element_by_xpath('/html/body/div[3]/md-select-menu/md-content/md-option[18]/div[1]')
    
    def genre_Undefined_Undefined(self):
        return self.driver.find_element_by_xpath('/html/body/div[3]/md-select-menu/md-content/md-option[1]')
    
    '''rating drop down'''
    def drop_down_rating(self):
        return self.driver.find_element_by_name('rating')
    
    def rating_all_ages(self):
        return self.driver.find_element_by_xpath('/html/body/div[4]/md-select-menu/md-content/md-option[2]/div[1]')
    
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
    
    '''
    @note: 04 IMAGES & SUBS
    '''
    def button_subtitles(self):
        return self.driver.find_element_by_xpath('//*[@id="tab-content-5"]/div/md-content/form/div/div[2]/div/div[1]/button')
   
    def button_image_16by9_1920by1080(self):
        return self.driver.find_element_by_xpath('//*[@id="tab-content-5"]/div/md-content/form/div/div[2]/div/div[2]/md-card[1]/md-card-actions/button/i')
    
    def button_image_4by3_1024by730(self):
        return self.driver.find_element_by_xpath('//*[@id="tab-content-5"]/div/md-content/form/div/div[2]/div/div[2]/md-card[2]/md-card-actions/button')
    
    def button_image_box_art_image_1080by1600(self):
        return self.driver.find_element_by_xpath('//*[@id="tab-content-5"]/div/md-content/form/div/div[2]/div/div[2]/md-card[3]/md-card-actions/button')
   
   
    