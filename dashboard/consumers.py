from channels import Group
from dashboard import tasks
import redis


def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group('users').add(message.reply_channel)

    r_server = redis.Redis('localhost')

    if r_server.get('scanrunning') != b"yes":
        r_server.set('scanrunning', 'yes')
        r_server.set('listeners', 1)
        tasks.scan.delay(["tcpdump", "-i", "eth0", "-tt", "-nn"])
    else:
        r_server.incr('listeners')


def ws_disconnect(message):
    r_server = redis.Redis('localhost')
    r_server.decr('listeners')

    Group('users').discard(message.reply_channel)

