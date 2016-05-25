'''
Created on 24 May 2016

@author: Satish Tailor
'''

class SeasonsPage(object):
    '''
    classdocs
    '''

    def navigate(self):
        self.driver.get('https://vodportal-test.awf.bskyb.com/#/assets/seasons')

    def __init__(self, web_driver):
        '''
        @attention: the web driver
        '''
        self.driver = web_driver.driver

    def title(self):
        #may need a wait condition/function here
        return self.driver.find_element_by_xpath('//*[@id="ui-admin"]/div/md-toolbar[1]/div/h2')

    def button_add_season(self):
        return self.driver.find_element_by_xpath('//*[@id="ui-admin"]/div/md-toolbar[1]/div/button[2]/md-icon')

    '''Add Season pop up elements'''

    def drop_down_series(self):
        return self.driver.find_element_by_xpath('//*[@id="select_171"]')

    def button_edit_id(self):
        return self.driver.find_element_by_xpath('//*[@id="dialogContent_173"]/div/form/div/div[2]/md-icon')

    def textfield_title_brief(self):
        return self.driver.find_element_by_name('seasonBrief')

    def textfield_summary_brief(self):
        return self.driver.find_element_by_name('summaryBrief')

    def textfield_season_num(self):
        return self.driver.find_element_by_name('seasonNum')

    def textfield_total_episodes(self):
        return self.driver.find_element_by_name('totalEpisodes')

    def textfield_production_year(self):
        return self.driver.find_element_by_name('year')

    '''Add image load elements'''

    def button_land_16_9_season(self):
        return self.driver.find_element_by_name('LAND_16_9_SEASON')

    def button_land_n_4_3_season(self):
        return self.driver.find_element_by_name('LAND_N_4_3_SEASON')

    '''Add OK an CANCEL buttons'''

    def button_cancel(self):
        return self.driver.find_element_by_xpath('/html/body/div[3]/md-dialog/div/button[1]/span')

    def button_ok(self):
        return self.driver.find_element_by_xpath('/html/body/div/div/div/md-content/div/ui-view/div/div/div/div/md-tabs/md-tabs-content-wrapper/md-tab-content[1]/div/div/form/div/div[2]/div[1]/md-icon[2]')
