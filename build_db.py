import sqlite3
conn = sqlite3.connect("phontan_mask.db")
pharmacy_columns = [
    "ph_name VARCHAR",
    "cash_balanse FLOAT",
    "openday VARCHAR",
    "opentime VARCHAR",
    "closetime VARCHAR",
]
create_table_cmd = f"CREATE TABLE pharmacy_table ({','.join(pharmacy_columns)})"
conn.execute(create_table_cmd)

mask_columns = [
    "m_id INTEGER",
    "mask_name VARCHAR",
    "perpack INTEGER",
    "price FLOAT",
    "pharmacy_name VARCHAR",
]
create_table_cmd = f"CREATE TABLE mask_table ({','.join(mask_columns)})"
conn.execute(create_table_cmd)

user_columns = [
    "user_name VARCHAR",
    "cash_balanse FLOAT"
]
create_table_cmd = f"CREATE TABLE user_table ({','.join(user_columns)})"
conn.execute(create_table_cmd)

order_history_columns = [
    "o_id INTEGER",
    "user_name VARCHAR",
    "pharmacy_name VARCHAR",
    "mask_name VARCHAR",
    "perpack INTEGER",
    "transactionAmount FLOAT",
    "transactionDate DATETIME",
]
create_table_cmd = f"CREATE TABLE order_history_table ({','.join(order_history_columns)})"
conn.execute(create_table_cmd)