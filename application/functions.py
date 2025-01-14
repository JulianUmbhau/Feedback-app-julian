from application.models import User, Event, Pin
from flask import request, jsonify
from application.constant import db_overwrite_params
from application import db
from datetime import datetime, timedelta

def change_event(app_id):
    event = Event.query.filter_by(app_id = app_id)
    vals = [request.get_json(f'{var}') for var in db_overwrite_params['Event']]
    event_title = vals[db_overwrite_params['Event'] == 'title']
    event_date_start = vals[db_overwrite_params['Event'] == 'date_start']
    event_date_end = vals[db_overwrite_params['Event'] == 'date_start']
    event_description = vals[db_overwrite_params['Event'] == 'description']

    for var in db_overwrite_params['Event']:
        var_change = "_".join(["event", var])
        if f'{var_change}' == None:
            continue

        match var_change:
            case 'title':
                event.title = event_title
            case 'date_start':
                event.date_start = event_date_start
            case 'date_end':
                event.date_end = event_date_end
            case 'description':
                event.description = event_description
    db.session.commit()


# def check_isActive_expired(isActive_status, date_end, time_delta):
#     endDate = datetime.strptime(date_end, "%Y-%m-%dT%H:%M:%SZ")
#     cap_time = endDate + timedelta(minutes = time_delta)
#     if (isActive_status == True and datetime.utcnow() > cap_time):
#         return False
#     else:
#         return True

def check_isActive_expired(event, time_delta):
    if not event.isActive:
        return False  
    endDate = datetime.strptime(event.date_end, "%Y-%m-%dT%H:%M:%SZ")
    cap_time = endDate + timedelta(minutes = time_delta)
    if (datetime.utcnow() > cap_time):
        event.isActive = False
        pin_delete = Pin.query.filter_by(pin = event.pin).delete()
        db.session.commit()
        return False
    else:
        return True    