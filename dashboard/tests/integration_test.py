import redis
from celery.task import task
from django.test import TestCase
from dashboard.models import *


@task(name="celery_test_task")
def celery_test_task(db):
    db.set("celery_test", "ok")


class IntegrationTestCase(TestCase):

    db = redis.Redis('localhost')

    def setUp(self):
        App.objects.create(name="test", apikey="testkey")

    def test_redis(self):
        self.db.set("redis_test", "ok")
        self.assertEqual(self.db.get("redis_test"), b"ok")

    def test_celery(self):
        celery_test_task.apply(self.db)
        self.assertEqual(self.db.get("celery_test"), b"ok")

    def test_sql(self):
        app = App.objects.get(name="test")
        self.assertEqual(app.apikey, "testkey")
