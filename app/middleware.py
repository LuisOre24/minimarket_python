from functools import wraps
from flask_login import current_user
from flask import render_template

def administrator(f):
    @wraps(f)
    def access_administrator(*args, **kwargs):
        if current_user.rol_id == 1:
            return f(*args, **kwargs)
        else:
            return render_template('views/error/401.html')
    return access_administrator


def storer(f):
    @wraps(f)
    def access_storer(*args, **kwargs):
        if current_user.rol_id == 2:
            return f(*args, **kwargs)
        else:
            return render_template('views/error/401.html')
    return access_storer


def seller(f):
    @wraps(f)
    def access_seller(*args, **kwargs):
        if current_user.rol_id == 3:
            return f(*args, **kwargs)
        else:
            return render_template('views/error/401.html')
    return access_seller


