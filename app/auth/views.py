from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, \
    current_user

from . import auth
from ..models import User, db
from .forms import LoginForm, RegistrationForm
from ..mail import send_email

__author__ = 'davidkarapetyan'


@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password.')
        if not user.confirmed:
            redirect(url_for('auth.send_confirmation'))
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
        return redirect(url_for('auth.login'))
    else:
        return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        current_user.confirmed = True
        db.session.add(current_user)
        db.session.commit()
        flash('You have confirmed your account. You may now log in.')
    else:
        flash('The confirmation link is invalid or has expired.')
        return redirect(url_for('auth.unconfirmed'))
    return redirect(url_for('main.index'))


# @auth.before_app_request
# def before_request():
#     if request.path[:5] == '/auth':
#         flash(
#             "Only server requests to this url are allowed, not user
# requests.")
#         return redirect(url_for('main.index'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous():
        return redirect('main.index')
    else:
        flash("Please confirm your account")
        return redirect(url_for('auth.send_confirmation'))


@auth.route('/confirm')
@login_required
def send_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account', 'auth/confirm_email',
               user=current_user, token=token)
    flash('A confirmation email has been sent via email. Please click'
          ' its enclosed link to enable your account and login.')
    return redirect(url_for('main.index'))
