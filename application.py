from flask import Flask
import os
from flask import Response
app = Flask(__name__)

@app.route("/")
#@app.after_request
def hello():
    #d = {}
    #subs_id = "xxxx"
    #d["subscription_id"] = subs_id
    #print (d)
    #resp = Flask.Response("Foo bar baz")
    print (os.environ["test"])
    return Response(headers={'Access-Control-Allow-Origin':'*'})
    #resp.headers['Ocp-Apim-Subscription-Key'] = 'sjhdsdjs'
    #return resp
    #return "test"
