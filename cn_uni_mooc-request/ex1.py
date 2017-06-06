import requests
import os

def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.status_code
		print(r.encoding)
		print(r.apparent_encoding)
		r.encoding=r.apparent_encoding
		print(r.text[:1000])
		#q.head(url)
		#print(r.head(url))
		r.text
		#q=requests.head(url)

	except:
		#return "err"
		#print("err")
		return "err"
 
if __name__ == '__main__':
	#main()
	url="http://www.baidu.com"
	#getHTMLText(url)

kv={'k1':'v1','k2':'v2'}
r=requests.request('GET','http://pt123.io/wa',params=kv)
print(r.url)
body="content"
r=requests.request('POST','http://pt123.io/wa',data=body)
print(r.url)

r=requests.request('POST','http://pt123.io/wa',json=kv)
print(r.url)

hd={'user-agent':'chrome/10'}
r=requests.request('POST','http://pt123.io/wa',headers=hd)
print(r.url)

#####jd
print("JD search")
url="https://item.jd.com/3857525.html?cpdad=1DLSUE"
getHTMLText(url)

#baidu search
print("Baidu search")
kv={'wd':'Python'}
r=requests.get("http://www.baidu.com/s",params=kv)
print(r.status_code)
print(len(r.text))

##get pictures
print("get pictures")

url="http://image.nationalgeagraphics.com.cn/2017/0211/20170211061910157.jpg"
root="D://pics//"
path=root+url.split('/')[-1]
try:
	if  not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r=requests.get(url)
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()
			print("success")
	else:
		print("file exists")
except:
	print("get failse")

##search IP
print("search IP")
url="http://m.ip138.com/ip.asp?ip="
url=url+'202.204.80.112'
getHTMLText(url)

