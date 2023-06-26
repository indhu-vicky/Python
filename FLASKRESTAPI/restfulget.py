from flask import Flask, jsonify, request

app = Flask(__name__)

#cities=[{'name':'Chennai'},{'name':'Bangalore'},{'name':'Mumbai'}]
cities=[{'name':'chennai'},{'name':'bangalore'},{'name':'mumbai'}]
@app.route('/citylist',methods=['GET'])
def returnAll():
    return jsonify({'Available Cities': cities})

@app.route('/citylist/<string:name>',methods=['GET'])
def returnOne(name):
    result=[city for city in cities if city['name']==name]
    return jsonify({'city': result[0]})

##it's not working except chennai if in caps^^^^^^^^
##works for all without caps

###this works
languages=[{'name':'Javascript'},{'name':'Python'},{'name':'Ruby'}]

@app.route('/lang',methods=['GET'])
def resultAll():
    return jsonify({'languages':languages})

@app.route('/lang/<string:name>',methods=['GET'])
def resultOne(name):
    langs=[language for language in languages if language['name']==name]
    return jsonify({'language':langs[0]})

##this also not works if you start with caps here and chrome doesn't accept it!!!
choices=[{'name':'coffee'},{'name':'tea'},{'name':'juice'}]

@app.route('/choices',methods=['GET'])
def AllChoices():
    return jsonify({'Choices':choices})

@app.route('/choices/<string:name>',methods=['GET'])
def OneChoice(name):
    c=[choice for choice in choices if choice['name']==name]
    #for choice in choices:
    #    #print(choice)
    #    if choice['name']==name:
    #       c=choice
    return jsonify({'Your Choice':c[0]})

if __name__ == "__main__":
    app.run(debug=True)