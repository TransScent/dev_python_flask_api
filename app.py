from flask import Flask
app = Flask(__name__)


@app.route('/',methods=['GET'])
def hello():
    return {"name":"Jayprakash","age":25}
    
@app.route('/<name>')
def hello_name(name):
    print(name)
    return "Hello {}!".format(name)
if __name__ == '__main__':
    app.run()