import requests
import json
import mysql.connector
from mysql.connector import Error

# Call an request
headers = {
    'Accept': 'application/json'}

res = requests.get("https://www.travel.taipei/open-api/zh-cn/Attractions/All?page=1", headers=headers)
data=res.json()
data = data['data']

# All columns needed
list_key = ['id','name','introduction','address','nlat','elong','modified']
list_ambigious=['transport','mrt']

# Category
list_id =[]
for i in range(len(data)):
    list_id.append(data[i]['id'])

list_cate = []
for i in range(len(data)):
    list_cate.append(data[i]['category'][0]['name']) # Good len = 30

# All rows
list_total=[]
list_tool=[]
for keys in list_key:
    list_tool=[]
    for i in range(len(data)):
        list_tool.append(data[i][keys])
    list_total.append(list_tool)
# print(list_total) # Good

# Check the numbers of elements in each columns
list_check=[]
for ele in list_total:
    if len(ele) != 30:
        list_check.append(ele)
# print(list_check) # Good, no NULL generated.

connection = mysql.connector.connect(host='practice-database.mysql.database.azure.com', 
                                        database='website',
                                        user='shared_user',
                                        password='Awanpassword!')

if connection.is_connected():
    print('Connected to MySQL database')
    cursor = connection.cursor()
    query = ''' 
    INSERT INTO attraction_hw (id) VALUES (%s)
    '''
    cursor.execute(query)


if connection.is_connected():
    cursor.close()
    connection.close()
    print('MySQL connection is closed')







