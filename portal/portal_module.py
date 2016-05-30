'''
Created on 2 May 2016

@author: Dev2
'''

from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from webdriver_utils.selenium_webdriver import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from isilon.isilon_ftp_helper import IsilonHelper
import time

'''
@note: Repo imports
'''
from portal.repo.login_page import LoginPage
from portal.repo.dashboard_page import DashBoardPage
from portal.repo.titles_page import TitlePage
from portal.repo.side_navigation_bar import SideNavigationBar
from portal.repo.admin_toolbar import AdminToolBar
from portal.repo.media_page import MediaPage
from portal.repo.seasons_page import SeasonsPage
from portal.repo.series_page import SeriesPage


class Portal(object):

    def __init__(self):
        pass
        
    def navigate_to_login_page(self,webdriver):
        #call the login repo page
        loginPage = LoginPage(webdriver)
        #navigate to the login page and verify the page has loaded
        loginPage.navigate()
        return loginPage.title().is_displayed()
    
    def login(self,webdriver,username="Dervis_superuser",password="test1234"):
        loginPage = LoginPage(webdriver)
        assert self.navigate_to_login_page(webdriver)
        #Enter the user name
        loginPage.textfield_username().click()
        loginPage.textfield_username().send_keys(username)
        #Enter the Password
        loginPage.textfield_password().click()
        loginPage.textfield_password().send_keys(password)
        #Login to the portal
        loginPage.button_login().click()
          
        #Check the user has logged into the portal
        dashboard = DashBoardPage(webdriver)
        #The elemenent if login is invalid will not be found so a try catch statement will handle this and return false  
        try:
            #need to have a wait - also need to ensure the screen is full screen   
            '''
            @note: This is_displayed() only confirms the element is visible to the user on the page.
            '''
            return dashboard.label_dashboard().is_displayed()
        except NoSuchElementException as e:
            print e
            return False

    '''
    Satish Tailor: Added logout()
    '''
    def logout(self,webdriver):
        #call the admin_toolbar repo page
        loginPage = LoginPage(webdriver)
        admintoolbar = AdminToolBar(webdriver)
        #navigate to the login page and verify the page has loaded
        admintoolbar.button_user().click()
        admintoolbar.button_logout().click()
        return loginPage.title().is_displayed()
    
    '''
    Set the provider to either 1,2,3 or 4 you will need to add providers here
    '''
    def set_provider(self,webdriver,provider=1):
        
        admintoolbar = AdminToolBar(webdriver)
        
        import time
        
        time.sleep(1)
        admintoolbar.drop_down_menu_provider().click()
        time.sleep(2)
        
        '''switch providers integer values'''
        if(provider==1):
            admintoolbar.provider_1().click()
            
        if(provider==2):
            admintoolbar.provider_2().click()
            
        if(provider==3):
            admintoolbar.provider_3().click()
            
        if(provider==4):
            admintoolbar.provider_4().click()
            
        time.sleep(1)
    
    '''
    @author: Dervis Suleyman
    @note: creating a new title e.g. non-episodic
    '''
    def navigate_to_create_new_title_page(self,webdriver,isURL=True):
        titlePage = TitlePage(webdriver)
        time.sleep(2)
        #if URL is true navigate using the browser URL
        if(isURL):
            titlePage.navigate()
        else:
            sideNav = SideNavigationBar(webdriver)
            sideNav.button_create_new_title().click()
        
        try:
            #need to have a wait - also need to ensure the screen is full screen   
            '''
            @note: This is_displayed() only!! confirms the element is visible to the user on the page.
            '''
            
            return titlePage.label_title().is_displayed()
        
        except NoSuchElementException as e:
            print e
            return False

    '''
    @author: Satish Tailor
    @note: navigating to seasons page
    '''
    def navigate_to_seasons_page(self,webdriver,isURL=True):
        seasonsPage = SeasonsPage(webdriver)

        #if URL is true navigate using the browser URL
        if(isURL):
            seasonsPage.navigate()
        else:
            pass
            #sideNav = SideNavigationBar(webdriver)
            #sideNav.button_create_new_title().click()

        try:
            #need to have a wait - also need to ensure the screen is full screen
            '''
            @note: This is_displayed() only!! confirms the element is visible to the user on the page.
            '''

            return seasonsPage.title()

        except NoSuchElementException as e:
            print e
            return False
        
    '''
    @author: Dervis Suleyman
    @note: navigating to series page
    '''
    def navigate_to_series_page(self,webdriver,isURL=True):
        seriesPage = SeriesPage(webdriver)

        #if URL is true navigate using the browser URL
        if(isURL):
            seriesPage.navigate()
        else:
            pass
            #sideNav = SideNavigationBar(webdriver)
            #sideNav.button_create_new_title().click()

        try:
            #need to have a wait - also need to ensure the screen is full screen
            '''
            @note: This is_displayed() only!! confirms the element is visible to the user on the page.
            '''

            return seriesPage.title()

        except NoSuchElementException as e:
            print e
            return False
    

    '''
    @author: Dervis Suleyman
    @summary: Send a new MXF to the drop zone, then create a new non-episodic asset
    
    Test Data:
        
        portal_asset={'asset_id':'123456789012311',
                      'channel':'Test Channel 2',
                      'series':'Friends4',
                      'season':'Friends4 season 3',
                      'episodeNumber':'1',
                      'TotalEpisodes':'50',
                      'Title':'Some Title',
                      'Summary':'Some Summary',
                      'Actors':'Dervis Suleyman',
                      'Warning':'This movie may contain flashing images',
                      'DisplayRuntime':'0:20',
                      'Genre':'Specialist:Adult',
                      'Rating':'All Ages',
                      'BroadcastDate':'03/05/2016',
                      'ProductionYear':'1990',
                      'Studio':'Some Studio Code',
                      'VideoFile':'auto_test_media_asset_01.mxf',
                      'SubTitles':'\\isilon\\subtitles\\SBC073608_1.stl',
                      '16-9-image':'\\isilon\\test_images\\1167563-LAND_16_9.jpg',
                      '4-3-image':'\\isilon\\test_images\\1167563-LAND_N_4_3.jpg',
                      'Boxart-image':'\\isilon\\test_images\\BOXART.jpg'}
        
    
    Test data for offers:

        offers=[]
        offers.append({'offer':{'Platform':'AM','Type':'Archive','StartDate':'24 May 2016, 13:58','EndDate':'30 May 2016, 13:58'}})
        offers.append({'offer':{'Platform':'AT','Type':'Archive','StartDate':'24 May 2016, 13:58','EndDate':'30 May 2016, 13:58'}})
        offers.append({'offer':{'Platform':'AS','Type':'Archive','StartDate':'24 May 2016, 13:58','EndDate':'30 May 2016, 13:58'}})
        
    
    '''
    def create_new_title(self,webdriver,portal_asset,offers):
        '''Check channel exists else create new channel'''
        '''Before test create and upload a new MXF with a unique name'''
        titlePage = TitlePage(webdriver)
        #Navigate to the page
        assert self.navigate_to_create_new_title_page(webdriver,True)
        time.sleep(1)
        #start with 01
        titlePage.button_edit_id().click()
        titlePage.textfield_id().click()
        titlePage.textfield_id().clear()
        titlePage.textfield_id().send_keys(portal_asset['asset_id'])
        
        '''Click drop down for channel and select '''
        titlePage.drop_down_channel()
        titlePage.select_channel(portal_asset['channel'])
        
        #move onto 02
        titlePage.button_01_next().click()
        
        titlePage.textfield_title().click()
        titlePage.textfield_title().send_keys(portal_asset['Title'])
        
        titlePage.textfield_summary().click()
        titlePage.textfield_summary().send_keys(portal_asset['Summary'])
        
        titlePage.textfield_actors().click()
        titlePage.send_text(portal_asset['Actors'])
        
        titlePage.textfield_warning().click()
        titlePage.textfield_warning().send_keys(portal_asset['Warning'])
        
        titlePage.textfield_display_runtime().click()
        titlePage.textfield_display_runtime().send_keys(portal_asset['DisplayRuntime'])
    
        '''Drop down for Genre'''
        titlePage.drop_down_genre().click()
        titlePage.select_genre(portal_asset['Genre'])
        
        '''drop down rating'''
        titlePage.drop_down_rating().click()
        titlePage.select_rating(portal_asset['Rating'])
        
        titlePage.textfield_broadcast_date().click()
        titlePage.textfield_broadcast_date().send_keys(portal_asset['BroadcastDate'])
        
        titlePage.textfield_production_year().click()
        titlePage.textfield_production_year().send_keys(portal_asset['ProductionYear'])
        
        titlePage.textfield_studio().click()
        titlePage.textfield_studio().send_keys(portal_asset['Studio'])
        
        titlePage.button_02_next().click()
        time.sleep(5)
        
        
        #Move onto 03 - select the video
        '''
        @note: You cannot select Audio Lang until you have chosen the channel on the first tab of title
        '''
        
        '''drop down media asset'''
        titlePage.drop_down_video_file().click()
        titlePage.select_video(portal_asset['VideoFile'])
        
        '''Button next step has click built into the function'''
        titlePage.button_next_step()
        
        #Move onto 04 - images & subs
        '''Upload a .stl the location must be within the project'''
        titlePage.upload_subtitles(portal_asset['SubTitles'])
        titlePage.upload_image_16by9_1920by1080(portal_asset['16-9-image'])
        titlePage.upload_image_4by3_1024by730(portal_asset['4-3-image'])
        titlePage.upload_image_box_art_image_1080by1600(portal_asset['Boxart-image'])
        time.sleep(2)
        
        '''Button next step has click built into the function'''
        titlePage.button_next_step()
        
        #Move onto 05 - offer
        assert titlePage.label_no_offers_defined()
        '''offers will need to go under a loop'''
        titlePage.button_add_new_offer().click()
        assert titlePage.label_add_new_offer()
        titlePage.drop_down_platform().click()
        titlePage.select_platform(platform='Tablet (AT)').click()
        titlePage.radio_button_archive()
        titlePage.radio_button_catchup()
        
        #http://stackoverflow.com/questions/30469419/fire-ng-change-of-angular-page-using-selenium
        titlePage.offer_start_date().click()
