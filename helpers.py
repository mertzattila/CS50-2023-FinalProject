import re
from flask import redirect, session
from functools import wraps


def is_valid_email(email):
    # Define a regex pattern for a basic email validation.
    pattern = r'^\S+@\S+\.\S+$'
    return re.match(pattern, email) is not None

def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function



def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','gif'])
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS