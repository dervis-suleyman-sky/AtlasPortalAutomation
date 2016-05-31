'''
Created on 25 May 2016

@author: Satish Tailor
'''

class UsersPage(object):
    '''
    classdocs
    '''


    def __init__(self, web_driver):
        '''
        @attention: the web driver
        '''
        self.driver = web_driver.driver

    def navigate(self):
        self.driver.get('https://vodportal-test.awf.bskyb.com/#/admin/users')

    def title(self):
        # may need a wait condition/function here
        return self.driver.find_element_by_xpath('/html/body/div[1]/div/div/md-content/div/div/div/md-toolbar[1]/div/h2')

    def button_add_user(self):
        return self.driver.find_element_by_xpath('/html/body/div[1]/div/div/md-content/div/div/div/md-toolbar[1]/div/button[2]')

    '''Add User pop up elements'''

    def textfield_username(self):
        return self.driver.find_element_by_name('username')

    def textfield_firstname(self):
        return self.driver.find_element_by_name('firstName')

    def textfield_lastname(self):
        return self.driver.find_element_by_name('lastName')

    def textfield_email(self):
        return self.driver.find_element_by_name('email')

    '''rating drop down'''
    def drop_down_role(self):
        return self.driver.find_element_by_name('role')

    def drop_down_rating(self):
        return self.driver.find_element_by_name('rating')

    '''Search through all the md-options to find the role for the test'''
    def select_rating(self,_role='admin'):
        #Wait for the drop down to load
        time.sleep(2)
        #Look for all elements with the tag name 'md-option' and store in a list
        element_md_options = self.driver.find_elements_by_tag_name('md-option')
        #loop through the list until you find your role then click
        for md_option in element_md_options:
            if md_option.text==_role:
                md_option.click()
                '''If role is found click the value'''
                return True
        return False

    def textfield_password(self):
        return self.driver.find_element_by_name('password')

    def textfield_confirm_password(self):
        return self.driver.find_element_by_name('confirmPassword')
    '''Add OK an CANCEL buttons'''

    def button_cancel(self):
        return self.driver.find_element_by_xpath('/html/body/div[3]/md-dialog/div/button[1]')

    def button_ok(self):
        return self.driver.find_element_by_xpath('/html/body/div[3]/md-dialog/div/button[2]')
