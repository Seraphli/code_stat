import requests
import json
from datetime import datetime, timezone
import random
import time

API_KEY = 'SFMyNTY.YkdWMlpXeDFjQT09IyNNelUwTmc9PQ.Kji3DPPb2TKPPbfK2RnqSjHs22kDFMUJWmcRFS7j8nM'
url = 'https://codestats.net/api/my/pulses/'
# Adding empty header as parameters are being sent in payload
headers = {
    'content-type': 'application/json',
    'X-API-Token': API_KEY,
    'user-agent': 'code-stats-sublime/1.1.0',
}
languages = ['Python', 'C++']
xp_limit = [5, 15]

while True:
    local_time = datetime.now(timezone.utc).astimezone()
    if 9 <= local_time.hour <= 19:
        time_str = local_time.replace(microsecond=0).isoformat()
        payload = {
            'coded_at': time_str,
            'xps': [
                {
                    'language': random.choice(languages),
                    'xp': random.randint(xp_limit[0], xp_limit[1])
                },
            ]
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if r.status_code != 201:
            print(r.content)
    time.sleep(1)
