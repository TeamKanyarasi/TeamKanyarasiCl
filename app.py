from flask import Flask

app = Flask(__name__)

@app.route("/home", methods=["GET"])
def helloWorld():
    return "Hello World"


if(__name__) == "__main__":
    app.run(port=80, debug=True)
