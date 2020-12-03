from flask import render_template, request
from app import app
from app.models.event_list import *


@app.route('/')
def index():
    return render_template("index.html", events=events)

@app.route("/add-event", methods=["POST"])
def add_event():
    event_date = request.form["date"]
    event_name_of_event = request.form["name_of_event"]
    event_no_of_guests = request.form["no_of_guests"]
    event_location = request.form["room_location"]
    event_description = request.form["description"]
    new_event = Event(event_date, event_name_of_event, event_no_of_guests, event_location, event_description)
    add_new_event(new_event)
    return render_template("index.html", events=events)
