'''
Created on 24 May 2016

@author: Dev2
'''

from portal.portal_module import Portal
import pytest

class TestClass(object):
    
    '''
    @author: Satish Tailor
    @summary: Test Navigation to the Seasons page is possible, if the Seasons page is not found fail the test
    '''
 
    def test_navigate_to_season_page(self, webdriver,Login):
        portal = Portal()
        assert portal.navigate_to_seasons_page(webdriver,isURL=True)