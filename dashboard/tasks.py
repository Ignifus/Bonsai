import json
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
    try:
        time = line.split(':')[0].split('IP')[0]
        ips = line.split(':')[0].split('IP')[1].split('>')
        garbage = line[line.index(':'):]
        searching_length = garbage.split('length')
        if len(searching_length) == 2:
            length = searching_length[1].strip()
        else:
            length = 0
    except IndexError:
        return {}

    return {"time": time, "source": ips[0], "dest": ips[1], "length": length}


@task(name="scan")
def scan(cmd):
    r_server = redis.Redis('localhost')
    for line in execute(cmd):
        if r_server.get('scanrunning') == b"no":
            return
        else:
            print(line, end='')
            Group("users").send({"text": json.dumps(parse(str(line)))})


@task(name="celery_test_task")
def celery_test_task(v):
    db = redis.Redis('localhost')
    db.set("celery_test", v)
