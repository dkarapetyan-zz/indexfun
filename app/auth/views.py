from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required

from . import auth
from ..models import User, db
from .forms import LoginForm, RegistrationForm

__author__ = 'davidkarapetyan'


@auth.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.email = form.email.data,
        user.password(form.password.data)
        user.username(form.username.data)
        db.session.add(user)
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    else:
        return render_template('auth/register.html', form=form)
