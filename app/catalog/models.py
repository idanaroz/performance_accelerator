# https://www.youtube.com/watch?v=OvhoYbjtiKc&list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW&index=6

from datetime import datetime

from flask_login import UserMixin

from app import db, bcrypt, login_manager  # app/__init__.py


class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    link = db.Column(db.String(255), nullable=True)
    goal = db.Column(db.INTEGER, nullable=True)
    bodyweight = db.Column(db.BOOLEAN, default=True)
    static = db.Column(db.BOOLEAN, default=False)
    # Relationships
    meta_drill = db.Column(db.String(255), db.ForeignKey('meta_drills.value'))

    # tags
    # exercise_tools - should be the same concept as tags

    def __init__(self, name: str, link: str, goal: int,
                 static: bool, meta_drill: str, tag: str, bodyweight=True):
        self.name = name
        self.link = link
        self.goal = goal
        self.tag = tag
        self.bodyweight = bodyweight
        self.static = static
        self.meta_drill = meta_drill

    def __repr__(self) -> str:
        return f'The id is {self.id}, Name is {self.name} '

    @classmethod
    def create_exercise(cls, name, link, goal, bodyweight, static, tag, meta_drill):
        if not MetaDrill.query.filter_by(value=meta_drill).first():
            MetaDrill.create_metaDrill(value=meta_drill)
        exercise = cls(name=name, link=link, goal=goal, bodyweight=bodyweight, static=static, tag=tag,
                       meta_drill=meta_drill)
        db.session.add(exercise)
        db.session.commit()
        return exercise


class ExerciseTag(db.Model):
    __tablename__ = 'exercise_tags'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    value = db.Column(db.String(255), nullable=False)

    # Relationships
    exercise_id = db.Column(db.Integer(), db.ForeignKey('exercises.id'),
                            nullable=False)  # foreignKey reference to exercises id

    def __init__(self, artifact_id: int, value: str):
        self.artifact_id = artifact_id
        self.value = value


class MetaDrill(db.Model):
    __tablename__ = 'meta_drills'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    value = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, value: str):
        self.value = value

    @classmethod
    def create_metaDrill(cls, value):
        metadrill = cls(value=value)
        db.session.add(metadrill)
        db.session.commit()
        return metadrill


class Tool(db.Model):
    __tablename__ = 'tools'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tool_name = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, tool_name: str):
        self.tool_name = tool_name


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    user_email = db.Column(db.String(60), unique=True, index=True)
    user_password = db.Column(db.String(80))
    registration_date = db.Column(db.DateTime, default=datetime.now())

    def check_password(self, password):
        return bcrypt.check_password_hash(self.user_password, password)

    @classmethod
    def create_user(cls, user, email, password):
        user = cls(user_name=user,
                   user_email=email,
                   user_password=bcrypt.generate_password_hash(password).decode('utf-8'))
        db.session.add(user)
        db.session.commit()
        return user


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
