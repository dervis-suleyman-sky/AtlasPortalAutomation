'''
Created on 23 Feb 2016

@author: Dev2
'''
import pytest


'''Portal URL for testing'''    
portal_url = "https://vodportal-test.awf.bskyb.com"
provider="Test provider 1"
'''
Super user connection details
'''
super_user_name="Dervis_superuser"
super_user_password="test1234"
'''
Admin user connection details
'''
Admin_user_name="dervis_admin"
Admin_user_password="abcd12345"
'''browser for testing'''
test_browser="chrome"
'''chrome exe path'''
chrom_exe="C:/workspace/DebugGUI/chromedriver_win32/chromedriver"
'''isilon drop zone'''
drop_zone="/mnt/dmz/atlas_provider_1/drop"
'''MongoDB connection details'''
mongodb_connection_details=""
'''content location'''
test_image_folder_location="C:\workspace\AtlasPortalAutomation\isilon\test_images"
test_media_folder_location="C:\workspace\AtlasPortalAutomation\isilon\test_media"


@pytest.fixture(scope="module")
def config_settings():
    '''set connection details'''
    pass

@pytest.fixture(scope="module")
def webdriver(request):
    from webdriver_utils.selenium_webdriver import WebDriver
    webdriver = WebDriver()
    
    #check for the web browser other wise create 
    if test_browser=="chrome":
        webdriver.set_chrome_driver()
    else:
        webdriver.set_firefox_driver()
        
    def fin():
        print ("Teardown close the driver")
        webdriver.driver.quit()
    request.addfinalizer(fin)
    return webdriver

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