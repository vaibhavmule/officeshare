from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class office(models.Model):
    user = models.ForeignKey(User)
    location = models.CharField(max_length=150)
    rent = models.IntegerField()
    people = models.IntegerField()
    description = models.TextField(max_length=1000)
    date = models.DateField(auto_now=True)
    picture = models.ImageField(upload_to='office_images', blank=True)

    def __unicode__(self):
        return self.location

class messages(models.Model):
    message = models.TextField(max_length=100)
    receiverid = models.IntegerField()
    senderid = models.IntegerField()
    seen = models.IntegerField()

    def __unicode__(self):
        return self.message
