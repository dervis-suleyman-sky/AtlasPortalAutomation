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
    def test_navigate_to_login_page(self,webdriver):
        portal = Portal()
        assert portal.navigate_to_add_user_page(webdriver)

    def test_login_invalid_credentials(self,webdriver):
        portal = Portal()
        assert not portal.login(webdriver, username="Invalid_user",password="Invalid_password")


    def test_add_user(self,webdriver):
        portal = Portal()
        assert portal.login(webdriver, username="st_admin",password="12345")
        assert portal.logout(webdriver)

