#forward geocoding
import opencage
from opencage.geocoder import OpenCageGeocode

key = " " #paste your api key from opencage.com 
geocoder = OpenCageGeocode(key)

#here you enter the address to locate
query= u,' '
results = geocoder.geocode(query)
print(u '%f;%f;%s;%s' %(results[0]['geometry']['lat'],
results[0]['geometry']['lng'],
results[0]['components']['country_code'],
results[0]['annotations']['timezone']['name']))