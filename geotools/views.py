from django.shortcuts import render, get_object_or_404, redirect
import json, requests
# Create your views here.

def coordinate(request):
    if request.method == "POST":
        lat = [request.POST['lat_deg'],request.POST['lat_min'], request.POST['lat_sec']]
        lon = [request.POST['lon_deg'],request.POST['lon_min'], request.POST['lon_sec']]
        #if validateCPF(cpfNumber) == True:

        #try:
        coord = calc_coord(lat, lon)
        url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+ repr(coord[0]) +','+ repr(coord[1]) +'&key=AIzaSyA_3wK_DfiwW94-1dg352-I8Zs__FGYrDo'
        result = requests.get(url)
        geoJson = result.json()
        return render(request, 'geotools/coordinate.html', {
            'lat': coord[0],
            'lon': coord[1],
            'geoInfo': geoJson['results'][0]['formatted_address'],
            'page_title': 'Geo',
            'coordInfo': coordInfo,
            'latInfo': latInfo,
            'lonInfo': lonInfo})
        """except:
            return render(request, 'geotools/coordinate.html', {
                'r': '* Insira coordenadas válidas! Utilize apenas números e pontos.',
                'page_title': 'Geo',
                'coordInfo': coordInfo,
                'latInfo': latInfo,
                'lonInfo': lonInfo})
"""
    return render(request, 'geotools/coordinate.html', {
        'page_title': 'Geo',
        'coordInfo': coordInfo,
        'latInfo': latInfo,
        'lonInfo': lonInfo})


def calc_coord(lat, lon):
    opt = 'opt1'
    #lat = float(laDeg)
    #min = float(laMin)
    #sec = float(laSec)
    lat_d = (((float(lat[2])/60) + float(lat[1]))/60)
    lon_d = (((float(lon[2])/60) + float(lon[1]))/60)
    if opt == 'opt1':
        lat_dec = -(float(lat[0]) + lat_d)
        lon_dec = -(float(lon[0]) + lon_d)
    elif opt == 'opt2':
        lat_dec = (float(lat[0]) + lat_d)
        lon_dec = (float(lon[0]) + on_d)
    return lat_dec , lon_dec



coordInfo = """
São linhas imaginárias pelas quais a Terra foi “cortada”, essas linhas são os paralelos e meridianos, através dos paralelos e meridianos é possível estabelecer localizações precisas em qualquer ponto do planeta.
"""
latInfo = """
• Latitude: É a distância medida em graus de um determinado ponto do planeta entre o arco do meridiano e a linha do equador.
"""

lonInfo = """
• Longitude: É a localização de um ponto da superfície medida em graus, nos paralelos e no meridiano de Greenwich.
"""
