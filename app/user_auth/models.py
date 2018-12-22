from django.db import models
from social_django.models import UserSocialAuth

# Create your models here.
class UserSocialAuthData(UserSocialAuth):
    image_url = models.URLField(default='http://www.test.com/test/test/')
