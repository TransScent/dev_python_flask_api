from flask import Flask,jsonify
import config as mysql_db
app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello():
    result=get_query_result("select * from actor")
    return jsonify({'isProcess': 'Y','data':result}) 

def get_query_result(query):  
    result=mysql_db.connection()
    mycursor=result.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult

@app.route('/<name>')
def hello_name(name):
    print(name)
    return "Hello {}!".format(name)
if __name__ == '__main__':
    app.run()