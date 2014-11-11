from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class office(models.Model):
    user = models.ForeignKey(User)
    location = models.CharField(max_length=150)
    rent = models.IntegerField()
    date = models.DateField(auto_now=True)
    picture = models.ImageField(upload_to='office_images', blank=True)

    def __unicode__(self):
        return self.location