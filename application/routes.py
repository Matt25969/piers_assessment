from flask import render_template, redirect, url_for
from application import app, db
from application.models import users, card_list, deck_list
from application.forms import RegisterForm, LoginForm, CreateCard, Createdeck
from application import password_hash as pw

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
		return redirect(url_for('home'))

	form = LoginForm()
	if form.validate_on_submit():
		user = users.query.filter_by(user_name=form.user_name.data).first()
		if user and pw.verify_password(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')

			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('home'))

	return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
		return redirect(url_for('home'))
    newuser = RegisterForm()
    if newuser.validate_on_submit():
        hashed = pw.hash_password(RegisterForm.password.data)
        user = users(
            user_name=RegisterForm.user_name.data,
            first_name=RegisterForm.first_name.data,
            last_name=RegisterForm.last_name.data,
            password=hashed
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        print(RegisterForm.errors)
        return render_template('register.html', title='Register', form=RegisterForm)

@app.route('/dashboard')
@login_required
def dashboard():
	return render_template('dashboard.html', title='Dashboard')
