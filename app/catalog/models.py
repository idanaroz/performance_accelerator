from sqlalchemy.orm import backref
# https://www.youtube.com/watch?v=OvhoYbjtiKc&list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW&index=6

from app import db
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from app import db, bcrypt  # app/__init__.py

Base = declarative_base()


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

class Tool(db.Model):
    __tablename__ = 'tools'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tool_name = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, tool_name: str):
        self.tool_name = tool_name
