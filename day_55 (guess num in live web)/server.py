from flask import Flask
import random
app = Flask(__name__)

def bold_text(function):
    def wrapp(*args):
        return f"<h1 style='text-align:center'><b>{function()} </b></h1>"
    return wrapp
answer = int(random.randrange(0,10))


@app.route("/")
@bold_text
def introduction():
    return "<p>Guess a number between 0 and 9</p>"\
            "<img src='https://media4.giphy.com/media/jzcre2tWBvFg95kCqS/giphy.webp' height=500>"

@app.route("/<int:number>")
def guessing(number):
    if number > answer:
        return f"<p><h1 style='text-align:center'>It's higher than expected</h1></p>" \
               f"<img src='https://media3.giphy.com/media/3oEduOnl5IHM5NRodO/giphy.gif?cid=ecf05e47rx8r7u7bvp8lwb3iogu8gipuk4dou39igzwnxid2&ep=v1_gifs_gifId&rid=giphy.gif&ct=g' height=200>"
    elif number< answer:
        return f"<p><h1 style='text-align:center'>It's lower than expected</h1></p>"\
                f"<img src='https://media0.giphy.com/media/gw3xhDHNElAluY3S/giphy.gif?cid=ecf05e472wa4k1hllkb9c5lnsgojbt38166o1i1kiryppyff&ep=v1_gifs_related&rid=giphy.gif&ct=g' height=200>"
    else:
        return f"<p><h1 style='text-align:center'>It's true</h1></p>"\
                f"<img src='https://media3.giphy.com/media/ToMjGpNV9CLR1DNY6k0/giphy.gif?cid=ecf05e47gi6fh7gxgeiqbqtasayi7bd1mpf2zf7di0hbctzf&ep=v1_gifs_related&rid=giphy.gif&ct=g' height=200>"


if __name__ == '__main__':
    app.run(debug=True)
