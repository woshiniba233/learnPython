import urllib2

try:
    urllib2.urlopen("http://baidu.com", timeout=2)
    print ("working connection")

except urllib2.URLError:
    print ("No internet connection")
