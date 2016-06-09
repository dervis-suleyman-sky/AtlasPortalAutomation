'''
Created on 12 Apr 2016

@author: Dev2
'''

from portal.config_module import PortalConfig


class SideNavigationBar(object):
    
    '''
    classdocs
    '''
    
    def __init__(self, web_driver):
        '''
        @attention: the web driver
        '''
        self.driver=web_driver.driver
        
    def button_dashboard(self):
        return self.driver.find_element_by_xpath('/html/body/div/div/md-sidenav[1]/tri-menu/md-content/tri-menu-item[1]/div/button/span')
    
    def button_assets(self):
        return self.driver.find_element_by_xpath('/html/body/div/div/md-sidenav[1]/tri-menu/md-content/tri-menu-item[2]/div/button')
    
    '''
    @note: SubMenu Items
    '''
    def button_series(self):
        return self.driver.find_element_by_xpath('/html/body/div/div/md-sidenav[1]/tri-menu/md-content/tri-menu-item[2]/div/ul/li[1]/tri-menu-item/div/button')
    
    def button_seasons(self):
        return self.driver.find_element_by_xpath('/html/body/div/div/md-sidenav[1]/tri-menu/md-content/tri-menu-item[2]/div/ul/li[2]/tri-menu-item/div/button')
    
    def button_titles(self):
        return self.driver.find_element_by_xpath('/html/body/div/div/md-sidenav[1]/tri-menu/md-content/tri-menu-item[2]/div/ul/li[3]/tri-menu-item/div/button')
    
    def button_media(self):
        return self.driver.find_element_by_xpath('/html/body/div/div/md-sidenav[1]/tri-menu/md-content/tri-menu-item[3]/div/button/span')
    
    def button_create_new_title(self):
        return self.driver.find_element_by_xpath('/html/body/div/div/md-sidenav[1]/tri-menu/md-content/tri-menu-item[4]/div/button/span')
    
    def button_admin(self):
        return self.driver.find_element_by_xpath('/html/body/div/div/md-sidenav[1]/tri-menu/md-content/tri-menu-item[5]/div/button')
    
    '''
    @note: SubMenu Items
    '''
    def button_users(self):
        return self.driver.find_element_by_xpath('/html/body/div/div/md-sidenav[1]/tri-menu/md-content/tri-menu-item[5]/div/ul/li[1]/tri-menu-item/div/button')
    
    def button_actors(self):
        return self.driver.find_element_by_xpath('/html/body/div/div/md-sidenav[1]/tri-menu/md-content/tri-menu-item[5]/div/ul/li[2]/tri-menu-item/div/button')
