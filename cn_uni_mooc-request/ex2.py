import requests
import os
import re
from bs4 import BeautifulSoup

def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.status_code
		print(r.encoding)
		print(r.apparent_encoding)
		r.encoding=r.apparent_encoding
		#print(r.text[:1000])
		#q.head(url)
		#print(r.head(url))
		r.text
		return r.text
		#q=requests.head(url)

	except:
		#return "err"
		#print("err")
		return "err"
 
if __name__ == '__main__':
	#main()
	url="http://www.baidu.com"
	#getHTMLText(url)

##search IP
print("search IP")
url="http://m.ip138.com/ip.asp?ip="
url=url+'202.204.80.112'
url='http://learning.sohu.com/20170227/n481870520.shtml'
#url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
demo=getHTMLText(url)
soup=BeautifulSoup(demo,'html.parser')#print(soup)
'''
print(soup)
print(soup.p.attrs)
print(soup.p.name)
print(soup.p.string)
print(type(soup.p))
print(soup.head)
print("soup.head.contents:")
print(soup.head.contents)
print(soup.body.contents)
'''
#print(soup.prettify())
print(demo)

for link in soup.find_all('a'):
	print(link.get('href'))

for tag in soup.find_all(re.compile('ht')):
	print(tag.name)

for str in soup.find_all(string=re.compile('ht')):
	print(str)
