from flask import abort, make_response
from datetime import date
from sqlalchemy import func, desc
from config import db
from models import pharmacy_table, mask_table, user_table, order_history_table
from models import pharmacy_table_Schema, mask_table_Schema, user_table_Schema, order_history_table_Schema


def get_top_user(top_num, date_front, date_end):
    '''
    SELECT * FROM PERSONAL WHERE BIRTH_DATE_TIME BETWEEN
    '2000-01-01 00:00:00' AND '2002-09-18 12:00:00';
    
    The top x users by total transaction amount of masks within a date range.

    SELECT user_name,sum(transactionAmount) FROM order_history_table group by user_name
    '''
    date_front = date(int(date_front.split('-')[0]),int(date_front.split('-')[1]),int(date_front.split('-')[2]))
    date_end = date(int(date_end.split('-')[0]),int(date_end.split('-')[1]),int(date_end.split('-')[2]))
    
    res = db.session.query(order_history_table.user_name, func.sum(order_history_table.transactionAmount)).filter(order_history_table.transactionDate.between(date_front, date_end)).group_by(order_history_table.user_name).order_by(desc(func.sum(order_history_table.transactionAmount))).limit(top_num).all()
    ans = {}
    print(res)
    for i in res:
        print(i[0])
        print(i[1])
        ans[i[0]] = i[1]
    # ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)
    # existing_list = order_history_table.query.filter(order_history_table.transactionDate.between(date_front, date_end)).group_by(order_history_table.user_name).limit(top_num).all()
    return ans

def get_total_mask_price(date_front, date_end):
    date_front = date(int(date_front.split('-')[0]),int(date_front.split('-')[1]),int(date_front.split('-')[2]))
    date_end = date(int(date_end.split('-')[0]),int(date_end.split('-')[1]),int(date_end.split('-')[2]))
    res = db.session.query(func.sum(order_history_table.transactionAmount), func.sum(order_history_table.perpack)).filter(order_history_table.transactionDate.between(date_front, date_end)).all()
    ans = {}
    ans['totalAmount'] = res[0][0]
    ans['totalMask'] = res[0][1]
    return ans
    

