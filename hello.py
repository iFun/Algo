from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
@app.route("/asd")    
def asd():
    return "asd"

if __name__ == "__main__":
    app.run()