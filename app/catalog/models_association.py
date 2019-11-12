# from sqlalchemy.orm import backref
# # https://www.youtube.com/watch?v=OvhoYbjtiKc&list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW&index=6
#
# from app import db
# from sqlalchemy.ext.declarative import declarative_base
#
#
# Base = declarative_base()
#
#
# association_table = db.Table('association', db.metadata,
#     db.Column('exercises_id', db.Integer, db.ForeignKey('exercises.id')),
#     db.Column('exercise_tags_id', db.Integer, db.ForeignKey('exercise_tags.id'))
# )
#
# class Exercise(db.Model):
#     __tablename__ = 'exercises'
#
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(80), nullable=False, unique=True)
#     link = db.Column(db.String(255), nullable=True)
#     goal = db.Column(db.INTEGER, nullable=True)
#     bodyweight = db.Column(db.BOOLEAN, default=True)
#     static = db.Column(db.BOOLEAN, default=False)
#     tags = db.relationship("ExerciseTag", secondary=association_table, back_populates="exercises")
#
#     # exercisetool
#     # MetaDrillCategory
#
#     def __init__(self, name: str, link: str, goal: int,
#                  static: bool, tag: str, bodyweight=True):
#         self.name = name
#         self.link = link
#         self.goal = goal
#         self.tag = tag
#         self.bodyweight = bodyweight
#         self.static = static
#
#     def __repr__(self) -> str:
#         return f'The id is {self.id}, Name is {self.name} '
#
#
# class ExerciseTag(db.Model):
#     __tablename__ = 'exercise_tags'
#
#     id = db.Column(db.Integer(), primary_key=True, nullable=False)
#     value = db.Column(db.String(255), nullable=False)
#
#     exercises = db.relationship("Exercise", secondary=association_table, back_populates="tags")
#
#     artifact_id = db.Column(db.Integer(), db.ForeignKey('exercises.id'),nullable=False)
#     # artifact = db.relationship(Exercise,
#     #                            backref=backref('tags',
#     #                                            cascade="all, delete-orphan"))
#
#     def __init__(self, artifact_id: int, value: str):
#         self.artifact_id = artifact_id
#         self.value = value
#
# # class ExerciseTag(db.Model):
# #     __tablename__ = 'exercise_tags'
# #
# #     id = db.Column(db.Integer(), primary_key=True)
# #     value = db.Column(db.String(80), nullable=False, unique=True)
# #
# #     # Relationships
# #     exercise_id = db.Column(db.Integer(), db.foreignKey('exercises.id'),
# #                             nullable=False)  # forign key reference to execercise id
# #
# #     def __init__(self, value, exercise_id):
# #         self.value = value
# #         self.exercise_id = exercise_id
# #
# #     def __repr__(self):
# #         return f" exercise tag with value: {self.value} to exercise id: {self.exercise_id}"
#
# # class ExerciseTool(db.Model):
# #     __tablename__ = 'exercise_tools'
# #
# #     id = db.Column(db.Integer, primary_key=True)
# #     value = db.Column(db.VARCHAR(80), nullable=False)  # some kind of string
# #
# #     # Relationships
# #     exercise_id = db.Column(db.Integer, db.foreignKey('exercises.id'))  # forign key reference to execercise id
# #
# #     def __init__(self, value, exercise_id):
# #         self.value = value
# #         self.exercise_id = exercise_id
# #
# #     def __repr__(self):
# #         return f" tool: {self.value} to exercise id: {self.exercise_id}"
