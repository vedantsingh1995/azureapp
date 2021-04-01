from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    d = {}
    subs_id = "xxxx"
    d["subscription_id"] = subs_id
    print (d)	
    return "<h1>Hello World!</h1>"
