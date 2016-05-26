'''
Created on 24 May 2016

@author: Dev2
'''

from portal.portal_module import Portal

class TestClass(object):
    '''
    classdocs
    '''
    Satish Tailor: Added user tests
    '''
    def test_add_user(self,webdriver):
        portal = Portal()
        assert portal.login(webdriver, username="st_admin",password="12345")
        assert portal.logout(webdriver)

