from flask import Blueprint, render_template, redirect, url_for, request, flash, get_flashed_messages, session, make_response
from .models import db, Admin, User
from flask_login import login_required, logout_user, login_user


main = Blueprint('main', __name__)


@main.route('/')
def common_home():
    welcome_msg = "Welcome Guest, Login to Join family"
    return render_template('common_home.html', welcome_msg = welcome_msg)

@main.route('/admin_home')
@login_required
def admin_home():
    welcome_msg = "Welcome, Admin"
    return render_template('admin_home.html', welcome_msg=welcome_msg)

@main.route('/admin_register', methods=['POST', 'GET'])
def admin_register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        existing_admin = Admin.query.filter((Admin.username == username) | (Admin.email == email)).first()
        if existing_admin:
            flash("Username or email already exists", "warning")
            return redirect(url_for('main.admin_register'))
        else:
            add_admin = Admin(username=username, email=email, password=password)
            db.session.add(add_admin)
            db.session.commit()
            flash("Admin account created successfully", "success")
            return redirect(url_for('main.admin_login'))
    return render_template('admin_register.html')

@main.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    welcome_msg = "Happy Login :)"
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_admin = Admin.query.filter_by(username=username).first()
        if existing_admin and existing_admin.check_password(password):
            login_user(existing_admin)
            return redirect(url_for('main.admin_home'))
        else:
            flash("Username or password is incorrect", "warning")
            return redirect(url_for('main.admin_login'))
    return render_template('admin_login.html', welcome_msg=welcome_msg)

@main.route('/admin_logout')
@login_required
def admin_logout():
    logout_user()
    session.clear()
    flash("You have been logged out", "info")
    response = make_response(redirect(url_for('main.common_home')))
    response.set_cookie('session', '', expires=0)
    return response

@main.route('/admin_add_user', methods=['GET', 'POST'])
@login_required
def admin_add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash("Username or email already exists", "warning")
            return redirect(url_for('main.admin_add_user'))
        else:
            add_user = User(username=username, email=email, password=password)
            db.session.add(add_user)
            db.session.commit()
            flash("User account created successfully", "success")
            return redirect(url_for('main.admin_add_user'))
    users = User.query.all()
    return render_template('admin_add_user.html', users=users)

@main.route('/admin_delete_user/<int:user_id>', methods=['POST'])
@login_required
def admin_delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('main.admin_add_user'))



@main.route('/admin_add_product')
@login_required
def admin_add_product():
    return render_template('admin_add_product.html')

@main.route('/admin_edit_product')
@login_required
def admin_edit_product():
    return render_template('admin_edit_product.html')


# user registration
@main.route('/user_register', methods=['POST', 'GET'])
def user_register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash("Username or email already exists", "warning")
            return redirect(url_for('main.user_register'))
        else:
            add_user = User(username=username, email=email, password=password)
            db.session.add(add_user)
            db.session.commit()
            flash("Admin account created successfully", "success")
            return redirect(url_for('main.user_login'))
    return render_template('user_register.html')

# user login
@main.route('/user_login', methods=['GET', 'POST'])
def user_login():
    welcome_msg = "Happy Login :)"
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user and existing_user.check_password(password):
            login_user(existing_user)
            return redirect(url_for('main.user_home'))
        else:
            flash("Username or password is incorrect", "warning")
            return redirect(url_for('main.user_login'))
    return render_template('user_login.html', welcome_msg=welcome_msg)

# user logout
@main.route('/user_logout')
@login_required
def user_logout():
    logout_user()
    session.clear()
    flash("You have been logged out", "info")
    response = make_response(redirect(url_for('main.common_home')))
    response.set_cookie('session', '', expires=0)
    return response

# user home
@main.route('/user_home')
@login_required
def user_home():
    return render_template('user_home.html')
