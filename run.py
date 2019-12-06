from app import create_app, db
from app.catalog.models import User

flask_app = create_app('dev')

with flask_app.app_context():
    db.create_all()
    if not User.query.filter_by(user_name='harry').first():
        User.create_user(user='harry',
                         email="harry@potters.com",
                         password="secret")
flask_app.run()
