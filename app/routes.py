from flask_login.mixins import UserMixin
from app import app, db, bcrypt, login_manager
from flask import render_template
from flask import url_for 
from flask import flash 
from flask import redirect
from flask import request, abort
from flask import jsonify
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import or_, and_
from flask_sqlalchemy import Pagination
from app.forms import (UserRegistrationForm, UserLoginForm, UserUpdateAccountForm, CashierRegistrationForm,CashierLoginForm)
from app.models import (User)

@app.route('/',methods = ['POST', 'GET'])
def home():
    return redirect('coc')

@app.route('/coc',methods = ['POST', 'GET'])
def coc():
    return render_template('COC.html')
