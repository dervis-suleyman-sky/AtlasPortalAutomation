'''
Created on 23 Feb 2016

@author: Dev2

https://pypi.python.org/pypi/pytest-html
pip install pytest-html
https://github.com/davehunt/pytest-html
https://docs.python.org/2.7/installing/index.html

'''

from portal.portal_module import Portal

class TestClass:
  
    '''
    @author: Dervis Suleyman
    @summary: Test Navigation to the Portal is possible, if the login page is not found fail the test
    '''
    def test_navigate_to_login_page(self,webdriver):
        portal = Portal()
        assert portal.navigate_to_login_page(webdriver)
 
    def test_login_valid_credentials(self,webdriver):
        portal = Portal()
        assert portal.login(webdriver, username="dervis_admin",password="abcd12345")

#     '''Set the provider to 2'''
#     def test_change_provider(self,webdriver):
#         portal = Portal()
#         assert portal.set_provider(webdriver,provider=2)
 
#     '''
#     @author: Dervis Suleyman
#     @summary: Check if the .mxfs are in the isilon for the portal if not copy them from the project, to ensure you are ready for automated testing 
#     '''
#     def test_navigate_to_media_page(self,webdriver):
#         portal = Portal()
#         assert portal.navigate_to_media_page(webdriver)
#         
#     def test_check_media_content_is_present(self,webdriver):
#         portal = Portal()
#         content=['auto_test_media_asset_01']
#         content_file_path='C:\\workspace\\AtlasPortalAutomation\\isilon\\test_media'
#         dropzone='/mnt/dmz/atlas_provider_2/drop/'
#         portal.check_media_content_is_present(webdriver,content,content_file_path,destination_folder=dropzone)

  
    '''
    @note: The login test should leave the user logged into the machine
    '''
    def test_navigate_to_new_title_page(self,webdriver):
        portal = Portal()
        assert portal.navigate_to_create_new_title_page(webdriver, True)
    
    '''
    @author: Dervis Suleyman
    @summary: Create a new non-episodic asset
    '''
    def test_create_new_title(self,webdriver):
        '''
        Test Data
        '''
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
        
        '''
        Test data for offers
        
            "platform": {
                "AS": {
                    "Platform": "AS",
                    "EndDate": "2016-05-31 00:00:00",
                    "Type": "Catchup",
                    "StartDate": "2016-05-24 00:00:00"
                },
                "AM": {
                    "Platform": "AM",
                    "EndDate": "2016-05-31 00:00:00",
                    "Type": "Catchup",
                    "StartDate": "2016-05-24 00:00:00"
                },
                "AT": {
                    "Platform": "AT",
                    "EndDate": "2016-05-31 00:00:00",
                    "Type": "Catchup",
                    "StartDate": "2016-05-24 00:00:00"
                }
            }
        
        '''
        
        platform_offers = {
                           "AS": {
                                "Platform": "AS",
                                "EndDate": "2016-05-31 00:00:00",
                                "Type": "Catchup",
                                "StartDate": "2016-05-24 00:00:00"
                            },
                            "AM": {
                                "Platform": "AM",
                                "EndDate": "2016-05-31 00:00:00",
                                "Type": "Catchup",
                                "StartDate": "2016-05-24 00:00:00"
                            },
                            "AT": {
                                "Platform": "AT",
                                "EndDate": "2016-05-31 00:00:00",
                                "Type": "Catchup",
                                "StartDate": "2016-05-24 00:00:00"
                            }
                        }
        
        portal = Portal()
        '''No need for an assert here the function contains asserts'''
        portal.create_new_title(webdriver,portal_asset,platform_offers)
        
        