from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap4

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
bootstrap = Bootstrap4(app)

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email("Not a valid email")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message="Your password need at least 8 characters")])
    submit = SubmitField('Login')


app.secret_key = "any-string-you-want-just-keep-it-secret"
EMAIL = 'admin@email.com'

PASS = '12345678'

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == EMAIL and login_form.password.data == PASS:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)

@app.route("/denied")
def denied():
    return render_template('denied.html')

@app.route("/success")
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
