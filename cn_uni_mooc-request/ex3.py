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


def fillUnivList(ulist, html):
	 soup=BeautifulSoup(html,"html.parser")
	 for tr in soup.find('tbody').children:
		 if isinstance(tr,bs4.element.Tag):
			 tds=tr('td')
#			 print(tds[0].string,tds[1].string,tds[3].string)
                         
			 ulist.append([tds[0].string,tds[1].string,tds[3].string])


def fillUnivList1(ulist, html):

    soup = BeautifulSoup(html, "html.parser")
    neirong = soup.table.contents
    #print(neirong)
    for form in neirong[3:504]:
        if isinstance(form, bs4.element.Tag):
            tds = form('td')   #将所有td标签存为一个列表类型tds
            ulist.append([tds[0].string, tds[1].string, tds[3].string])    #在ulist中增加相应字段
            print([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(ulist,num):
	 print("{:^10}\t{:^20}\t{:^10}".format("排名","学校名称","总分"))
	 for i in range(num):
		 u=ulist[i]
		 print("{:^10}\t{:^20}\t{:^10}".format(u[0],u[1],u[2]))

def main():
	 uinfo=[]
	 url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
	 #url='http://www.zuihaodaxue.cn/news/20170227-332.html'
	 #url='http://learning.sohu.com/20170227/n481870520.shtml'

	 html=getHTMLText(url)
	 #print(html)
	 fillUnivList(uinfo,html)
	 printUnivList(uinfo,20) #20 univs main()

if __name__ == '__main__':
	main()
