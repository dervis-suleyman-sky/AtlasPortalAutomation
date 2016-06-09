'''
Created on 9 Jun 2016

@author: Dev2
'''

import ConfigParser
import os

class PortalConfig():
    '''
    @author: Dervis Suleyman
    @summary: Check if the config.ini file exists if not create and populate else read contents
    '''
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config_file_location=os.path.abspath("")+"\\config.ini"
        self.config.read(self.config_file_location)
        self.portalDetails=self.ConfigSectionMap('PortalDetails')
        self.userCredentials=self.ConfigSectionMap('userCredentials')
        self.content=self.ConfigSectionMap('content')
        self.reports=self.ConfigSectionMap('reports')
        self.excel_file_location=self.ConfigSectionMap('spreadSheet')
    
    def ConfigSectionMap(self,section):
        dict1 = {}
        options = self.config.options(section)
        for option in options:
            try:
                dict1[option] = self.config.get(section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except:
                #print("exception on %s!" % option)
                dict1[option] = None
        return dict1
    
    '''
    Portal Details
    '''
    def url(self):
        return self.portalDetails['portal_url']
    
    def browser(self):
        return self.portalDetails['browser']
    
    def provider(self):
        return self.portalDetails['provider']
    
    '''
    userCredentials
    '''
    def username(self):
        return self.userCredentials['user_name']
    
    def password(self):
        return self.userCredentials['user_password']
    

    '''
    content
    '''
    def image_dir_location(self):
        return self.content['image_folder_location']
    
    def media_dir_location(self):
        return self.content['media_folder_location']
    
    def subtitles_dir_location(self):
        return self.content['subtitles_folder_location']

    '''
    reports
    '''
    def reports_dir_location(self):
        return self.reports['output_directory']
    
    '''
    spread sheet location
    '''
    def spread_sheet_location(self):
        return self.excel_file_location['spread_sheet_location']
  
# '''
# Test
# '''
# if __name__ == '__main__':
#     config = PortalConfig()
#     '''portal details'''
#     print config.url()
#     print config.browser()
#     print config.provider()
#     '''portal details'''
#     print config.username()
#     print config.password()
#     '''portal details'''
#     print config.image_dir_location()
#     print config.media_dir_location()
#     print config.subtitles_dir_location()
#     '''portal details'''
#     print config.reports_dir_location()
#     '''spread sheet location'''
#     print config.spread_sheet_location()
    
    
    