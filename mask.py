from flask import abort, make_response

from config import db
from models import pharmacy_table, mask_table, user_table, order_history_table
from models import pharmacy_table_Schema, mask_table_Schema, user_table_Schema, order_history_table_Schema

def get_sold(input_pharmacy_name, input_sorted_by):
    if input_sorted_by == "mask_name":
        existing_list = mask_table.query.filter(mask_table.pharmacy_name == input_pharmacy_name).order_by(mask_table.mask_name)
    else:
        existing_list = mask_table.query.filter(mask_table.pharmacy_name == input_pharmacy_name).order_by(mask_table.price)
    if existing_list is not None:
        return mask_table_Schema.dump(existing_list)
    else:
        abort(404, f"wrong usage for this api!")

def get_mask_within_price(input_mask_name, lower_price, upper_price):
    existing_list = mask_table.query.filter(mask_table.mask_name == input_mask_name, mask_table.price >= lower_price, mask_table.price<=upper_price)
    return mask_table_Schema.dump(existing_list)    
    '''
        List all pharmacies with more or less than x mask products within a price range.
    '''