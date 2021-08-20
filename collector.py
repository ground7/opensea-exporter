from flask import Response, Flask
import prometheus_client
from prometheus_client import Gauge
import requests # switch this to flask?

app = Flask(__name__)

# Set up array of gauges to handle values from the api
graphs = {}
graphs['eth'] = Gauge('opensea_eth_value', 'The current value of ethereum according to OpenSea')

# Go to the root domain to request the eth price from opensea (will set up a timer or something later)
# Root is at http://localhost:9000/
@app.route("/")
def process_request():
    url = "https://api.opensea.io/api/v1/asset/0xc36cf0cfcb5d905b8b513860db0cfe63f6cf9f5c/46958966635089507957945695825584013180928/"
    response = requests.request("GET", url)
    eth_price = response.json()["collection"]["payment_tokens"][0]["usd_price"]
    graphs['eth'].set(eth_price)   # Set to current value of eth in usd
    return str(eth_price)

# Go to http://localhost:9000/metrics to see the prometheus endpoint
@app.route("/metrics")
def requests_count():
    res = []
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")