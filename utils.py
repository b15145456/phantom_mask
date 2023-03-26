from flask import abort, make_response
from sqlalchemy.sql import text
from config import db
from models import pharmacy_table, mask_table, user_table, order_history_table
from models import pharmacy_table_Schema, mask_table_Schema, user_table_Schema, order_history_table_Schema



def search_word(key_word):
    '''
    '''
    # search = '%{}%'.format(key_word)
    # posts = pharmacy_table.query.filter(pharmacy_table.pharmacy_name.like(search)).all()
    # print(dir(pharmacy_table))
    # posts = pharmacy_table.query.filter(pharmacy_table.pharmacy_name.like('search')).all()
    # posts = db.session.query(pharmacy_table).filter(pharmacy_table.pharmacy_name.like('%Ra%')).all()
    # sql = "select mask_name or pharmacy_name from pharmacy_table where like "+search
    ans = []

    sql = "SELECT DISTINCT mask_name FROM mask_table WHERE mask_name LIKE '%"+key_word+"%'"
    res1 = db.session.execute(text(sql)).fetchall()

    sql = "SELECT DISTINCT pharmacy_name FROM mask_table WHERE pharmacy_name LIKE '%"+key_word+"%'"
    res2 = db.session.execute(text(sql)).fetchall()

    for i in res1:
        print(i)
        ans.append(i[0])
    
    # print(posts)
    for j in res2:
        print(j)
        ans.append(j[0])

    return ans