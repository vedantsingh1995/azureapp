from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    #d = {}
    #subs_id = "xxxx"
    #d["subscription_id"] = subs_id
    #print (d)
    resp = flask.Response("Foo bar baz")
    resp.headers['Ocp-Apim-Subscription-Key'] = '3947aa67fd0c434a996c597775c04176'   
    return resp
