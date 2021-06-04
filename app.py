from flask import Flask, url_for, redirect, session, render_template
from flask_login import LoginManager, login_required, logout_user
from datetime import timedelta
import dj_database_url
from models import db, User, VisitingTime
from views.login import login
from views.result import result
from views.admin import admin
# from werkzeug.security import generate_password_hash
app = Flask(__name__)
app.register_blueprint(login)
app.register_blueprint(result)
app.register_blueprint(admin)

app.config['SECRET_KEY'] = 'Thisismysecretkeyandsupposenottobeknownfromothers'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://PDN7R7LWTe:FUjyTWF6nO@remotemysql.com/PDN7R7LWTe'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 1
# heroku connect database settings
DATABASES = {
    'default': 'mysql://PDN7R7LWTe:FUjyTWF6nO@remotemysql.com/PDN7R7LWTe'
}
DATABASES['default'] = dj_database_url.config(
    default='mysql://PDN7R7LWTe:FUjyTWF6nO@remotemysql.com/PDN7R7LWTe',
)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login.user_login"
login_manager.login_message = "您沒有權限，請先登入"

# with app.app_context():
    # test = db.session.query(VisitingTime).filter(except_all(VisitingTime.date.startswith("Sat"))).all()
        
    # a = News.query.filter_by(newsId=509).first()
    # db.session.delete(a)
    # db.session.commit()
    # user = User(name="John", password=generate_password_hash("testpassword", method="sha256"))
    # db.session.add(user)
    # db.session.commit()
    # test = User.query.all()
    # print(test)
@login_manager.user_loader
def load_user(id):
    user = User.query.get(id)
    return user

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(hours=1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == 'main':
    db.create_all()
    app.run()