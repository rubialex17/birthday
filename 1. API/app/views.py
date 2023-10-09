from flask import Flask, request, Response
import datetime
from datetime import date
import psycopg2
import json
import os


# App modules
from app import app

# Variables
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "mysecretpassword")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "5432")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "postgres")


@app.route('/hello/<username>', methods=['GET', 'PUT'])
def route(username):
   if not validate_username(username):
       return Response("Username must have only letters", status=422, mimetype='application/json')
   if request.method == 'GET':
       return get_birthday_days(username)
   elif request.method == "PUT":
       return save_or_update_birthday(username,request.get_json(force=True))

def save_or_update_birthday(username,date_json):
   birthday = date_json['birthday']
   if not validate_date(birthday):
    return Response("Incorrect data format, should be YYYY-MM-DD", status=422, mimetype='application/json')
   run_postgres_command(f"""INSERT INTO birthday (name, birthdaydate)
        VALUES('{username}','{birthday}') 
        ON CONFLICT (name) 
        DO 
        UPDATE SET birthdaydate = EXCLUDED.birthdaydate
        RETURNING id;""")
   return Response("", status=204)

def get_birthday_days(username):
    try :
        birthday = get_birthday(username)[0]
    except:
        return Response(f"Birthday for user {username} not found",status=404)
    days = calculate_days(birthday)
    data = {}
    if days == 0:
         data['message'] = f'Hello, {username}! Happy birthday!'
    else:
        data['message'] = f'Hello, {username}! Your birthday is in {days} day(s)'
    json_data = json.dumps(data)
    return json_data

def get_birthday(username):
    return run_postgres_command(f"SELECT birthdaydate from birthday where name = '{username}'")

def calculate_days(birthday):
    date1 = date.today().strftime("%Y-%m-%d")
    date2 = birthday.strftime("%Y-%m-%d")

    x = date1.split("-")
    y = date2.split("-")

    numbers1 = [ int(i) for i in x ]
    numbers2 = [ int(i) for i in y ]

    d0 = date(numbers1[0],numbers1[1],numbers1[2])
    d1 = date(numbers1[0],numbers2[1],numbers2[2])

    delta = d1 - d0

    if delta.days < 0:
        d1 = date(numbers1[0]+1,numbers2[1],numbers2[2])
        delta = d1-d0
    
    return delta.days

def validate_username(username):
    return str.isalpha(username)

def validate_date(date_text):
    try:
        datetime.date.fromisoformat(date_text)
        return True
    except ValueError:
        return False

def run_postgres_command(command):
   conn = psycopg2.connect(
        database=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PASSWORD, host=POSTGRES_HOST, port= POSTGRES_PORT
   )   
   cursor = conn.cursor()
   print(command)
   cursor.execute(command)
   data = cursor.fetchone()
   conn.commit()
   cursor.close()
   conn.close()
   return data
