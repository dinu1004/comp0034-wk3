from flask import current_app as app
from paralympics.schemas import RegionSchema, EventSchema
from paralympics import db
from paralympics.models import Region, Event

# Flask-Marshmallow Schemas
regions_schema = RegionSchema(many=True)
region_schema = RegionSchema()
events_schema = EventSchema(many=True)
event_schema = EventSchema()

@app.get("/regions")
def get_regions():
    """Returns a list of NOC regions and their details in JSON."""
    # Select all the regions using Flask-SQLAlchemy
    all_regions = db.session.execute(db.select(Region)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = regions_schema.dump(all_regions)
    # Return the data
    return result

@app.get("/events")
def get_events():
    """Returns a list of events and their details in JSON."""
    # Select all the events using Flask-SQLAlchemy
    all_events = db.session.execute(db.select(Event)).scalars()
    # Get the data using Marshmallow schema (returns JSON)
    result = events_schema.dump(all_events)
    # Return the data
    return result

@app.get("/regions/<NOC>")
def get_region(NOC):
    region = db.session.execute(
        db.select(Region).filter_by(NOC=NOC)
    ).scalar_one_or_none()
    return region_schema.dump(region)

@app.get("/events/<event_id>")
def get_event(event_id):
    """ Returns the event with the given id JSON.

    :param event_id: The id of the event to return
    :param type event_id: int
    :returns: JSON
    """
    event = db.session.execute(
        db.select(Event).filter_by(id=event_id)
    ).scalar_one_or_none()
    return event_schema.dump(event)

@app.route('/')
def hello():
    return f"Hello!"
