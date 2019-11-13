from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required

from app.catalog import main
from app.catalog.forms import EditExerciseForm, CreateExerciseForm
from app.catalog.models import *


@main.route('/')
def display_exercises():
    exercises = Exercise.query.all()
    return render_template('home.html', exercises=exercises)


@main.route('/new/exercises', methods=['GET', 'POST'])
def new_exercise():
    if request.method == 'POST':
        # Name,link, goal, tag, bodyweight, static, Meta drill
        exercise_name = request.form['name']
        # item_url = request.form['item_url']
        # price_limit = float(request.form['price_limit'])
        #
        # store = Store.find_by_url(item_url)
        # item = Item(item_url, store.tag_name, store.query)
        # item.save_to_mongo()
        #
        # Alert(alert_name, item._id, price_limit).save_to_mongo()

    return render_template('/new_exercise.html')


@main.route('/exercise/delete/<exercise_id>', methods=['GET', 'POST'])
@login_required
def delete_exercise(exercise_id):
    exercise = Exercise.query.get(exercise_id)
    if request.method == 'POST':
        db.session.delete(exercise)
        db.session.commit()
        flash('exercise deleted successfully')
        return redirect(url_for('main.display_exercises'))
    return render_template('delete_exercise.html', exercise=exercise, exercise_id=exercise_id)


@main.route('/edit/exercise/<exercise_id>', methods=['GET', 'POST'])
@login_required
def edit_exercise(exercise_id):
    exercise = Exercise.query.get(exercise_id)
    form = EditExerciseForm(obj=exercise)
    if form.validate_on_submit():
        exercise.name = form.name.data
        exercise.link = form.link.data  # edit link is not working properly
        exercise.goal = form.goal.data
        exercise.bodyweight = form.bodyweight.data
        exercise.static = form.static.data
        exercise.meta_drill = form.meta_drill.data
        db.session.add(exercise)
        db.session.commit()
        flash('Book Edited successfully')
        return redirect(url_for('main.display_exercises'))
    else:
        return render_template('edit_exercise.html', form=form)


@main.route('/create/exercise', methods=['GET', 'POST'])
@login_required
def create_exercise():
    form = CreateExerciseForm()

    if form.validate_on_submit():
        exercise = Exercise(name=form.name.data,
                            link=form.link.data,
                            tag='',
                            goal=form.goal.data,
                            static=form.static.data,
                            meta_drill=form.meta_drill.data)
        db.session.add(exercise)  # update the tag as well
        db.session.commit()
        flash('Exercise was added successfully')
        return redirect(url_for('main.display_exercises'))  # show maybe all relevant for this Metadata
    return render_template('create_exercise.html', form=form)
