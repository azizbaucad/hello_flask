from json import dumps
import os
from urllib import response
from flask import Flask , jsonify , request, render_template
import psycopg2
import psycopg2.extras
import jsonpickle
import json

app = Flask(__name__)

# fonction de connexion à la BDD Postgres
def get_db_connecter():
    co = psycopg2.connect(host='localhost',
    database='postgres',
    user='postgres',
    password='Aziz_2030')
    return co

@app.route("/") 
def home():
    return "Hello Flask"

# api pour obtenir tous les données
@app.route('/all_user')
def get_all_data():
    co = get_db_connecter()
    cur = co.cursor()
    cur.execute('SELECT * FROM orangee;')
    data = cur.fetchall()
    return data ;

# api pour obtenir les 10 premiers lignes  
@app.route('/ten_user')
def get_limit_ten_user():
    co = get_db_connecter()
    cur = co.cursor()
    cur.execute('SELECT * FROM orangee Limit 10;')
    data = cur.fetchall()
    return data ;    

# api pour obtenir le user par id 
@app.route('/user/<int:id_user>')
def get_user_by_id(id_user):
    conn = get_db_connecter()
    cur = conn.cursor()
    cur.execute("""SELECT * FROM orangee WHERE mssisdn = %s """, (id_user,))
    response = cur.fetchone()
    return jsonify(response)

# api pour obtenir le user par son numéro de téléphone
@app.route('/idnumber/<int:id_number>')
def get_user_by_number(id_number):
    conn = get_db_connecter()
    cur = conn.cursor()
    cur.execute("""SELECT * FROM orangee WHERE mssisdn = %s """, (id_number,))
    response = cur.fetchone()
    return jsonify(response)    

if __name__ == '__main__' :
    app.run(debug=True)












 




 
    

    
