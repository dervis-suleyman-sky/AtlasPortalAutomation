'''
Created on 25 May 2016

@author: Satish Tailor
'''

class SeriesPage(object):
    '''
    classdocs
    '''

    def navigate(self):
        self.driver.get('https://vodportal-test.awf.bskyb.com/#/assets/series')

    def __init__(self, web_driver):
        '''
        @attention: the web driver
        '''
        self.driver = web_driver.driver

    def title(self):
        # may need a wait condition/function here
        return self.driver.find_element_by_xpath('/html/body/div/div/div/md-content/div/div/div/md-toolbar[1]/div/h2')

    def button_add_series(self):
        return self.driver.find_element_by_xpath('/html/body/div/div/div/md-content/div/div/div/md-toolbar[1]/div/button[2]')

    '''Add Series pop up elements'''

    def drop_down_series(self):
        return self.driver.find_element_by_xpath('//*[@id="select_171"]')

    def button_edit_id(self):
        return self.driver.find_element_by_xpath('/html/body/div[3]/md-dialog/md-dialog-content/div/form/div/div[1]/md-icon')

    def textfield_title_brief(self):
        return self.driver.find_element_by_name('titleBrief')

    def textfield_summary_brief(self):
        return self.driver.find_element_by_name('summaryBrief')

    def drop_down_genre(self):
        return self.driver.find_element_by_name('genre')

    def textfield_studio(self):
        return self.driver.find_element_by_name('studioDisplay')

    '''Add image load elements'''

    def button_land_16_9_series(self):
        return self.driver.find_element_by_name('LAND_16_9_SERIES')

    def button_land_n_4_3_series(self):
        return self.driver.find_element_by_name('LAND_N_4_3_SERIES')

    '''Add OK an CANCEL buttons'''

    def button_cancel(self):
        return self.driver.find_element_by_xpath('/html/body/div[3]/md-dialog/div/button[1]')

    def button_ok(self):
        return self.driver.find_element_by_xpath('/html/body/div[3]/md-dialog/div/button[2]')
