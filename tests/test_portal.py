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
    @summary: Check if the .mxfs are in the isilon for the portal if not copy them from the project, to ensure you are ready for automated testing 
    '''
    def test_output_config_params(self,config_settings):
        print("project config settings...")
  
    '''
    @author: Dervis Suleyman
    @summary: Test Navigation to the Portal is possible, if the login page is not found fail the test
    '''
    def test_navigate_to_login_page(self,webdriver):
        portal = Portal()
        assert portal.navigate_to_login_page(webdriver)
#           
#     def test_login_invalid_credentials(self,webdriver):
#         portal = Portal()
#         assert not portal.login(webdriver, username="Invalid_user",password="Invalid_password")
#      
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
#     def test_navigate_to_new_title_page(self,webdriver):
#         portal = Portal()
#         assert portal.navigate_to_create_new_title_page(webdriver, True)
       
    def test_create_new_title(self,webdriver):
        portal = Portal()
        assert portal.create_new_title(webdriver)

        