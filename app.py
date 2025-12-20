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
    email = db.Column(db.String(150), unique=True)

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

@app.route('/register')
def register():
    return render_template('entry_page.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)