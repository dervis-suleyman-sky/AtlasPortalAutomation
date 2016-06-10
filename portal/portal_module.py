#-*- coding: utf-8 -*-
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
from portal.repo.users_page import UsersPage

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
            #print e
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
            #print e
            return False
        
            '''
    @author: Dervis Suleyman
    @note: navigates to the existing title page
    '''
    def navigate_to_title_page(self,webdriver,isURL=True):
        titlePage = TitlePage(webdriver)
        time.sleep(2)
        #if URL is true navigate using the browser URL
        if(isURL):
            titlePage.navigate_existing_titles()
        else:
            '''
            @todo: Add side nav functionality
            '''
            pass
            #sideNav = SideNavigationBar(webdriver)
            #sideNav.button_create_new_title().click()

        try:
            #need to have a wait - also need to ensure the screen is full screen
            '''
            @note: This is_displayed() only!! confirms the element is visible to the user on the page.
            '''

            return titlePage.Label_titles().is_displayed()

        except NoSuchElementException as e:
            #print e
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
            #print e
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
            #print e
            return False

    '''
    @author: Satish Tailor
    @note: navigating to Admin Users page
    '''
    def navigate_to_admin_users_page(self, webdriver, isURL=True):
        usersPage = UsersPage(webdriver)
        time.sleep(2)
        #if URL is true navigate using the browser URL
        if(isURL):
            usersPage.navigate()
        else:
            pass
            # sideNav = SideNavigationBar(webdriver)
            # #sideNav.button_create_new_title().click()

        try:
            # need to have a wait - also need to ensure the screen is full screen
            '''
            @note: This is_displayed() only!! confirms the element is visible to the user on the page.
            '''
            return usersPage.title().is_displayed()
        except NoSuchElementException as e:
            print e
            return False
    
    
    '''
    @author: Dervis Suleyman
    @summary: Create a place holder asset - to be used along side the spread sheet tool to populate the portal
    '''    
    def create_asset_placeholders(self,webdriver,portal_asset,offers):
        
        assert not (portal_asset['Title']==None or portal_asset['Title']=='' ),"Title is not present cannot create an asset without this..."
        
        overall_report=[]
        isEpisodicContent = not (portal_asset['series']==None or portal_asset['series']=='')
        
        '''Check channel exists else create new channel'''
        '''Before test create and upload a new MXF with a unique name'''
        titlePage = TitlePage(webdriver)
        #Navigate to the page
        assert self.navigate_to_create_new_title_page(webdriver,True)
        time.sleep(1)
        #start with 01
        if(not (portal_asset['asset_id']==None or portal_asset['asset_id']=='')):
            if(len(str(portal_asset['asset_id']))==15):
                titlePage.button_edit_id().click()
                titlePage.textfield_id().click()
                titlePage.textfield_id().clear()
                titlePage.textfield_id().send_keys(portal_asset['asset_id'])
            else:
                assert False,"Asset ID ["+str(portal_asset['asset_id'])+"] is incorrect length should be 15"


        '''Click drop down for channel and select '''
        titlePage.drop_down_channel()
        assert titlePage.select_channel(portal_asset['channel']),"The Channel["+portal_asset['channel']+"] could not be found..."
        
        '''Handle the case '''
        if(isEpisodicContent==True):
            assert titlePage.drop_down_series(),"Could not click on the Series Drop Down Field"
            assert titlePage.select_series(portal_asset['series']),"The series["+portal_asset['series']+"] could not be found..."
            assert titlePage.drop_down_season()
            assert titlePage.select_season(portal_asset['season']),"The season["+portal_asset['season']+"] could not be found..."
            titlePage.textfield_episode_number().click()
            assert not (portal_asset['episodeNumber']==None or portal_asset['episodeNumber']==''),"episode number not given..."
            assert not (portal_asset['TotalEpisodes']==None or portal_asset['TotalEpisodes']==''),"Total episode not given..."
            titlePage.textfield_episode_number().send_keys(portal_asset['episodeNumber'])
            titlePage.textfield_total_episode_number().click()
            titlePage.textfield_total_episode_number().clear()
            titlePage.textfield_total_episode_number().send_keys(portal_asset['TotalEpisodes'])

        #move onto 02
        titlePage.button_01_next().click()
        
        '''check if title is present else report fail'''
        assert not (portal_asset['Title']==None or portal_asset['Title']=='' ),"Title is not present cannot create an asset without this..."
        titlePage.textfield_title().click()
        titlePage.textfield_title().send_keys(portal_asset['Title'])

        titlePage.textfield_summary().click()
        
        if(not (portal_asset['Summary']==None or portal_asset['Summary']=='')):
            titlePage.textfield_summary().send_keys(portal_asset['Summary'])
        else:
            overall_report.append("No Summary given..")

        if(not (portal_asset['Actors']==None or portal_asset['Actors']=='')):
            titlePage.textfield_actors().click()
            '''Need to create actors using the enter key e.g. split on the comma and send keys then hit enter to insert the actor'''
            if(portal_asset['Actors'].find(',')==-1):
                titlePage.send_text(portal_asset['Actors'])
                titlePage.press_enter_key()
            else:
                actors = portal_asset['Actors'].split(',')
                for actor in actors:
                    titlePage.send_text(actor)
                    titlePage.press_enter_key()
                    time.sleep(1)
        else:
            overall_report.append("No Actors given..")
            #actors=False

        if(not (portal_asset['Warning']==None or portal_asset['Warning']=='')):
            titlePage.textfield_warning().click()
            titlePage.textfield_warning().send_keys(portal_asset['Warning'])
        else:
            overall_report.append("No Warning given..")
            #warning=False

        if(not (portal_asset['DisplayRuntime']==None or portal_asset['DisplayRuntime']=='')):
            titlePage.textfield_display_runtime().click()
            titlePage.textfield_display_runtime().send_keys(portal_asset['DisplayRuntime'])
        else:
            overall_report.append("No DisplayRuntime given..")
            #DisplayRuntime=False

        if(not (portal_asset['Genre']==None or portal_asset['Genre']=='' )):
            '''Drop down for Genre'''
            titlePage.drop_down_genre().click()
            time.sleep(2)
            titlePage.select_genre(portal_asset['Genre'])
        else:
            overall_report.append("No Genre given..")
            #Genre=False
        
        if(not (portal_asset['Rating']==None or portal_asset['Rating']=='')):
            '''drop down rating'''
            titlePage.drop_down_rating().click()
            titlePage.select_rating(portal_asset['Rating'])
        else:
            overall_report.append("No Rating given..")
            #rating=False

        if(not (portal_asset['BroadcastDate']==None or portal_asset['BroadcastDate']=='')):
            titlePage.textfield_broadcast_date().click()
            titlePage.textfield_broadcast_date().send_keys(portal_asset['BroadcastDate'])
        else:
            overall_report.append("No BroadcastDate given..")
            #broadcastDate=False

        if(not (portal_asset['ProductionYear']==None or portal_asset['ProductionYear']=='')):
            titlePage.textfield_production_year().click()
            titlePage.textfield_production_year().clear()
            titlePage.textfield_production_year().send_keys(portal_asset['ProductionYear'])
        else:
            overall_report.append("No ProductionYear given..")
            #productionYear=False

        if(not (portal_asset['Studio']==None or portal_asset['Studio']=='')):
            titlePage.textfield_studio().click()
            titlePage.textfield_studio().clear()
            titlePage.textfield_studio().send_keys(portal_asset['Studio'])
        else:
            overall_report.append("No Studio given..")
            #studio=False

        titlePage.button_02_next().click()
        time.sleep(3)
        
        #Move onto 03 - select the video
        '''
        @note: You cannot select Audio Lang until you have chosen the channel on the first tab of title
        '''
        
        if(not (portal_asset['VideoFile']==None or portal_asset['VideoFile']=='')):
            '''drop down media asset'''
            titlePage.drop_down_video_file().click()
            mxf = titlePage.select_video(portal_asset['VideoFile'])
            if mxf==False:
                overall_report.append("MXF["+portal_asset['VideoFile']+"] not found..") 
        else:
            overall_report.append("No VideoFile given..")
            #videoFile=False

        '''Button next step has click built into the function'''
        titlePage.button_next_step()

        #Move onto 04 - images & subs
        '''Upload a .stl the location must be within the project'''
        if(not (portal_asset['SubTitles']==None or portal_asset['SubTitles']=='')):
            sub = titlePage.upload_subtitles(portal_asset['SubTitles'])
            if sub==False:
                overall_report.append("SubTitles["+portal_asset['SubTitles']+"] not found..") 
        else:
            overall_report.append("No SubTitles given..")
            #subTitles=False
                    
        if(not (portal_asset['16-9-image']==None or portal_asset['16-9-image']=='')):
            image = titlePage.upload_image_16by9_1920by1080(portal_asset['16-9-image'])
            if image==False:
                overall_report.append("16-9-image["+portal_asset['16-9-image']+"] not found..") 
        else:
            overall_report.append("No 16-9-image given..")
            #image16by9=False       
            
        if(not (portal_asset['4-3-image']==None or portal_asset['4-3-image']=='')):
            image=titlePage.upload_image_4by3_1024by730(portal_asset['4-3-image'])
            if image==False:
                overall_report.append("4-3-image["+portal_asset['4-3-image']+"] not found..") 
        else:
            overall_report.append("No 4-3-image given..")
            #image4by3=False  
            
        if(not (portal_asset['Boxart-image']==None or portal_asset['Boxart-image']=='')):
            image=titlePage.upload_image_box_art_image_1080by1600(portal_asset['Boxart-image'])
            if image==False:
                overall_report.append("Boxart-image["+portal_asset['Boxart-image']+"] not found..")
            
            if type(image)==str:
                overall_report.append("Boxart-image["+portal_asset['Boxart-image']+"] Cannot be used for episodic asset..")
        else:
            overall_report.append("No Boxart image given..")
            #boxart=False 
        
        time.sleep(2)

        '''Button next step has click built into the function'''
        titlePage.button_next_step()
        
        
        #titlePage.button_save().click()
        
        '''Add an assert to check if the content exists'''
        #assert self.exists_title(webdriver, portal_asset['Title']),"The asset ["+portal_asset['Title']+"] could not be found..."
        
        '''report overall output'''
        if(len(overall_report)>0):
            '''Append Asset ID and Name to the Overall Report'''
            if(not (portal_asset['asset_id']==None or portal_asset['asset_id']=='')):
                overall_report.insert(0, ['asset_id',portal_asset['asset_id']])
            if(not (portal_asset['Title']==None or portal_asset['Title']=='')):
                overall_report.insert(0, ["Title",portal_asset['Title']])
            assert False,overall_report
        
    '''
    @author: Dervis Suleyman
    @summary: Check if the title is on in the portal, you can specify if you want to navigate or not
    '''
    def exists_title(self,webdriver,title_brief,navigate=True):
        titlePage = TitlePage(webdriver)
        '''Navigate to the titles page and check if the asset exits if yes create else don't'''
        if(navigate):
            titlePage.navigate_existing_titles()
            time.sleep(2)    
        titlePage.textfield_search(title_brief)
        asset = titlePage.find_title(title_brief)
        
        if(type(asset)==bool):
            return False
        else:
            return True
        

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
            #print e
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


    '''
    @author: Derivs Suleyman
    @note: create season function

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
    def create_new_season(self,webdriver,season_info,delete=False):
        seasonPage = SeasonsPage(webdriver)
        self.navigate_to_seasons_page(webdriver)
        seasonPage.button_add_season().click()
        assert seasonPage.label_add_season(),"Could not navigate to the [season] page..."

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


        '''click ok and create the season'''
        seasonPage.button_ok().click()

        #Temp wait
        time.sleep(3)
        
        '''check the season is present but do not navigate to the same screen'''
        #assert self.exists_season(webdriver, season_info['TitleBrief'], navigate=False),"The Season["+season_info['TitleBrief']+"] could not be created..."
        
        '''remove the season asset if delete is True'''
        if(delete):#delete):
            self.delete_season(webdriver, season_info['TitleBrief'])
            
    '''
    @author: Dervis Suleyman
    @summary: Check if the season is on in the portal, you can specify if you want to navigate or not
    '''
    def exists_season(self,webdriver,title_brief,navigate=True):
        seasonPage = SeasonsPage(webdriver)
        '''navigate to the series page if True'''
        if(navigate):
            assert self.navigate_to_seasons_page(webdriver),"Could not navigate to the season page..."
                #Temp wait
        time.sleep(2)
        '''expand row to max'''
        seasonPage.set_row_number('50')
        time.sleep(2)
        
        current_season = seasonPage.find_season(title_brief)
        
        if(type(current_season)==bool):
            return False
        
        return current_season.is_displayed()
        
    def delete_season(self,webdriver,title_brief):
        seasonPage = SeasonsPage(webdriver)
        '''remove the series'''
        seasonPage.find_season(title_brief).click()
        time.sleep(2)
        seasonPage.button_incon_delete_season().click()
        time.sleep(2)
        '''pop up'''
        assert seasonPage.label_delete_season(),"Could not see the Delete Season Popup"
        seasonPage.button_delete_season_ok().click()
        time.sleep(2)
        '''check season has been removed'''
        assert not seasonPage.find_season(title_brief),"The Season["+title_brief+"] could not be removed..."


    '''
    @author: Dervis Suleyman
    @note: create series function

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
    def create_new_series(self,webdriver,series_info,delete=False):
        seriesPage = SeriesPage(webdriver)
        assert self.navigate_to_series_page(webdriver),"Could not navigate to the [series page] page..."
        seriesPage.button_add_series().click()
        '''Pop up'''
        assert seriesPage.label_add_series(),"Could not see the [add series] popup..."


        '''Enter series id if given'''
        if(not (series_info['SeriesID']==None or series_info['SeriesID']=='')):
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
        time.sleep(2)
        seriesPage.textfield_studio_display().send_keys(series_info['StudioDisplay'])
        '''
        @note: Upload images
        '''
        seriesPage.upload_image_16by9_1920by1080(series_info['16x9 image'])
        seriesPage.upload_image_4by3_1024by730(series_info['4x3 image'])


        '''click ok and create the series'''
        seriesPage.button_ok().click()
        
        '''check the series is present but do not navigate to the same screen'''
        #assert self.exists_series(webdriver, series_info['TitleBrief'], navigate=False),"The Series["+series_info['SummaryShort']+"] could not be created..."
        
        '''remove the asset from if delete is True'''
        if(delete):#delete):
            self.delete_series(webdriver, series_info['TitleBrief'])

    
    '''
    @author: Dervis Suleyman
    @summary: Check if the series is on in the portal, you can specify if you want to navigate or not
    '''
    def exists_series(self,webdriver,title_brief,navigate=True):
        seriesPage = SeriesPage(webdriver)
        '''navigate to the series page if True'''
        if(navigate):
            assert self.navigate_to_series_page(webdriver)
        #Temp wait
        time.sleep(2)
        '''expand row to max'''
        seriesPage.set_row_number('50')
        
        current_series = seriesPage.find_series(title_brief)
        
        if(type(current_series)==bool):
            return False
        
        return current_series.is_displayed()
        
    def delete_series(self,webdriver,title_brief):
        seriesPage = SeriesPage(webdriver)
        '''remove the series'''
        seriesPage.find_series(title_brief).click()
        time.sleep(2)
        seriesPage.button_incon_delete_series().click()
        time.sleep(2)
        '''pop up'''
        assert seriesPage.label_delete_series()
        seriesPage.button_delete_series_ok().click()
        time.sleep(2)
        '''check series has been removed'''
        assert not seriesPage.find_series(title_brief)

    '''create channel function'''
    def create_new_channel(self,webdriver):
        pass

    '''create provider function'''
    def create_new_provider(self,webdriver):
        pass

    '''create user function'''
    def create_new_user(self, webdriver):
        pass