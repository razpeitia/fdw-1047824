from django.db import models
import datetime

class Hit(models.Model):
    url = models.ForeignKey('Page')
    ip = models.IPAddressField()
    visit_datetime = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return '%s %s %s' % (self.ip, self.url, self.visit_datetime)

class Page(models.Model):
    url = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.url
