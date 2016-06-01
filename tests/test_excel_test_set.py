'''
Created on 1 Jun 2016

@author: Dev2
'''

from portal.portal_module import Portal
import pytest
import json

from excel.excel_helper import ExcelHelper

class TestClass(object):
    
    '''
    @author: Dervis Suleyman
    @summary: Load a test set from an excel spread sheet specified by the tester
    @note: sample .xlsm file can be found in \AtlasPortalAutomation\excel\excel_documents\test.xlsm
    '''
    @pytest.fixture(scope="module")
    def load_set(self):
        excel_helper = ExcelHelper('C:\\workspace\\AtlasPortalAutomation\\excel\\excel_documents\\test.xlsm')
        test_set = excel_helper.get_test_set()
        return test_set['test_set'].items()
    
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
    
    '''
    @note: The login test should leave the user logged into the machine
    '''
    def test_navigate_to_new_title_page(self,webdriver):
        portal = Portal()
        assert portal.navigate_to_create_new_title_page(webdriver, True)
    
    @pytest.mark.parametrize("test",load_set(""))
    def test_portal_asset(self,webdriver,test):
        
        series_info = test[1].get('series_info')
        season_info = test[1].get('season_info')
        portal_asset = test[1].get('portal_asset')
        platform_offers = test[1].get('platform')
        
#         print test
#         print json.dumps(test,indent=4, separators=(',', ': '))
        
        portal = Portal()
        '''No need for an assert here the function contains asserts'''
        portal.create_new_series(webdriver, series_info)
        portal.create_new_season(webdriver, season_info)
        portal.create_new_title(webdriver,portal_asset,platform_offers)
        
        
        
        