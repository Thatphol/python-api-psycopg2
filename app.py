from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import json
import psycopg2 as p

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

# connect to psql
hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = '1234**'
port_id = 5432

@app.route("/api/attractions")
def read():
    mydb = p.connect(host = hostname, dbname = database, user = username, password = pwd, port = port_id )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM user_table")
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult),200)
# ส่วนของการเรียก และเข้าถึง psql

@app.route("/api/attractions/<id>")
def readbyid():
    mydb = p.connect(host = hostname, dbname = database, user = username, password = pwd, port = port_id )
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM user_table WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult),200)

@app.route("/api/attractions", methods = ['POST'])
def create():
    data = request.get_json()
    mydb = p.connect(host = hostname, dbname = database, user = username, password = pwd, port = port_id )
    mycursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO user_table (User_UID, Username, role, cash, start) VALUES(%s, %s, %s, %s)"
    val = (data['User_UID'], data['Username'], data['role'], data['cash'], data['start'])
    mycursor.execute(sql, val)
    mydb.commit()
    return make_response(jsonify({"rowcount": mycursor.rowcount }),200)
# Create / เพิ่มแถวข้อมูล

@app.route("/api/attractions/<id>", methods = ['PUT'])
def update(id):
    data = request.get_json()
    mydb = p.connect(host = hostname, dbname = database, user = username, password = pwd, port = port_id )
    mycursor = mydb.cursor(dictionary=True)
    sql = "UPDATE user_table SET User_UID = %s, Username= %s, role= %s, cash= %s, start= %s WHERE id = %s"
    val = (data['User_UID'], data['Username'], data['role'], data['cash'], data['start'], id)
    mycursor.execute(sql, val)
    mydb.commit()
    return make_response(jsonify({"rowcount": mycursor.rowcount }),200)
# update / เพิ่มข้อมูลต่าง ๆ 

@app.route("/api/attractions/<id>", methods = ['PUT'])
def delete(id):
    data = request.get_json()
    mydb = p.connect(host = hostname, dbname = database, user = username, password = pwd, port = port_id )
    mycursor = mydb.cursor(dictionary=True)
    sql = "DELETE FROM user_table WHERE id = %s"
    val = (id, )
    mycursor.execute(sql, val)
    mydb.commit()
    return make_response(jsonify({"rowcount": mycursor.rowcount }),200)

if __name__ == "__main__":
    app.run(debug=True)
