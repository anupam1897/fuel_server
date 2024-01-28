from flask import Flask, jsonify
from boto3 import client
import os
from mysql.connector import connect
from dotenv import load_dotenv
load_dotenv()


s3 = client(
    's3', 
    aws_access_key_id    = os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key= os.environ.get("AWS_SECRET_ACCESS_KEY"),
    region_name          = os.environ.get("AWS_REGION"),
	)

conn = connect(
	host =os.environ.get("RDS_MYSQL_HOST"),
	port =os.environ.get("RDS_MYSQL_PORT"),
	user =os.environ.get("RDS_MYSQL_USER"),
	password =os.environ.get("RDS_MYSQL_PASSWORD"),
	database = os.environ.get("RDS_MYSQL_DATABASE"),
	) 

def get_data(query):
    cursor = conn.cursor()
    cursor.execute(query)
    entries = cursor.fetchall()
    cursor.close()
    return entries 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def method_name():
    return ("server up and running")

@app.route('/api/v1/get_ads', methods=['GET'])
def index():
    query = "Select * from ads;"
    entries = get_data(query)
    ad_lst = [{'ad_id' : i[0]  , 'ad_image': i[1] } for i in entries]
    return jsonify(ad_lst) 
    


@app.route('/api/v1/get_posts', methods=['GET'])
def get_posts():
    query = "Select * from posts;"
    posts = get_data(query)
    posts_lst = [{
        'post_id' : i[0]  , 
        'username': i[1] ,
        'profilePicture': i[2] ,
        'postImage': i[3] ,
        'caption': i[4] ,
        'views': i[5] ,
        'likes': i[6] ,
        'createdAt': i[7] 
        } for i in posts]
    return jsonify(posts_lst) 
    

@app.route('/api/v1/get_ventures', methods=['GET'])
def get_ventures():
    query = "Select * from ventures;"
    ventures = get_data(query)
    ventures_lst = [{
        'venture_id' : i[0]  , 
        'venture_name': i[1] ,
        'founder_name': i[2] ,
        'logo_icon_src': i[3] ,
        'rating': i[4] ,
        'valuation': i[5] ,
        'location': i[6] ,
        'incorporationDate': i[7], 
        'incorporationType': i[8] ,
        'type': i[9] ,
        'industryCategory': i[10] ,
        'fundingRounds': i[11] ,
        'investor': i[12] ,
        'fundingStatus': i[13] ,
        'employeeCount': i[14] ,
        'description': i[15] ,
        } for i in ventures]
    return jsonify(ventures_lst) 

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=8080, load_dotenv=True, debug=False)