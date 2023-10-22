from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def preface():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    name = request.form["username"]
    password = request.form["password"]
    print(f"<h1>Name: {name}, Password: {password}</h1>")
    return "The answer is recorded"
if __name__ == '__main__':
    app.run(debug=True)
