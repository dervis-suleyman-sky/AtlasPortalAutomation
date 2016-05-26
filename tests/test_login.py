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

    '''
    Satish Tailor: Added the logout assert statements to combine login and logout tests
    '''
    def test_admin_role_login_and_logout_valid_credentials(self,webdriver):
        portal = Portal()
        assert portal.login(webdriver, username="st_admin",password="12345")
        assert portal.logout(webdriver)

    def test_superuser_role_login_and_logout_valid_credentials(self, webdriver):
        portal = Portal()
        assert portal.login(webdriver, username="st_superuser", password="12345")
        assert portal.logout(webdriver)

    def test_user_role_login_and_logout_valid_credentials(self, webdriver):
        portal = Portal()
        assert portal.login(webdriver, username="st_user", password="12345")
        assert portal.logout(webdriver)

    '''
    Satish Tailor: Added minimum password length tests
    '''
    def test_minimum_password_length_of_eight_7_disallowed(self, webdriver):
        portal = Portal()
        assert not portal.login(webdriver, username="st_admin_pw_length_7", password="1234567")

    def test_minimum_password_length_of_eight_8_allowed(self, webdriver):
        portal = Portal()
        assert portal.login(webdriver, username="st_admin_pw_length_8", password="12345678")
