from flask import current_app, flash
from flask.ext.bcrypt import check_password_hash, generate_password_hash
from flask.ext.login import UserMixin, AnonymousUserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from . import db, login_manager
from .mail import send_email


# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#
#     def __repr__(self):
#         return '<Role %r>' % self.name

class BankAccount(db.Model):
    __tablename__ = 'bank_accounts'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    bank_name = db.Column(db.String(64))
    bank_account_hash = db.Column(db.String(128), unique=True)
    bank_password_hash = db.Column(db.String(128))

    def __init__(self, bank_name=None, bank_account_hash=None,
                 bank_password_hash=None):
        self.bank_name = bank_name
        self.bank_account_hash = generate_password_hash(bank_account_hash)
        self.bank_password_hash = generate_password_hash(bank_password_hash)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class User(db.Model, UserMixin, AnonymousUserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    user_password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, index=True)
    confirmed = db.Column(db.Boolean, default=False)

    def __init__(self, username=None, userpassword=None, email=None,
                 confirmed=False, bank_account=None, bank_password=None):
        self.username = username
        self.password_hash = generate_password_hash(userpassword)
        self.email = email
        self.confirmed = confirmed
        self.bank_account = generate_password_hash(bank_account)
        self.bank_password = generate_password_hash(bank_password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        return True

    def send_confirmation(self):
        token = self.generate_confirmation_token()
        send_email(self.email, 'Confirm Your Account',
                   'auth/confirm_email',
                   user=self, token=token)
        flash('A confirmation email has been sent via email. Please click'
              ' its enclosed link to enable your account and login.')

    def __repr__(self):
        return '<User %r>' % self.username


# for flask-login
@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))
