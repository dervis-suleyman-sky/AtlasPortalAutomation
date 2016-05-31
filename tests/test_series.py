'''
Created on 24 May 2016

@author: Dev2
'''

from portal.portal_module import Portal

class TestClass(object):
    '''
    classdocs
    '''
    def test_navigate_to_series_page(self,webdriver,Login):
        portal = Portal()
        assert portal.navigate_to_series_page(webdriver)
        
    '''
    test the creation of a new series
    '''
    def test_creat_new_series(self,webdriver):
        portal = Portal()
        series_info = {'SeriesID':'12345678901234567892',
                       'TitleBrief':'Title brief',
                       'TitleMedium':'Title medium',
                       'TitleLong':'Long',
                       'SummaryBrief':'brief',
                       'SummaryShort':'short',
                       'SummaryMedium':'med',
                       'SummaryLong':'long',
                       'Genre':'Children:Factual',
                       'StudioDisplay':'studio',
                       '16x9 image':'\\isilon\\test_images\\1167563-LAND_16_9.jpg',
                       '4x3 image':'\\isilon\\test_images\\1167563-LAND_N_4_3.jpg'}
        
        portal.create_new_series(webdriver, series_info)
        
    '''
    test the creation of a new series
    '''
    def test_creat_new_series_no_id_given(self,webdriver):
        portal = Portal()
        series_info = {'SeriesID':'',
                       'TitleBrief':'Title brief',
                       'TitleMedium':'Title medium',
                       'TitleLong':'Long',
                       'SummaryBrief':'brief',
                       'SummaryShort':'short',
                       'SummaryMedium':'med',
                       'SummaryLong':'long',
                       'Genre':'Children:Factual',
                       'StudioDisplay':'studio',
                       '16x9 image':'\\isilon\\test_images\\1167563-LAND_16_9.jpg',
                       '4x3 image':'\\isilon\\test_images\\1167563-LAND_N_4_3.jpg'}
        
        portal.create_new_series(webdriver, series_info)
        
        
        
        
        