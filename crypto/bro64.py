# {"nonce": "TzMh7RxMJr8=", "ciphertext": "IynkKnGon3iK4oNSv59tqdLlpIowmfpiH88Vj1CjQBm3SvTcwTbrnY4q/UWKtJRu0M3v4sl+C0k8QFM8pdpyFCkE9Nur", "key": "Fidel_Alejandro_Castro_Ruz_Cuba!"}
# we need to find the cipher it was encrypted with, it uses a nonce and a key, it might be AES, ChaCha20, or Salsa20
# i think its ChaCha20, so we need to decrypt it with the nonce and key
# the nonce is base64 encoded, so we need to decode it, same as the ciphertext
import requests
from Crypto.Cipher import ChaCha20
import base64
site = "http://34.159.73.134:30707/"
data = requests.get(site).json()
nonce = data["nonce"]
ciphertext = data["ciphertext"]
key = data["key"]
nonce = base64.b64decode(nonce)
ciphertext = base64.b64decode(ciphertext)
key = key.encode()
cipher = ChaCha20.new(key=key, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)