from flask import session, redirect
from functools import wraps


def login_required(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        # if logged in, call original function with original arguments
        if session.get('loggedIn') == True:
            return func(*args, **kwargs)

        return redirect('/login')

    return wrapped_function


# Python decorator example in JavaScript

# function login_required(func) {
#   function wrapped_function() {
#     console.log('wrapper');

#     // func(*args, **kwargs)
#     return func(...arguments);
#   }

#   return wrapped_function;
# }

# // @login_required
# // def callback():
# const callback = login_required(() => {
#   console.log('hello');
# });

# callback();
