from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    #d = {}
    #subs_id = "xxxx"
    #d["subscription_id"] = subs_id
    #print (d)
    resp = Flask.Response("Foo bar baz")
    print  (ConfigurationManager.AppSettings["test"])
    #resp.headers['Ocp-Apim-Subscription-Key'] = ''   
    return resp
