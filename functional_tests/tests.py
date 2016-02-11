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
        self.browser.get(self.live_server_url + '/signup')
        self.assertTemplateUsed('signup.html')

    #Billy loads the login page
    def test_login_page(self):    
        self.browser.get(self.live_server_url + '/login')
        self.assertTemplateUsed('login.html')
