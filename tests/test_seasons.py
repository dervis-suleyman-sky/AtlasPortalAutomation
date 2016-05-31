#-*- coding: utf-8 -*-
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
        assert portal.navigate_to_seasons_page(webdriver)
        
        
    def test_create_season(self,webdriver):
        portal = Portal()
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
        
        
        portal.create_new_season(webdriver, season_info)
        
        
        