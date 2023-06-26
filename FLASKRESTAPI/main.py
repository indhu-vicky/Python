from flask import Flask, jsonify, Response, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/sum/<int:a>')
def sum(a):
    result={
        "Number":a,
        "Value":"Yes"
    }
    return jsonify(result)

##@app.route('/format/<string:name>')
@app.route('/format/<name>',methods=['GET'])
def format(name):
    if name=="json":
        result={
            "Type":"json",
            "Value":"Yes"
        }
        return jsonify(result) 
    elif name=="xml":
        result="""
        <root>
        <Temperature>24.0</Temperature>
        <City>Bangalore</City>
        <Latitude>12.98</Latitude>
        <Longitude>77.58</Longitude>
        </root>
        """
        return Response(result, mimetype='text/xml')
    
@app.route('/check/')
def hello():
    name = request.args['name']
    return HELLO_HTML.format(
            name, str(datetime.now()))
HELLO_HTML = """
    <html><body>
        <h1>Hello, {0}!</h1>
        The time is {1}.
    </body></html>"""

if __name__ == "__main__":
    app.run(host="localhost",debug=True)