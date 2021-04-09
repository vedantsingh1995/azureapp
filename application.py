from flask import Flask
import os
from flask import Response
app = Flask(__name__)

@app.route("/",methods = ['POST', 'GET'])
#@app.after_request
def hello():
    #d = {}
    #subs_id = "xxxx"
    #d["subscription_id"] = subs_id
    #print (d)
    #resp = Flask.Response("Foo bar baz")
    head = (os.environ["test"])
    return Response(headers={'Ocp-Apim-Subscription-Key': head})
    #resp.headers['Ocp-Apim-Subscription-Key'] = 'sjhdsdjs'
    #return resp
    #return "test"
