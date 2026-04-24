import json
from collections import Counter

def read_logs():
    with open('logs.json','r', encoding='utf-8') as archive:
        data = json.load(archive)
        for info_logs in data:
            print(f'IP: {info_logs['ip']} | Login: {info_logs['login']}')
              

read_logs()

    




