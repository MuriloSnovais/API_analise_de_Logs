import json
from collections import Counter

def suspect_logs(dados_revebidos):
    suspect_ips = []
    final_ips = []

    for info_logs in dados_revebidos:
        if info_logs['login'] == 'failed':
            suspect_ips.append(info_logs['ip'])

    count = Counter(suspect_ips)
    for ips,times in count.items():
        if times >= 5:
            final_ips.append({"Suspect IP": f"{ips}", "Try": times})                 
    return final_ips
