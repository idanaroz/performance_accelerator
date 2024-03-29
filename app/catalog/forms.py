from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length


class EditExerciseForm(FlaskForm):  # Todo: craft it
    name = StringField("What's the name of the exercise?",
                       validators=[DataRequired(), Length(3, 15, message='between 3 to 15 characters')])
    link = StringField('Enter exercise video link', validators=[DataRequired()])
    goal = IntegerField("What's your goal for this field?", [DataRequired()])
    bodyweight = BooleanField('Is it a bodyweight exercise?')
    static = BooleanField('Is it a static exercise?')
    meta_drill = StringField('What meta drill is it relate to?', validators=[DataRequired()])
    submit = SubmitField('Update')


# Todo: take care all tables (e.g tags)
class CreateExerciseForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(3, 15, message='between 3 to 15 characters')])
    link = StringField('Link', validators=[DataRequired()])
    goal = IntegerField("Goal", [DataRequired()])
    bodyweight = BooleanField('bodyweight')
    static = BooleanField('Static')
    meta_drill = StringField('Meta_drill', validators=[DataRequired()])
    submit = SubmitField('Create')
