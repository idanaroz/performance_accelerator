import uuid

from app import create_app, db,auth
from app.catalog.models import Exercise, ExerciseTag

if __name__ == '__main__':
    flask_app = create_app('dev')

    with flask_app.app_context():
        db.create_all()

        # link = "https://www.youtube.com/watch?v=KpeAMHINKHQ"
        # tag ="working"
        # exercise = Exercise("Front Lever", link,
        #                     goal=30, static=True, tag=tag)
        # tag = ExerciseTag(1, "Strength")
        # db.session.add_all([tag])
        # db.session.commit()
        # all = Exercise.query.all()
        # first = Exercise.query.first()
        # filter_data = Exercise.query.filter_by(name="Tuck Planche").limit(5).all()
        # tags = ExerciseTag.query.filter_by(artifact_id=1).all()
        # print(filter_data)

    flask_app.run(debug=True)
