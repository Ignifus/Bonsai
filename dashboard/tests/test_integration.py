from random import randint

import redis
from dashboard import tasks
from django.test import TestCase
from dashboard.models import *


class IntegrationTestCase(TestCase):

    db = redis.Redis('localhost')

    def setUp(self):
        App.objects.create(name="test", apikey="testkey")

    def test_redis(self):
        v = randint(0, 9)
        self.db.set("redis_test", v)
        self.assertEqual(str(self.db.get("redis_test")), v)

    def test_celery(self):
        t = tasks.celery_test_task.delay()
        while not t.ready():
            pass
        self.assertEqual(self.db.get("celery_test"), b"ok")

    def test_sql(self):
        app = App.objects.get(name="test")
        self.assertEqual(app.apikey, "testkey")
