from django.db import models


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
    timestamp = models.FloatField()
    app = models.ForeignKey(App, related_name='logs')

    class Meta:
        verbose_name_plural = "logs"

    def __str__(self):
        return self.description


class Http(models.Model):
    code = models.CharField(max_length=3)
    timestamp = models.FloatField()
    app = models.ForeignKey(App, related_name='httpcodes')

    class Meta:
        verbose_name_plural = "http"

    def __str__(self):
        return self.code + " " + self.route


class ServerLog(models.Model):
    cpu_usage = models.IntegerField()
    ram_usage = models.IntegerField()
    ram_total = models.IntegerField()
    hdd_usage = models.IntegerField()
    hdd_total = models.IntegerField()
    net_upload = models.IntegerField()
    net_download = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        verbose_name_plural = "serverlogs"
