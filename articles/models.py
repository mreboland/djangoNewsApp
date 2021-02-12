from django.conf import settings
# We want to use our custom user model which we set in config/settings.py as AUTH_USER_MODEL. We can do so by importing get_user_model. We use said model for our author, the user.
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    # Allows us to view the model in our admin interface
    def __str__(self):
        return self.title
    
    # When we create a new article and click save we are redirected to the detail page.
    # https://stackoverflow.com/questions/43179875/when-to-use-django-get-absolute-url-method
    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])
