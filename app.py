from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import sqlite3
app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

# Scehma CREATE TABLE meeting(name TINYTEXT, description MEDIUMTEXT, picture int, Location TINYTEXT, time TINYTEXT);
# One row of data in the db {'Beer with the boies', 'We are gonna get drunk and have fun', '1', 'Andralong', '2023-05-12 18:00'}

@app.route("/")
def home():
    return "Test"

@app.route("/meeting", methods = ["Get", "Post"])
@cross_origin()
def meeting():
    if request.method == "GET": 
        cur = sqlite3.connect("meetings.db").cursor()
        #try:
        data = cur.execute("SELECT * FROM meeting")
        output = []
        print(data)
        for i in data.fetchall():
            output += i

        return jsonify(results = output)
        #except:
        return "Unable to find the meetings", 501
        
    if request.method == "POST":
        try:
            con = sqlite3.connect("meetings.db")
            cur = con.cursor()
            data = cur.execute(f""" INSERT INTO meeting(picture, name, location, time, description)
            VALUES(        
            "{request.json[0]}",
            "{request.json[1]}",
            "{request.json[2]}",
            "{request.json[3]}",
            "{request.json[4]}"
            )""")
            con.commit()
            return request.json
        except:
            return "Unable to save the meeting", 502        