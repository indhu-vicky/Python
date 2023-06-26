from flask import Flask, jsonify, request

app = Flask(__name__)

languages=[{'name':'Javascript'},{'name':'Python'},{'name':'Ruby'}]

@app.route('/lang',methods=['GET'])
def resultAll():
    return jsonify({'languages':languages})

@app.route('/lang/<string:name>',methods=['GET'])
def resultOne(name):
    langs=[language for language in languages if language['name']==name]
    #print(langs)
    return jsonify({'language':langs[0]})

######## POST #########
##important hint in postman>> select input raw >> type json
@app.route('/lang',methods=['POST'])
def addOne():
    language={'name': request.json['name']}
    languages.append(language)
    return jsonify({'languages':languages})

######### PUT ##########
##important hint in postman>> select input raw >> type json
@app.route('/lang/<string:name>',methods=['PUT'])
def editOne(name):
    langs=[language for language in languages if language['name']==name]
    langs[0]['name']=request.json['name']
    return jsonify({'language':langs[0]})

######### DELETE ##############
##no need to add data as raw just url is fine
@app.route('/lang/<string:name>',methods=['DELETE'])
def removeOne(name):
    lang=[language for language in languages if language['name']==name]
    languages.remove(lang[0])
    return jsonify({'languages':languages})

if __name__ == "__main__":
    app.run(debug=True)