from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


# Create your tests here.
class TestHomePage(StaticLiveServerTestCase):

    def setUp(self):
       self.browser = webdriver.Firefox()
       self.browser.implicitly_wait(3)

    def tearDown(self):  
        self.browser.quit()
        pass

    #Billy Participant loads the home page
    def test_index_page(self):
        self.browser.get(self.live_server_url)
        self.assertTemplateUsed('home.html')
        self.assertIn('Events', self.browser.title)
        #self.assertEqual(self.response_code, '200')

    #Billy creates an account
    #def test_signup(self):    