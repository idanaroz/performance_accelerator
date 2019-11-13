from flask import render_template, flash, redirect, url_for

from app.auth import authentication as at
from app.auth.forms import RegistrationForm
from app.catalog.models import User


@at.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm()
    if form.validate_on_submit():  # check that it is Post request and validate the data
        User.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data
        )
        flash('Registration Successful')
        return redirect(url_for('authentication.login_user'))

    return render_template('registration.html', form=form)


@at.route('/login', methods=['GET', 'POST'])
def login_user():
    return render_template('login.html')
