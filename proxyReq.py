import requests
try:
    r = requests.get("http://gimmeproxy.com/api/getProxy?country=US")
    contents = r.content
    contents = contents.decode().split(',')
    IP = contents[2]
    PORT = contents[3]

    IP = IP.replace(':','')
    IP = IP.replace('"','')
    IP = IP.replace(' ','')
    IP = IP.replace('\n','')
    IP = IP.replace('ip','')

    PORT = PORT.replace(':','')
    PORT = PORT.replace('"','')
    PORT = PORT.replace(' ','')
    PORT = PORT.replace('\n','')
    PORT = PORT.replace('port','')
    string_proxy = IP + ':' + PORT
    print("PROXY:" + string_proxy)

    f = open('proxy_file.txt','w')
    f.write(string_proxy)
    f.close()
except:
     print("Error requesting proxy")
     f = open('proxy_file.txt','w')
     f.write('0')
     f.close()
