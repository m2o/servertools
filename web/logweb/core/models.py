from django.db import models

class IP(models.Model):
    address = models.CharField(max_length=200)

    def __unicode__(self):
        return '{}'.format(self.address)

class Access(models.Model):
    ip = models.ForeignKey(IP)
    time = models.DateTimeField()

    def __unicode__(self):
        return '{}-{}'.format(self.ip,self.time)
