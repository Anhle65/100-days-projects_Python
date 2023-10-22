from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

def don():
    return render_template('don.html')
def dieu():
    return "good day"
@app.route("/<name>")
def in_detailed(name):
    if name == 'don':
        return don()
    elif name == 'dieu':
        return dieu()
    return "<h1>Hello</h1>"
if __name__ == '__main__':
    app.run(debug=True, port=80)