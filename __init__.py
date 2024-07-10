from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db = SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='secret-key'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
    
    db.init_app(app)
    app.app_context().push()

    login_manager=LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from .main import main as mainBlueprint
    app.register_blueprint(mainBlueprint)
    from .auth import auth as authBlueprint
    app.register_blueprint(authBlueprint)
    return app

