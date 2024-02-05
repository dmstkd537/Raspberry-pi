from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello flask!"

if __name__ == "__main__":
    app.run(host = "192.168.0.181", port = "8080")
