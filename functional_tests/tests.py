from selenium import webdriver
from django.test import LiveServerTestCase


# Create your tests here.
class TestHomePage(LiveServerTestCase):
    @classmethod
    def setUp(self):
       self.browser = webdriver.Firefox()
       self.browser.implicitly_wait(3)

    @classmethod
    def tearDown(self):  
        self.browser.quit()
        pass


    #Billy Participant loads the home page
    def test_index_page(self):
        self.browser.get(self.live_server_url)
        self.assertTemplateUsed('home.html')
        self.assertIn('Events', self.browser.title)
        

    #Billy loads the signup page
    def test_signup_page(self):    
        self.browser.get(self.live_server_url + '/account/signup')
        self.assertTemplateUsed('signup.html')

    #Billy loads the login page
    def test_login_page(self):    
        self.browser.get(self.live_server_url + '/account/login')
        self.assertTemplateUsed('login.html')


class TestSignUpPage(LiveServerTestCase):
    @classmethod
    def setUp(self):
       self.browser = webdriver.Firefox()
       self.browser.implicitly_wait(3)

    @classmethod
    def tearDown(self):  
        self.browser.quit()
        pass
    
    def test_create_user_with_no_username(self):
        self.browser.get(self.live_server_url + '/account/signup')
        self.browser.find_element_by_id('id_email').send_keys('\n')
        error = self.browser.find_element_by_id('error_1_id_email')
        self.assertEqual(error.text, "This field is required.")

    def test_create_user(self):
        self.browser.get(self.live_server_url + '/account/signup')
        self.browser.find_element_by_id('id_email').send_keys('kienen@mockmyid.com')
        self.browser.find_element_by_id('id_password').send_keys('correcthorsebatterystaple')
        self.browser.find_element_by_id('id_password_confirm').send_keys('correcthorsebatterystaple\n')
        self.assertEqual('Confirm your email address', self.browser.title)
        self.assertTemplateUsed('email_confirmation_sent.html')
