'''
Created on 12 Apr 2016

@author: Dev2
'''

#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support.ui import Select

import time
import os
import SendKeys

class TitlePage(object):
    '''
    @author: Derivs Suleyman
    @summary: repo contain all the elements from the title page
    '''
    def __init__(self,web_driver):
        '''
        @attention: the web driver
        '''
        self.driver=web_driver.driver
        
    def navigate(self):
        self.driver.get('https://vodportal-stage.awf.bskyb.com/#/adi/new')
        
    def navigate_existing_titles(self):
        self.driver.get('https://vodportal-stage.awf.bskyb.com/#/assets/titles')
        
    def title(self):
        #may need a wait condition/function here
        return self.driver.find_element_by_xpath('//*[@id="admin-panel"]/md-toolbar/div/h2[1]/span/span')
    
    def Label_titles(self):
        #may need a wait condition/function here
        return self.driver.find_element_by_xpath('/html/body/div/div/div/md-toolbar/div/h2/span[2]/span')
    
    def send_text(self,text):
        actions = ActionChains(self.driver)
        actions.send_keys(text)
        actions.perform()
    
    '''
    Keyboard actions - sends key strokes to an active field 
    '''
    def send_keystrokes(self,text):
        SendKeys.SendKeys(text)
        
    '''
    Simulate pressing the enter key
    '''
    def press_enter(self,text):
        actions = ActionChains(self.driver)
        actions.send_keys(text)
        actions.perform()
        
    def press_enter_key(self):
        '''Simulate the action of pressing enter'''
        SendKeys.SendKeys('{ENTER}')
    
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
    
    '''series drop down'''
    def drop_down_series(self):
        #name="series"
        return self.driver.find_element_by_tag_name('series')
    
    '''Select a series'''
    def select_series(self,_series='Friends4'):
        #Wait for the drop down to load
        time.sleep(2)
        #Look for all elements with the tag name 'md-option' and store in a list
        element_md_options = self.driver.find_elements_by_tag_name('md-option')
        #loop through the list until you find your rating then click
        for md_option in element_md_options:
            print md_option.text
            if md_option.text==_series:
                '''If series is found click the value'''
                md_option.click()
                '''return true'''
                return True
            
        return False
    
    
    '''season drop down'''
    def drop_down_season(self):
        return self.driver.find_element_by_tag_name('season')
    
    '''Select a season'''
    def select_season(self,_season='Friends4 season 3'):
        #Wait for the drop down to load
        time.sleep(2)
        #Look for all elements with the tag name 'md-option' and store in a list
        element_md_options = self.driver.find_elements_by_tag_name('md-option')
        #loop through the list until you find your rating then click
        for md_option in element_md_options:
            print md_option.text
            if md_option.text==_season:
                '''If series is found click the value'''
                md_option.click()
                '''return true'''
                return True
            
        return False
    
    def textfield_episode_number(self):
        time.sleep(1)
        return self.driver.find_element_by_name('episodeNumber')
    
    def textfield_total_episode_number(self):
        time.sleep(1)
        return self.driver.find_element_by_name('totalEpisodes')
    
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
                
    '''
    select the options in the radio button fields for audio lang
    '''
                
                
    def button_next_step(self):
        element_buttons = self.driver.find_elements_by_tag_name('button')
        for button in element_buttons:
            if button.get_attribute('aria-label')=='next step':
                button.click()
        
    '''
    @note: 04 IMAGES & SUBS
    '''
    def upload_subtitles(self,subtitle_file):
        '''Need to wait for input dialog to appear'''
        time.sleep(1)
        self.driver.find_element_by_name('SUBS').click()
        time.sleep(5)
        self.send_keystrokes(os.path.abspath("")+subtitle_file)
        '''Simulate the action of pressing enter'''
        SendKeys.SendKeys('{ENTER}')
   
    def upload_image_16by9_1920by1080(self,image):
        '''Need to wait for input dialog to appear'''
        time.sleep(1)
        self.driver.find_element_by_name('LAND_16_9').click()
        time.sleep(1)
        self.send_keystrokes(os.path.abspath("")+image)
        '''Simulate the action of pressing enter'''
        SendKeys.SendKeys('{ENTER}')
    
    def upload_image_4by3_1024by730(self,image):
        '''Need to wait for input dialog to appear'''
        time.sleep(1)
        self.driver.find_element_by_name('LAND_N_4_3').click()
        time.sleep(1)
        self.send_keystrokes(os.path.abspath("")+image)
        '''Simulate the action of pressing enter'''
        SendKeys.SendKeys('{ENTER}')
    
    def upload_image_box_art_image_1080by1600(self,image):
        '''Need to wait for input dialog to appear'''
        time.sleep(1)
        self.driver.find_element_by_name('BOXART').click()
        time.sleep(1)
        self.send_keystrokes(os.path.abspath("")+image)
        '''Simulate the action of pressing enter'''
        SendKeys.SendKeys('{ENTER}')
    
    '''
    @note: 05 OFFER
    '''
    def label_no_offers_defined(self):
        h2_elements = self.driver.find_elements_by_tag_name('h2')
        for h2 in h2_elements:
            if h2.text=='No offers defined':
                return True
            
        return False
        
    def button_add_new_offer(self):
        button_elements = self.driver.find_elements_by_tag_name('button')
        for button in button_elements:
            if button.get_attribute('aria-label')=='add new offer':
                return button
                
    '''
    @note: Pop-up Add new offer
    '''
    def label_add_new_offer(self):
        h2_elements = self.driver.find_elements_by_tag_name('h2')
        for h2 in h2_elements:
            if h2.text=='Add a new offer':
                return True
        
        return False
            
    def drop_down_platform(self):
        return self.driver.find_element_by_name('platform')
    
    '''
    Select Platform e.g. AM,AT,AS the default is AM
    Mobile (AM)
    Tablet (AT)
    '''    
    def select_platform(self,platform='Mobile (AM)'):
        time.sleep(2)
        md_option_elements = self.driver.find_elements_by_tag_name('md-option')
        for md_option in md_option_elements:
            print md_option.text
            if md_option.text==platform:
                return md_option
    
    def radio_button_catchup(self):
        md_radio_button_elements = self.driver.find_elements_by_tag_name('md-radio-button')
        for radio_button in md_radio_button_elements:
            print radio_button.get_attribute('aria-label')
            if radio_button.get_attribute('aria-label')=='Catchup (CUTV)':
                return radio_button.click()
    
    def radio_button_archive(self):
        md_radio_button_elements = self.driver.find_elements_by_tag_name('md-radio-button')
        for radio_button in md_radio_button_elements:
            print radio_button.get_attribute('aria-label')
            if radio_button.get_attribute('aria-label')=='Archive':
                return radio_button.click()
    
    def offer_start_date(self):
        return self.driver.find_element_by_name('startDate')
    
    def offer_end_date(self):
        return self.driver.find_element_by_name('endDate')
    
    def button_cancel(self):
        button_elements = self.driver.find_elements_by_tag_name('button')
        for button in button_elements:
            if button.get_attribute('aria-label')=='Cancel':
                return button
        
    def button_ok(self):
        #return self.driver.find_element_by_xpath('/html/body/div[7]/md-dialog/md-dialog-actions/button[2]')
        button_elements = self.driver.find_elements_by_tag_name('button')
        for button in button_elements:
            print button.text
            print button.get_attribute('aria-label')
            if button.get_attribute('aria-label')=='OK':
                actions = ActionChains(self.driver)
                actions.move_to_element(button)
                actions.click(button)
                actions.perform()
                #return button
   
    def label_atlas_mobile_AM(self):
        h2_elements = self.driver.find_elements_by_tag_name('h2')
        for h2 in h2_elements:
            if h2.get_attribute('aria-label')=='Mobile (AM)':
                return h2
    
    def label_atlas_tablet_AT(self):
        h2_elements = self.driver.find_elements_by_tag_name('h2')
        for h2 in h2_elements:
            if h2.get_attribute('aria-label')=='Tablet (AT)':
                return h2
    
    def label_atlas_set_top_box_AS(self):
        h2_elements = self.driver.find_elements_by_tag_name('h2')
        for h2 in h2_elements:
            if h2.get_attribute('aria-label')=='Tablet (AT)':
                return h2
            
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
    
    
    '''
    Asset Titles Page - Existing titles will be on this page
    '''
    
    
    '''1'''
    def textfield_search(self,title):
        search = self.driver.find_element_by_xpath('/html/body/div/div/div/md-content/div/div/div/md-toolbar/div/form/input')
        search.click()
        search.send_keys(title)
        time.sleep(2)
    
    '''2'''
    def find_title(self,title):
        td_elements = self.driver.find_elements_by_tag_name('td')
        for td_element in td_elements:
            asset_title=td_element.text
            if not asset_title=='':
                return asset_title
        
        return False
    
    '''3'''
    
    '''
    get the state of the first row, should be used along side the search feature
        
        #<span class="ng-isolate-scope" status-icon="SAVED">
        #<span class="ng-isolate-scope" status-icon="NEW_VERSION">
        #<span class="ng-isolate-scope" status-icon="CONTENT_PREP_REQ">
        
    '''
    def get_state(self):
        span_elements = self.driver.find_elements_by_tag_name('span')
        for span_element in span_elements:
            state = span_element.get_attribute('status-icon') 
            if not state==None:
                return state
        
        return False
    
    '''4'''
    def button_menu(self):
        button_elements = self.driver.find_elements_by_tag_name('button')
        for button_element in button_elements:
            if button_element.get_attribute('aria-label')=='Open demo menu':
                return button_element
        
        return False
    
    '''For Update, testing'''
    def button_edit(self):
        button_elements = self.driver.find_elements_by_tag_name('button')
        for button_element in button_elements:
            if button_element.get_attribute('aria-label')=='Edit':
                return button_element
        
        return False
    
    
    def button_new_version(self):
        button_elements = self.driver.find_elements_by_tag_name('button')
        for button_element in button_elements:
            if button_element.get_attribute('aria-label')=='New version':
                return button_element
        
        return False
    
    
    def button_new_version_and_edit(self):
        button_elements = self.driver.find_elements_by_tag_name('button')
        for button_element in button_elements:
            if button_element.get_attribute('aria-label')=='New version and edit':
                return button_element
        
        return False
    
    def button_save(self):
        button_elements = self.driver.find_elements_by_tag_name('button')
        for button_element in button_elements:
            if button_element.get_attribute('aria-label')=='save':
                return button_element
        
        return False
    