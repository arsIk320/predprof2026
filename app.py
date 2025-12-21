from flask import Flask, render_template, request, redirect, url_for
import datetime
from hashlib import sha384
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)  
app.config['SECRET_KEY'] = 'b791482a6365226b05c230e51381356b337bffe7abd43134a00fceb78e72c234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///canteencontrol.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    middle_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    phone_number = db.Column(db.String(150))
    date_of_birth = db.Column(db.String(150))
    role = db.Column(db.String(150))
    admin = db.Column(db.Integer)
    password = db.Column(db.String(150))



@app.route("/main")
def main():
    return render_template('main_page.html')


@app.route('/entry', methods=['POST', 'GET'])
def entry():
    if request.method == 'POST':
        login = request.form.get('login')
        password = str(sha384(request.form.get('password').encode()))
        print(login, password)

        return redirect(url_for('entry'))
        
    return render_template('entry_page.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        middle_name = request.form.get('middle_name')
        date_of_birth = request.form.get('dob')
        category = request.form.get('category')
        login = request.form.get('login')
        email = request.form.get('email')
        password = request.form.get('password')
        phone_number = request.form.get('phone_number')

        user_by_email = Users.query.filter_by(email=email).first()
        user_by_login = Users.query.filter_by(login=login).first()

        if not user_by_email and not user_by_login:
            new_user = Users(
                login = login,
                first_name = first_name,
                middle_name = middle_name,
                last_name = last_name,
                email = email,
                phone_number = phone_number,
                date_of_birth = date_of_birth,
                role = category,
                password = password
            )

            db.session.add(new_user)
            db.session.commit()

        return redirect(url_for('register'))



    return render_template('register_page.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)