from app.models.event import *

event_1 = Event("10/02/2019","Birthday Party", 1, "Bedroom", "Pity Party" )
event_2 = Event("25/12/2019", "Christmas", 10, "In your heart", "Christmas Celebration" )
events = [event_1, event_2]

def add_new_event(event):
    events.append(event)
