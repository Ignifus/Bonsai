import pytest
import redis


def test_redis():
    db = redis.Redis('localhost')
    db.set("test", "test")
    assert db.get("test") == b"test"
