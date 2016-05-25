'''
Created on 24 May 2016

@author: Dev2
'''

from portal.portal_module import Portal

class TestClass(object):
    '''
    classdocs
    '''
    def test_navigate_to_login_page(self,webdriver):
        portal = Portal()
        assert portal.navigate_to_login_page(webdriver)

    def test_login_invalid_credentials(self,webdriver):
        portal = Portal()
        assert not portal.login(webdriver, username="Invalid_user",password="Invalid_password")

    def test_admin_role_login_valid_credentials(self,webdriver):
        portal = Portal()
        assert portal.login(webdriver, username="st_admin",password="12345")

    def test_superuser_role__login_valid_credentials(self, webdriver):
        portal = Portal()
        assert portal.login(webdriver, username="st_superuser", password="12345")

    def test_user_role_login_valid_credentials(self, webdriver):
        portal = Portal()
        assert portal.login(webdriver, username="st_user", password="12345")
