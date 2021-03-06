'''
Created on 1 Jun 2016

@author: Dev2
'''

from portal.portal_module import Portal
from portal.config_module import PortalConfig
import pytest

from excel.excel_helper import ExcelHelper

class TestClass(object):
    
    '''
    @author: Dervis Suleyman
    @summary: Load a test set from an excel spread sheet specified by the tester
    @note: sample .xlsm file can be found in \AtlasPortalAutomation\excel\excel_documents\test.xlsm
    '''
    @pytest.fixture(scope="module")
    def load_set(self):
        config = PortalConfig()
        excel_helper = ExcelHelper(config.excel_file_location['spread_sheet_location'])
        test_set = excel_helper.get_test_set()
        return test_set['test_set'].items()
    
    '''
    Execute load test from spread sheet
    @todo: Check series or season exits if yes ignore and contiue
    '''
    @pytest.mark.parametrize("test",load_set(""))
    def test_portal_asset(self,webdriver,Login,test):
        
        '''Delete or create'''
        create=True
        update=False
        delete=False
        
        '''read test data'''
        series_info = test[1].get('series_info')
        season_info = test[1].get('season_info')
        portal_asset = test[1].get('portal_asset')
        platform_offers = test[1].get('platform')
       
        '''for debugging JSON data'''
        #print test
        #print json.dumps(test,indent=4, separators=(',', ': '))
        
        portal = Portal()
        
        #Take from the spread sheet create
        if(create):
#             '''check the series can be created'''
#             if(not series_info['TitleBrief']==None):
#                 '''check series already created and skip creation else create'''
#                 #if(not portal.exists_series(webdriver, series_info['TitleBrief'], navigate=True)):
#                 '''No need for an assert here the function contains asserts'''
#                 portal.create_new_series(webdriver, series_info,delete=False)
#                 
#                 '''check season already created and skip creation else create'''
#                 #if(not portal.exists_season(webdriver, season_info['TitleBrief'], navigate=True)):
#                 portal.create_new_season(webdriver, season_info,delete=False)
                     
            '''create new episodic or non-episodic asset'''
            if(not portal.exists_title(webdriver, portal_asset['Title'],navigate=True)):
                portal.create_asset_placeholders(webdriver, portal_asset, platform_offers)
            
        if(update):
            pass
        
        if(delete):
            pass
        
        
        
        
        
        