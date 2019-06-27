from functools import wraps
from flask import redirect, session, render_template


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session['uid']:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function
