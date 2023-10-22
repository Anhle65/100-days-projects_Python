from flask import Flask, render_template, request, redirect, url_for
import sqlite3
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"

# create the extension
db = SQLAlchemy()
# initialize the app with the extension
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# all_books = []

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_books = result.scalars().all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        new_book = Books(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating']
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete(id):
    # book_position = request.args.get('id')
    delete_book = db.get_or_404(Books, id)
    db.session.delete(delete_book)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/edit_rating", methods=["GET", "POST"])
def edit_rating():
    if request.method == "POST":
        navigate = request.form['id']
        print(navigate)
        rating_book = db.get_or_404(Books, navigate)
        rating_book.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    print(book_id)
    book_selected = db.get_or_404(Books, book_id)
    return render_template('edit.html', book=book_selected)

if __name__ == "__main__":
    app.run(debug=True)

