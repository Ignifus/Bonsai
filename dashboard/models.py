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
        return self.code


class ServerLog(models.Model):
    cpu_usage = models.FloatField()
    ram_usage = models.FloatField()
    ram_total = models.FloatField()
    hdd_usage = models.FloatField()
    hdd_total = models.FloatField()
    net_upload = models.FloatField()
    net_download = models.FloatField()
    net_upload_total = models.FloatField()
    net_download_total = models.FloatField()
    timestamp = models.FloatField()

    class Meta:
        verbose_name_plural = "serverlogs"
