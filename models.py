from datetime import datetime
from marshmallow_sqlalchemy import fields
from sqlalchemy import func
from config import db, ma

class pharmacy_table(db.Model):
    __tablename__ = "pharmacy_table"
    ph_name = db.Column(db.String, primary_key=True)
    cash_balanse = db.Column(db.Float)
    openday = db.Column(db.String)
    opentime = db.Column(db.String)
    closetime = db.Column(db.String)
    

class pharmacy_table_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = pharmacy_table
        load_instance = True
        sqla_session = db.session
        include_fk = True

class mask_table(db.Model):
    __tablename__ = "mask_table"
    m_id = db.Column(db.Integer, primary_key=True)
    mask_name = db.Column(db.String)
    perpack = db.Column(db.Integer)
    price = db.Column(db.Float)
    pharmacy_name = db.Column(db.String)


class mask_table_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = mask_table
        load_instance = True
        sqla_session = db.session
        include_relationships = True
    # notes = fields.Nested(NoteSchema, many=True)

class user_table(db.Model):
    __tablename__ = "user_table"
    name = db.Column(db.String, primary_key=True)
    cash_balanse = db.Column(db.Float)


class user_table_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_table
        load_instance = True
        sqla_session = db.session
        include_fk = True

class order_history_table(db.Model):
    __tablename__ = "order_history_table"
    o_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)
    pharmacy_name = db.Column(db.String)
    mask_name = db.Column(db.String)
    perpack = db.Column(db.Integer)
    transactionAmount = db.Column(db.Float)
    transactionDate = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class order_history_table_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = order_history_table
        load_instance = True
        sqla_session = db.session
        include_fk = True

class output_sum(db.Model):
    user_name = db.Column(db.String, primary_key=True)
    transactionAmount = db.Column(db.Float)

# class output_sum_Schema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = output_sum
#         load_instance = True
#         sqla_session = db.session
#         include_fk = True


pharmacy_table_Schema = pharmacy_table_Schema(many=True)
mask_table_Schema = mask_table_Schema(many=True)
user_table_Schema = user_table_Schema(many=True)
order_history_table_Schema = order_history_table_Schema(many=True)
# output_sum_Schema = output_sum_Schema(many=True)
