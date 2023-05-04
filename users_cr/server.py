from flask_app import app
from flask_app.controllers import users
# import class User from our user.py to information to the template
# from user import User
# -------------
# or use import user since it is in the same file
# imports the entire file 
# import user


# app = Flask(__name__) initilized in our __init__.py 









if __name__ =='__main__':
    app.run(debug=True, port=5001)