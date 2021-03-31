import requests
import json
import time

class Geocoder:
    base_url = 'https://nominatim.openstreetmap.org/search'
    def fetch(self, address):
        params = { 'q': address, 'format': 'geocodejson' }
        
        res = requests.get(self.base_url, params=params)
        print('req: %s | code: %s' % (res.url, res.status_code))
        
        if res.status_code == 200:
            return res
        else:
            return none
            
    def parse(self, res):
        label = json.dumps(res['features'][0]['properties']['geocoding']['label'], indent=2)
        coords = json.dumps(res['features'][0]['geometry']['coordinates'], indent=2).replace('\n','').replace('[','').replace(']','').strip()
        #print(res.keys())
        items = {
            'address': label,
            'coordinates': coords        
        }
        print(json.dumps(items, indent=2))
        
        
        
    def run(self):
    
        addresses = ''
        
        with open('addresses.txt', 'r') as f:
            for line in f.read():
                addresses += line
        addresses = addresses.split('\n')
        for a in addresses:
            res = self.fetch(a).json()
            self.parse(res)
            time.sleep(2)
        
if __name__ == '__main__':
    geocoder = Geocoder()
    geocoder.run()
    

