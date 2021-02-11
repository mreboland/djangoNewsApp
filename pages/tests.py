# We import the below to reference our custom user model.
from django.contrib.auth import get_user_model
# SimpleTestCase is fine for testint the homepage as it doesn't use any db code. However the sign up page does so we need to use TestCase for it.
from django.test import SimpleTestCase, TestCase
# Use reverse() to give you the url of a page, given either the path to the view, or the page_name parameter from your url conf.
from django.urls import reverse

# We only need tests for our home and sign up pages and not our log in and out. The reason is the latter 2 are a part of django and unless we've made substantial changes to django's built in system there is no need to test it. We do not need to add tests for core django functionality.

# For both tests, we test 3 things:
# • the page exists and returns a HTTP 200 status code
# • the page uses the correct url name in the view
# • the proper template is being used
class HomePageTests(SimpleTestCase):
    
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_view_url_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        

class SignupPageTests(TestCase):
    
    username = "newuser"
    email = "newuser@email.com"
    
    def test_signup_page_status_code(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        
    def test_view_url_by_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
        
    # Here we're verifying that when a username and email address as POSTed (sent to db), they match what is stored on the CustomUser model.
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
        
        
