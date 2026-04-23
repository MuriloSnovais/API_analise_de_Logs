import json

with open('logs.json','r') as archive:
    for line in archive:
        print(line.strip())

