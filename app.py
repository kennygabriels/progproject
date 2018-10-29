from flask import Flask, render_template
import requests
import xmltodict
app = Flask(__name__)



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/reisplanner')
def reisplanner_page():
    auth_details = ('thijsaarts.aarts@student.hu.nl', '1IbHrkNUhwW6Bnezbn0C9F9_0GKMLSBkXo7vmFW97EHmfaMnVd2Oaw')
    api_url = 'http://webservices.ns.nl/ns-api-stations'
    city_name = 'amsterdam'
    vertrek_url = 'http://webservices.ns.nl/ns-api-avt?station='+ city_name
    response = requests.get(api_url , auth=auth_details)
    vertrek_response = requests.get(vertrek_url, auth=auth_details)
    convert = xmltodict.parse(response.text)
    vertrek_convert = xmltodict.parse(vertrek_response.text)

    list1 = []
    for x in convert['stations']['station']:
        if x['country'] == 'NL':
            list1.append(x)


    list2 = []
    for x in vertrek_convert['ActueleVertrekTijden']['VertrekkendeTrein']:
        list2.append(x)

    return render_template('reisplanner.html', list1=list1, list2=list2)

@app.route('/reisplanner/<string:city_name>')
def reisplanner_city_page(city_name):
    auth_details = ('thijsaarts.aarts@student.hu.nl', '1IbHrkNUhwW6Bnezbn0C9F9_0GKMLSBkXo7vmFW97EHmfaMnVd2Oaw')
    api_url = 'http://webservices.ns.nl/ns-api-stations'
    vertrek_url = 'http://webservices.ns.nl/ns-api-avt?station='+ city_name
    response = requests.get(api_url , auth=auth_details)
    vertrek_response = requests.get(vertrek_url, auth=auth_details)
    convert = xmltodict.parse(response.text)
    vertrek_convert = xmltodict.parse(vertrek_response.text)

    list1 = []
    for x in convert['stations']['station']:
        list1.append(x)

    list2 = []
    for x in vertrek_convert['ActueleVertrekTijden']['VertrekkendeTrein']:
        list2.append(x)

    return render_template('vertrektijden.html', list1=list1, list2=list2)

if __name__ == '__main__':
    app.run()