#         time.sleep(5)
#         titlePage.button_test()
        time.sleep(2)
        titlePage.button_ok()
        time.sleep(2)
        titlePage.button_ok()
        time.sleep(2)
        titlePage.button_ok()
        
        time.sleep(30)
        
        #.send_keys('27 May 2016, 15:06')
        #titlePage.offer_end_date().click()
        #.send_keys('31 May 2016, 15:06')
        #titlePage.button_ok().click()
    
    '''
    Navigate to the media file page check for media asset, if not present add media asset
    '''
    def navigate_to_media_page(self,webdriver,isURL=True):
        mediaPage=MediaPage(webdriver)
        #if URL is true navigate using the browser URL
        if(isURL):
            mediaPage.navigate()
        else:
            sideNav = SideNavigationBar(webdriver)
            sideNav.button_create_new_title().click()
        try:
            #need to have a wait - also need to ensure the screen is full screen   
            '''
            @note: This is_displayed() only!! confirms the element is visible to the user on the page.
            '''
            
            return mediaPage.label_media().is_displayed()
        
        except NoSuchElementException as e:
            print e
            return False
    
    '''
    Check Media Files are present in the correct drop zone
    '''
    def check_media_content_is_present(self,
                                       webdriver,
                                       content=None,
                                       content_file_path='C:\\workspace\\AtlasPortalAutomation\\isilon\\test_media',
                                       destination_folder='/mnt/dmz/atlas_provider_1/'):
        
        '''Navigate to the Media page '''
        assert self.navigate_to_media_page(webdriver)
        
        '''check media is present else add new media'''
        for mxf in content:

            '''check mxf/media assets are present on the portal'''
            isPresent=False
            
            '''Only execute the following code block if the media assets are not present'''
            if(not isPresent):
                '''Add drop the content into the correct location and wait 5 mins'''
                try:
                    #build the local file path location
                    #print content_file_path+'\\'+ mxf+'.mxf'
                    connection = IsilonHelper()
                    _sftp = connection.secure_FTP(destination_folder)
                         
                    '''
                    @note: Will need to check the Portal to verify if the assets exist
                    '''
                    if(not connection.file_exists(_sftp, content_file_path+'\\'+ mxf+'.mxf')):
                        assert connection.send(_sftp,content_file_path+'\\'+ mxf+'.mxf')
                    
                except Exception as e:
                    print e
            
            
        '''Return overall result - success message all content has been pushed to the isilon'''
        return True
    
    
    '''create season function'''
    
    '''
            season_info = {'SeasonID':'SEA__test12345',
                       'Series':'Friends4',
                       'TitleBrief':'Title brief',
                       'TitleMedium':'Title medium',
                       'TitleLong':'Long',
                       'SummaryBrief':'brief',
                       'SummaryShort':'short',
                       'SummaryMedium':'med',
                       'SummaryLong':'long',
                       'SeasonNumber':'1',
                       'TotalEpisodes':'21',
                       'ProductionYear':'1990',
                       '16x9 image':'\\isilon\\test_images\\1167563-LAND_16_9.jpg',
                       '4x3 image':'\\isilon\\test_images\\1167563-LAND_N_4_3.jpg'}
    '''   
    def create_new_season(self,webdriver,season_info):
        seasonPage = SeasonsPage(webdriver)
        self.navigate_to_seasons_page(webdriver)
        seasonPage.button_add_season().click()
        assert seasonPage.label_add_season()
        
        '''series drop down'''
        seasonPage.drop_down_series().click()
        seasonPage.select_series(season_info['Series'])
        time.sleep(2)
        
        '''Enter season id if given'''
        if(not season_info['SeasonID']==''):
            seasonPage.button_edit_id().click()
            seasonPage.textfield_id().send_keys(season_info['SeasonID'])
            
        time.sleep(1)
        seasonPage.button_expand_title().click()
        seasonPage.textfield_title_brief().send_keys(season_info['TitleBrief'])
        seasonPage.textfield_title_medium().send_keys(season_info['TitleMedium'])
        seasonPage.textfield_title_long().send_keys(season_info['TitleLong'])
        seasonPage.button_expand_summary().click()
        seasonPage.textfield_summary_brief().send_keys(season_info['SummaryBrief'])
        seasonPage.textfield_summary_short().send_keys(season_info['SummaryShort'])
        seasonPage.textfield_summary_medium().send_keys(season_info['SummaryMedium'])
        seasonPage.textfield_summary_long().send_keys(season_info['SummaryLong'])
        
        '''
        Season specific info
        '''
        seasonPage.textfield_season_number().send_keys(season_info['SeasonNumber'])
        seasonPage.textfield_total_episodes().send_keys(season_info['TotalEpisodes'])
        seasonPage.textfield_production_year().send_keys(season_info['ProductionYear'])
        
        '''
        @note: Upload images
        '''
        seasonPage.upload_image_16by9_1920by1080(season_info['16x9 image'])
        seasonPage.upload_image_4by3_1024by730(season_info['4x3 image'])
        
        
        '''click ok and create the series'''
        seasonPage.button_ok().click()
            
        #Temp wait
        time.sleep(5)
        
    
    '''create series function'''
    '''
            series_info = {'SeriesID':'12345678901234567892',
                       'TitleBrief':'Title brief',
                       'TitleMedium':'Title medium',
                       'TitleLong':'Long',
                       'SummaryBrief':'brief',
                       'SummaryShort':'short',
                       'SummaryMedium':'med',
                       'SummaryLong':'long',
                       'Genre':'genre',
                       'StudioDisplay':'studio',
                       '16x9 image':'\\isilon\\test_images\\1167563-LAND_16_9.jpg',
                       '4x3 image':'\\isilon\\test_images\\1167563-LAND_N_4_3.jpg'}
    '''       
    def create_new_series(self,webdriver,series_info):
        seriesPage = SeriesPage(webdriver)
        assert self.navigate_to_series_page(webdriver)
        seriesPage.button_add_series().click()
        '''Pop up'''
        assert seriesPage.label_add_series()
        
        
        '''Enter series id if given'''
        if(not series_info['SeriesID']==''):
            seriesPage.button_edit_id().click()
            seriesPage.textfield_id().send_keys(series_info['SeriesID'])
        
        time.sleep(1)
        seriesPage.button_expand_title().click()
        seriesPage.textfield_title_brief().send_keys(series_info['TitleBrief'])
        seriesPage.textfield_title_medium().send_keys(series_info['TitleMedium'])
        seriesPage.textfield_title_long().send_keys(series_info['TitleLong'])
        seriesPage.button_expand_summary().click()
        seriesPage.textfield_summary_brief().send_keys(series_info['SummaryBrief'])
        seriesPage.textfield_summary_short().send_keys(series_info['SummaryShort'])
        seriesPage.textfield_summary_medium().send_keys(series_info['SummaryMedium'])
        seriesPage.textfield_summary_long().send_keys(series_info['SummaryLong'])
        '''select a genre'''
        seriesPage.drop_down_genre().click()
        time.sleep(2)
        seriesPage.select_genre(series_info['Genre'])
        
        seriesPage.textfield_studio_display().send_keys(series_info['StudioDisplay'])
        '''
        @note: Upload images
        '''
        seriesPage.upload_image_16by9_1920by1080(series_info['16x9 image'])
        seriesPage.upload_image_4by3_1024by730(series_info['4x3 image'])
        
        
        '''click ok and create the series'''
        seriesPage.button_ok().click()
            
        #Temp wait
        time.sleep(5)
        
    
    '''create channel function'''       
    def create_new_channel(self,webdriver):
        pass
    
    '''create provider function'''
    def create_new_provider(self,webdriver):
        pass

    '''create user function'''

    def create_new_user(self, webdriver):
        pass
