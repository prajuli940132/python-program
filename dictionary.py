#web parsing for dictionary word with try-except
import re
import urllib.request
#http://www.dictionary.com/browse
url="http://www.dictionary.com/browse"
word=input("Enter your word:")
url=url+"/"+word
try:
    data=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
    data1=urllib.request.urlopen(data).read()
    data2=data1.decode('utf-8')
    #print(data2)
    m=re.search('e10vl5dg6">',data2)
    start=m.end()
    end=start+126
    print(data2[start:end])
except:
    print("Word Not Found In Dictionary,Try Again!")
    
