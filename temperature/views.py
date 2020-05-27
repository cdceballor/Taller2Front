from django.shortcuts import render, HttpResponse
import requests

def temperature(request):
    if 'value' in request.GET:
        value = request.GET['value']
        longi = request.GET['longi']
        lati = request.GET['lati']
        tipTerr = request.GET['tipTerr']
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'value': value, 'lati': lati, 'longi':longi, 'tipTerr': tipTerr, 'type': 'temperature'}
            #response = requests.post('http://127.0.0.1:8000/temperaturas/', args)
            response = requests.post('https://pi1-eafit-cdceballor.azurewebsites.net/temperaturas/', args)
            # Convierte la respuesta en JSON
            temperature_json = response.json()

    # Realiza una petición GET al Web Services
    #response = requests.get('http://127.0.0.1:8000/temperaturas/')
    response = requests.get('https://pi1-eafit-cdceballor.azurewebsites.net/temperaturas/')
    # Convierte la respuesta en JSON
    temperatures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "temperature/temperature.html", {'temperatures': temperatures})