from app import create_app, db
from app.catalog.models import User, Exercise

flask_app = create_app('dev')


def upsert_to_db():
    # create exercises
    if not Exercise.query.filter_by(name='pseudo push up').first():
        Exercise.create_exercise(name='pseudo push up', link="https://www.youtube.com/watch?v=odcPqBOlJhI",
                                 goal=10, bodyweight=True, static=False, tag="upper body",
                                 meta_drill="hand stand push up")
    if not Exercise.query.filter_by(name='ring archers').first():
        Exercise.create_exercise(name='ring archers', link="https://www.youtube.com/watch?v=H4mKc0y55to",
                                 goal=5, bodyweight=True, static=False, tag="upper body", meta_drill="one hand chin up")
    if not Exercise.query.filter_by(name='ring archers').first():
        Exercise.create_exercise(name='ring archers', link="https://www.youtube.com/watch?v=H4mKc0y55to",
                                 goal=5, bodyweight=True, static=False, tag="upper body", meta_drill="one hand chin up")
    if not Exercise.query.filter_by(name='tuck front lever').first():
        Exercise.create_exercise(name='tuck front lever', link="https://www.youtube.com/watch?v=2jYkF-RYZjQ",
                                 goal=30, bodyweight=True, static=True, tag="upper body", meta_drill="front lever")
    if not Exercise.query.filter_by(name='tuck planche').first():
        Exercise.create_exercise(name='tuck planche', link="https://www.youtube.com/watch?v=KpeAMHINKHQ",
                                 goal=30, bodyweight=True, static=True, tag="upper body", meta_drill="planche")


with flask_app.app_context():
    db.create_all()
    if not User.query.filter_by(user_name='harry').first():
        User.create_user(user='harry',
                         email="harry@potters.com",
                         password="secret")

    upsert_to_db()

if __name__ == '__main__':
    flask_app.run()