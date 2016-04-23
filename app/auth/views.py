from flask import render_template, redirect, url_for, flash, request
from flask.ext.login import login_user, logout_user, login_required, \
    current_user

from . import auth
from .forms import LoginForm, RegistrationForm
from ..models import User, db

__author__ = 'davidkarapetyan'


@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('Invalid username.')
        elif not user.verify_password(form.password.data):
            flash('Invalid password.')
        else:
            login_user(user, form.remember_me.data)
            flash('Successfully logged in.')
            return redirect(request.args.get('next') or url_for('main.index'))
    else:
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
        user = User(username=form.username.data, password=form.password.data,
                    email=form.email.data)
        if User.query.filter_by(email=user.email):
            flash("A user with this information has already registered. If "
                  "you've confirmed this account, you may now log in")
            return redirect(url_for('auth.login'))
        db.session.add(user)
        db.session.commit()
        user.send_confirmation()
        return redirect(url_for('auth.login'))
    else:
        return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if not current_user.confirmed:
        if current_user.confirm(token):
            current_user.confirmed = True
            db.session.add(current_user)
            db.session.commit()
            flash('You have confirmed your account. You may now log in.')
        else:
            current_user.send_confirmation()
            flash('The confirmation link is invalid or has expired. Another'
                  'has been sent. ')
    return redirect(url_for('main.index'))

# @auth.before_app_request
# def before_request():
#     if request.path[:5] == '/auth':
#         flash(
#             "Only server requests to this url are allowed, not user
# requests.")
#         return redirect(url_for('main.index'))
