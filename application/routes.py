from flask import render_template, redirect, url_for
from application import app, db
from application import models
from application import forms
from application import password_hash as pw

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/login')
def login():
	return render_template('login.html', title='Login')

@app.route('/register')
def register():
    newuser = forms.RegisterForm()
    hashed = pw.hash_password(forms.RegisterForm.password.data)
    if newuser.validate_on_submit():
        user = models.users(
            user_name=forms.RegisterForm.user_name.data,
            first_name=forms.RegisterForm.first_name.data,
            last_name=forms.RegisterForm.last_name.data,
            password=hashed
            admin=False
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        print(forms.RegisterForm.errors)
        return render_template('register.html', title='Register', form=forms.RegisterForm)

	return render_template('register.html', title='Register')

@app.route('/dashboard')
def register():
	return render_template('dashboard.html', title='Dashboard')