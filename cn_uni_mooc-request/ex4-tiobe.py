import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		print(r.status_code)
		#print(r.encoding)
		#print(r.apparent_encoding)
		r.encoding=r.apparent_encoding

		r.raise_for_status()
		return r.text
	except:
		return "err"


def fillTIOBEList(ulist, html):
	'''     返回一个包含 20 行数据的列表     
	每行数据为一个包含五个键值对的字典     
	keys: "Feb 2017","Feb 2016","Programming Language","Ratings","Change"     '''     
	 
	soup=BeautifulSoup(html,"html.parser")
	 
	kw = {"class": "table table-striped table-top20"}     
	table = soup.find("table", attrs=kw)     # table 存在两列 change 字段，处理时丢弃第一个 pop(2)     # 获取表头字段信息     
	ths = table.thead.find_all("th")     
	keys = []

	for th in ths:
		keys.append(th.string)     
		keys.pop(2)          # 获取主体字段信息     
		tlist = []     
		trs = table.tbody.find_all("tr")
                 
	for tr in trs:         
		values = []
        
	for td in tr:             
	 	values.append(td.string)         
	 	values.pop(2)                  
	 	item = dict(zip(keys, values))         
	 	tlist.append(item)

	return tlist

def fillTIOBEList_modify(tList,html):
        soup=BeautifulSoup(html, "html.parser")     
        for tr in soup.find('tbody').children:         
                if isinstance(tr,bs4.element.Tag):             
                        tds=tr('td')             
                        tList.append([tds[0].string,tds[1].string,tds[3].string,tds[4].string,tds[5].string])   


def printTIOBEList(ulist,num):
	 print("{:^10}\t{:^20}\t{:^10}".format("排名","学校名称","总分"))
	 for i in range(num):
		 u=ulist[i]
		 print("{:^10}\t{:^20}\t{:^10}".format(u[0],u[1],u[2]))

def main():
	 uinfo=[]
	 url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'

	 html=getHTMLText(url)
	 #print(html)
	 fillTIOBEList(uinfo,html)
	 printTIOBEList(uinfo,20) #20 univs main()

if __name__ == '__main__':
	main()

