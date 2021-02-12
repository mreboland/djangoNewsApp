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
    
    # When we create or edit a new article and click save we are redirected to the detail page. If we don't have this we'll get an error saying we need a get_absolute_url.
    # https://stackoverflow.com/questions/43179875/when-to-use-django-get-absolute-url-method
    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])


# We want to have users be able to add comments to our articles. We will do so using a foreignKey and the model which will handle it will have a many-to-one relationship with Article. One article can have many components but not the other way around.
# Traditionally the name of the foreign key field is simply the model it links to. So in this case it'll be called article. We'll also use two other fields, comment and author.

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.comment
    
    # Return to article_list page after commenting
    def get_absolute_url(self):
        return reverse("article_list")