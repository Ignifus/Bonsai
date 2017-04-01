from django.db import models
from django.utils import timezone


class App(models.Model):
    name = models.CharField(max_length=40)
    apikey = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "apps"

    def __str__(self):
        return self.name


class Log(models.Model):
    method = models.CharField(max_length=40)
    description = models.CharField(max_length=60)
    timestamp = models.IntegerField(default=timezone.now)
    app = models.ForeignKey(App, related_name='logs')

    class Meta:
        verbose_name_plural = "logs"

    def __str__(self):
        return self.description + " " + self.timestamp.__str__()


class Http(models.Model):
    code = models.CharField(max_length=3)
    route = models.CharField(max_length=200)
    timestamp = models.IntegerField()
    app = models.ForeignKey(App, related_name='httpcodes')

    class Meta:
        verbose_name_plural = "http"

    def __str__(self):
        return self.code + " " + self.route + " " + self.timestamp.__str__()
