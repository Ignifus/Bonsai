from threading import Timer
import os.path
import requests

def parse_logs(filename):
    page_logs = []
    http_logs = []

    if(os.path.isfile(filename)): 

        with open(filename) as f:
            lines = f.readlines()
        
        for line in lines:
            parts = line.split('||')
            if(len(parts) != 2):
                continue
            log = parts[1].split(' - ')
            level = log[0].strip()

            if(level == 'INFO'):
                page_logs.append(log[1])

            if(level == 'HTTP'):
                http_logs.append(log[1])

    page_logs = '"logs":[' + ','.join(page_logs) + ']'
    http_logs = '"http":[' + ','.join(http_logs) + ']'

    return [page_logs, http_logs]

def send_logs(app_name, api_key, filename):
    parsed = parse_logs(filename)
    json = '{"app":"' + app_name + '", "key":"' + api_key + '",' + parsed[0] + ',' + parsed[1] + '}'
    headers = {'content-type': 'application/json'}
    r = requests.post("https://bonsai.ignifus.com/receive-logs/", headers=headers, data=json)
    print(r.status_code, r.reason, json)
    #open('index.html', 'w').write(r.text)

def init(app_name, api_key, filename):
    send_logs(app_name, api_key, filename)
    Timer(10.0, init, [app_name, api_key, filename]).start()

if __name__ == "__main__":
    init("TestAppA", "sarasacosmica", "logs_a.log")