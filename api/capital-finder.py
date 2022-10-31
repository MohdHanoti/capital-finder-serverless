from http.server import BaseHTTPRequestHandler
from urllib import parse 
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path   
        url_components=parse.urlsplit(s)
        query_string_list=parse.parse_qsl(url_components.query)
        my_dictionary= dict(query_string_list)
       
        
        if 'country' in my_dictionary:
            url='https://restcountries.com/v3.1/name/'
            country=my_dictionary['country']
            r = requests.get(url + country)
            data = r.json()
            capital=data[0]['capital'][0]
            message=f"The capital of {country} is {capital}"
        elif 'capital' in my_dictionary:
            url='https://restcountries.com/v3.1/capital/'
            capital=my_dictionary['capital']
            r = requests.get(url + capital)
            data = r.json()
            country= data[0]['name']['common']
            message=f"{capital} is the capital of {country}."

        else:
            message = "Please enter a country or a capital name"
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return
