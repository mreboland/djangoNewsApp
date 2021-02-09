# Note that we did not run migrate to configure our database. It’s important to wait until after
# we’ve created our new custom user model before doing so given how tightly connected the user
# model is to the rest of Django.

# If you read the official documentation on custom user models it recommends using 
# AbstractBaseUser not AbstractUser. This needlessly complicates things.

# AbstractBaseUser vs AbstractUser
# AbstractBaseUser requires a very fine level of control and customization. We essentially
# rewrite Django. This can be helpful, but if we just want a custom user model that can be updated
# with additional fields, the better choice is AbstractUser which subclasses AbstractBaseUser.
# In other words, we write much less code and have less opportunity to mess things up. It’s the
# better choice unless you really know what you’re doing with Django!

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # null is database-related. When a field has null=True it can store a database entry as NULL,meaning no value
    # blank is validation-related, if blank=True then a form will allow an empty value, whereas if blank = False then a value is required.
    # In practice, null and blank are commonly used together in this fashion so that a form allows an empty value and the database stores that value as NULL.
    age = models.PositiveIntegerField(null=True, blank=True)
# Note: A common gotcha to be aware of is that the field type dictates how to use these values. Whenever you have a string-based field like CharField or TextField, setting both null and blank as we’ve done will result in two possible values for “no data” in the database. Which is a bad idea. The Django convention is instead to use the empty string '', not NULL.
