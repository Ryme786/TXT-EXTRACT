from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "SAMEER JI ❤️ Flask Server Working on Port 8080!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
