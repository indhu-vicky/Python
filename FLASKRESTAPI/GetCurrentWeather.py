## Importing Library files ##
from flask import Flask, jsonify, request, Response
app = Flask(__name__)

## Data list ##
CityList=[{'City':'chennai','Weather':'20C','Latitude':'12.9716','Longitude':'77.5946'},
        {'City':'bangalore','Weather':'30C','Latitude':'89.5656','Longitude':'56.9098'},
        {'City':'mumbai','Weather':'40C','Latitude':'34.3677','Longitude':'91.1087'}]


## EndPoint to get all city details ##
@app.route('/allCityDetail',methods=['GET'])
def resultAll():
    return jsonify({'All Cities':CityList})


## EndPoint to get specific city details in GET method ##
@app.route('/city/<string:cityname>',methods=['GET'])
def CityOne(cityname):
    cityname=cityname.lower()
    try:
        res=[city for city in CityList if city['City']==cityname]
        return jsonify({'City Details':res[0]})
    except:
        res="Thank you for reaching out! We're unable to find details for the city requested."
        return res


## EndPoint to get specfic city details in POST method ##
@app.route('/getCurrentWeather',methods=['POST'])
def GetCity():
    inputcity=request.json['City']
    inputcity=inputcity.lower()
    try:
        res=[city for city in CityList if city['City']==inputcity][0]
        outputformat=request.json['output_format']
        if outputformat == 'xml':
            name=res['City']
            Temp=res['Weather']
            Latitude=res['Latitude']
            Longitude=res['Longitude']
    
            resultxml="""<?xml version="1.0" encoding="UTF-8" ?>
            <root>
            <Temperature>"""+Temp+"""</Temperature>
            <City>"""+name+"""</City>
            <Latitude>"""+Latitude+"""</Latitude>
            <Longitude>"""+Longitude+"""</Longitude>
            </root>"""
            return Response(resultxml, mimetype='text/xml')
        else:
            return jsonify({'City Details':res})
    except:
        res="Thank you for reaching out! We're unable to find details for the city requested."
        return res


##sample input format for ref ##
## {"City":"mumbai","output_format":"xml"} ##


if __name__ == "__main__":
    app.run(debug=True)

