from flask import abort, make_response
import json
from config import db
from models import pharmacy_table, mask_table, user_table, order_history_table
from models import pharmacy_table_Schema, mask_table_Schema, user_table_Schema, order_history_table_Schema

def get_sold(input_pharmacy_name, input_sorted_by):
    if input_sorted_by == "mask_name":
        existing_list = pharmacy_table.query.filter(pharmacy_table.pharmacy_name == input_pharmacy_name).order_by(pharmacy_table.mask_name)
    else:
        existing_list = pharmacy_table.query.filter(pharmacy_table.pharmacy_name == input_pharmacy_name).order_by(pharmacy_table.price)
    if existing_list is not None:
        return order_history_table_Schema.dump(existing_list)
    else:
        abort(404, f"wrong usage for this api!")

def get_pharmacy_time_day(input_time, input_day):
    '''
    query all pharmacy
    '''
    result = []
    existing_list = pharmacy_table.query.all()
    res = pharmacy_table_Schema.dump(existing_list)
    '''
    {'ph_name': 'DFW Wellness', 
    'cash_balanse': 328.41, 
    'openday': '[1, 1, 1, 1, 1, 0, 0]', 
    'closetime': "['12', '18', '12', '18', '12', 0, 0]", 
    'opentime': "['08', '14', '08', '14', '08', 0, 0]"}
    '''
    print(type(input_day-1))
    for i in res:
       if json.loads((i['openday']))[input_day-1] == 1 :
           opentime = json.loads(i["opentime"])[input_day-1]
           closetime = json.loads(i["closetime"])[input_day-1]
           if closetime < opentime:
               closetime += 24
           if opentime < int(input_time) and closetime > int(input_time):
               result.append(i["ph_name"])
    return result
    
    