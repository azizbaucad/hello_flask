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
    cur.execute("""SELECT * FROM orangee WHERE msisdn_sans_indicatif = %s """, (id_number,))
    response = cur.fetchone()
    return jsonify(response) 

# api pour les personnes qui ont payé par orange money
@app.route('/pay_by_orange_money')
def get_user_by_orange_money():
    co = get_db_connecter()
    cur = co.cursor()
    cur.execute("SELECT * FROM orangee where payment_mode like 'ORANGEMONEY';")
    data = cur.fetchall()
    return data ;

# api pour les personnes qui ont payé par mobile web
@app.route('/pay_by_mobile_web')
def get_user_by_mobile_web():
    co = get_db_connecter()
    cur = co.cursor()
    cur.execute("SELECT * FROM orangee where interface like 'MOBILE_WEB';")
    data = cur.fetchall()
    return data ;

# apir pour les personnes qui ont payé par android
@app.route('/pay_by_android')
def get_user_by_android():
    co = get_db_connecter()
    cur = co.cursor()
    cur.execute("SELECT * FROM orangee where interface like 'ANDROID';")
    data = cur.fetchall()
    return data ;

# api pour les personnes qui ont payé par orange money et par mobile web
@app.route('/client_qui_ont_payer_par_OM')
def get_all_user_by_om():
    co = get_db_connecter()
    cur = co.cursor()
    cur.execute("SELECT COUNT(payment_mode) FROM orangee where payment_mode in('ORANGEMONEY') Group by payment_mode ;")
    data = cur.fetchall()
    return data ;

# api pour les nombres personnes qui ont payé par android
@app.route('/client_qui_ont_payer_par_ANDROID')
def get_all_user_by_android():
    co = get_db_connecter()
    cur = co.cursor()
    cur.execute("SELECT COUNT(interface) FROM orangee where interface in('ANDROID') Group by interface;")
    data = cur.fetchall()
    return data ;              

if __name__ == '__main__' :
    app.run(debug=True)












 




 
    

    
