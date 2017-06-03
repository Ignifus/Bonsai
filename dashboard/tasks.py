import subprocess
import redis
from celery.task import task
from channels import Group


def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, b''):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)


def parse(line):
    #TODO
    return {"text": line}


@task(name="scan")
def scan(cmd):
    r_server = redis.Redis('localhost')
    for line in execute(cmd):
        if r_server.get('listeners') == b'0':
            r_server.set('scanrunning', 'no')
            return
        else:
            print(line, end='')
            Group("users").send(parse(line))


@task(name="celery_test_task")
def celery_test_task(v):
    db = redis.Redis('localhost')
    db.set("celery_test", v)
