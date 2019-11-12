from flask import render_template, Blueprint, request

from app.catalog import main
from app import db

from  app.catalog.models import *


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
