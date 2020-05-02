from flask import Flask
from flask import jsonify
import config as mysql_db
app = Flask(__name__)




@app.route('/',methods=['GET'])
def hello():
    result=mysql_db.connection()
    mycursor=result.cursor()
    mycursor.execute("select * from customers")
    myresult = mycursor.fetchall()
    return jsonify({'success': 'success', 'data':myresult}) 


   
    
@app.route('/<name>')
def hello_name(name):
    print(name)
    return "Hello {}!".format(name)
if __name__ == '__main__':
    app.run()