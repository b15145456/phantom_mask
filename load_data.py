import sqlite3
import json
import re
conn = sqlite3.connect("phontan_mask.db")

f = open('data/pharmacies.json', "r")
pharmacy_data = json.load(f)

def openingHrToOpendayAndOpenCloseTime(openHr):
    '''
    case1："Mon, Wed, Fri 08:00 - 12:00"
    case2："Mon - Fri 08:00 - 17:00"
    '''
    openHr_list = []
    day = {"Mon":0, "Tue":1, "Wed":2, "Thur":3, "Fri":4, "Sat":5, "Sun":6}
    empty_day = [0,0,0,0,0,0,0]
    empty_open_time = [0,0,0,0,0,0,0]
    empty_close_time = [0,0,0,0,0,0,0]

    if "/" in openHr:
        openHr_list = openHr.split("/")
    else:
        openHr_list.append(openHr)
    for i in range(len(openHr_list)):
    
        #分兩種case 如果只有一個- 是第一個case 有兩個- 是第二個case
        if openHr_list[i].count(" - ") == 1 :    
            for key in day.keys():
                if key in openHr_list[i]:

                    empty_day[day[key]] = 1
                    Pattern = r'\d\d'
                    Regex = re.compile(Pattern)
                    open_close_time = Regex.findall(openHr_list[i])
                    empty_open_time[day[key]] = int(open_close_time[0])
                    empty_close_time[day[key]] = int(open_close_time[2])
        else:
            Pattern = r'[A-z][A-z][A-z] - [A-z][A-z][A-z]'          #抓出Mon - Fri
            openday_range = re.compile(Pattern)
            open_days = openday_range.findall(openHr_list[i])[0].split(' ')
            # print(open_days)

            Pattern = r'\d\d'
            Regex = re.compile(Pattern)

            open_close_time = Regex.findall(openHr_list[i])

            for i in range(day[open_days[0]], day[open_days[2]]+1):
                empty_day[i] = 1
                empty_open_time[i] = int(open_close_time[0])
                empty_close_time[i] = int(open_close_time[2])
            
            
    return [empty_day, empty_open_time, empty_close_time]
def maskNameToNameAndPerpack(maskName):
    '''
    "True Barrier (green) (3 per pack)"
    '''
              #抓出數字
    regex = re.compile(r'\d+')
    perpackNum = regex.findall(maskName)
    
    regex = re.compile(r'[^(]*')
    name = regex.findall(maskName)
    return name[0][0:-1], perpackNum[0]  # return [True Barrier ,3]

m_id = 0

for pharmacy in pharmacy_data:

    print(pharmacy['name'])
    print(pharmacy['cashBalance'])
    print(str(openingHrToOpendayAndOpenCloseTime(pharmacy['openingHours'])[0]))
    print(str(openingHrToOpendayAndOpenCloseTime(pharmacy['openingHours'])[1]))
    print(str(openingHrToOpendayAndOpenCloseTime(pharmacy['openingHours'])[2]))
    
    for mask_idx in range(len(pharmacy['masks'])):
        insert_mask_cmd = f"INSERT INTO mask_table VALUES {m_id, maskNameToNameAndPerpack(pharmacy['masks'][mask_idx]['name'])[0], maskNameToNameAndPerpack(pharmacy['masks'][mask_idx]['name'])[1], pharmacy['masks'][mask_idx]['price'], pharmacy['name']}"
        m_id+=1
        conn.execute(insert_mask_cmd)


    insert_pharmacy_cmd = f"INSERT INTO pharmacy_table VALUES {pharmacy['name'],pharmacy['cashBalance'],str(openingHrToOpendayAndOpenCloseTime(pharmacy['openingHours'])[0]),str(openingHrToOpendayAndOpenCloseTime(pharmacy['openingHours'])[1]),str(openingHrToOpendayAndOpenCloseTime(pharmacy['openingHours'])[2])}"
    conn.execute(insert_pharmacy_cmd)
conn.commit()


f = open('data/users.json', "r")
user_data = json.load(f)
o_id = 0
for user in user_data:
    
    insert_user_cmd = f"INSERT INTO user_table VALUES {user['name'], user['cashBalance']}"
    conn.execute(insert_user_cmd)

    
    for order_history in range(len(user['purchaseHistories'])):
        insert_order_history_cmd = f"INSERT INTO order_history_table VALUES {o_id, user['name'],user['purchaseHistories'][order_history]['pharmacyName'],maskNameToNameAndPerpack(user['purchaseHistories'][order_history]['maskName'])[0],maskNameToNameAndPerpack(user['purchaseHistories'][order_history]['maskName'])[1],user['purchaseHistories'][order_history]['transactionAmount'],user['purchaseHistories'][order_history]['transactionDate']}"
        o_id+=1
        conn.execute(insert_order_history_cmd)
conn.commit()
