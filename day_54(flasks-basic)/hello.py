from flask import Flask
from markupsafe import escape
app = Flask(__name__)

def make_bold(function):
    def text_bold():
        return f"<b>{function()}</b>"
    return text_bold
def emphasized(function):
    def text_emp():
        return f"<em> {function()} <em>"
    return text_emp
@app.route("/")
def hello_world():
    return "<h1><p style='text-align: center'>Hello, World!</p></h1>" \
           "<p><img src='https://media2.giphy.com/media/1oBwBVLGoLteCP2kyD/giphy.gif' height=200></p>"
@app.route("/username/<name>")
def greet(name):
    return f"Good day! {name}"

@app.route("/bye")
@make_bold
@emphasized
def say_bye():
    return "Bye!"
if __name__ == "__main__":
    app.run(debug=True)