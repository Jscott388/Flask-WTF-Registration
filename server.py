from flask import Flask, render_template, redirect, request, flash
from flask_wtf import Form
from wtforms import TextField, validators, StringField, SubmitField, PasswordField, ValidationError

DEBUG = True
app = Flask(__name__)
app.config.from_object('config')

def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error for %s - %s" % (
                getattr(form, field).label.text,error), 'error')

class RegistrationForm(Form):
    email = StringField('Email:', [validators.InputRequired(),validators.Regexp(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$', message='Please enter a valid email.')])
    firstname = StringField('First Name:', [validators.InputRequired(), validators.Regexp(r'^[a-zA-Z]+$', message='Must contain only letters')])
    lastname = StringField('Last Name:', [validators.InputRequired(),validators.Regexp(r'^[a-zA-Z]+$', message='Must contain only letters')])
    password = PasswordField('Password:', [validators.InputRequired(),  validators.Length(min=8, message='Password must be at least 8 characters long.'), validators.EqualTo('confirmpassword', message='Passwords must match'), validators.Regexp(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,25}$', message='Must have at least 1 uppercase letter, 1 lowercase letter, and 1 numeric value')])
    confirmpassword = PasswordField('Confrim Password:')
    submit = SubmitField('submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()

    print form.errors
    if request.method == 'POST':

        if form.validate_on_submit():
            flash('Thanks for registration')
        else:
            flash_errors(form)
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()
