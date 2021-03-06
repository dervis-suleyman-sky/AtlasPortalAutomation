'''
Created on 23 Feb 2016

@author: Dev2
'''
import pytest
from isilon.isilon_ftp_helper import IsilonHelper
from portal.config_module import PortalConfig

@pytest.fixture(scope="module")
def config_settings():
    '''set connection details'''
    pass

'''Login fixture will run per python module and stay active till the end of the test'''
@pytest.fixture(scope="module")
def Login(request,webdriver):
    from portal.portal_module import Portal
    config = PortalConfig()
    portal = Portal()
    assert portal.login(webdriver, username=config.username(),password=config.password())
    '''set the provider e.g. NBCU'''

@pytest.fixture(scope="module")
def webdriver(request):
    from webdriver_utils.selenium_webdriver import WebDriver
    webdriver = WebDriver()
    config = PortalConfig()
    #check for the web browser other wise create 
    if config.browser()=="chrome":
        webdriver.set_chrome_driver()
    else:
        webdriver.set_firefox_driver()

    def fin():
        print ("Teardown close the driver")     
#         from portal.portal_module import Portal
#         portal = Portal()
#         portal.logout(webdriver)
        webdriver.driver.quit()
    request.addfinalizer(fin)
    return webdriver

    '''
    Check Media Files are present in the correct drop zone
    '''
@pytest.fixture(scope="module")
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

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call':
#         # always add url to report
#         extra.append(pytest_html.extras.url(__url))
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             extra.append(pytest_html.extras.image('\images\demoScreenShot.pmg', "Link to Image"))
#             #extra.append(pytest_html.extras.image('C:\workspace\DebugGUI\images\demoScreenShot.pmg', "Link to Image"))
#             # only add additional html on failure
#             #extra.append(pytest_html.extras.html('Additional HTML'))
#         report.extra = extra