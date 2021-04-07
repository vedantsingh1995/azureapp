from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    #d = {}
    #subs_id = "xxxx"
    #d["subscription_id"] = subs_id
    #print (d)
    resp = flask.Response("Foo bar baz")
    resp.headers['Ocp-Apim-Subscription-Key'] = ''   
    return resp
