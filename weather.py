#program to parse web for weather forecast
import re
import urllib.request
#https://www.weather-forecast.com/locations/Pune/forecasts/latest
city=input("enter your city")
url="https://www.weather-forecast.com/locations/"+city+"/forecasts/latest"
data=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
data1=urllib.request.urlopen(data).read()
data2=data1.decode("utf-8")
#print(data2)
m=re.search('span class="phrase">',data2)
start=m.end()
end=start+100
newstring=data2[start:end]
print(newstring)
 
