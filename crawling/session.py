import requests

with s = requests.Session() as s:
    req = s.get('https://www.dogdrip.net')
    html = req.text
    header = req.headers
    status = req.status_code
    is_ok = req.ok
