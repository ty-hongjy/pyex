# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:46:49 2017

@author: hongjy
"""

#CrowTaobaoPrice.py 

import requests
import re 
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        kv={'user-agent':'Mozilla/5.0'}
        r=requests.get(url,headers=kv,timeout=30)
        #r=requests.get(url,timeout=30)
        r.raise_for_status()
        #r.encoding=r.apparent_encoding
        r.encoding='UTF-8'
        #r.encoding='gbk'
        return r.text
    except:
        return "err"

def CategoryList(ilt,html):
    try:
        tlt=re.findall(r'data-label="..{2,5}"',html)
        
        for i in range(len(tlt)):
                cate=eval(tlt[i].split('=')[1])
                cate1=re.findall(r'.*[^\d{1,2}]',cate)
                ilt.append(cate1)
    except:
        print("")
        
def CategoryList1(ilt,html):
        soup=BeautifulSoup(html,'html.parser')
        for p in soup.select(".slideTop-cateFunc-f"):
            #print(p.text)
            #print(p.select(".slideTop-cateFunc-f_div200_a201"))
            #print(p.select(".slideTop-cateFunc-f_div200_a201")[1].text)
            #print(p.a.attrs['href'])
            #print(p.get("a"))
            ilt.append([p.text,p.a.attrs['href']])
        ilt.append(["Quit",""])
            

def printCategoryList(ilt):
    tplt="{:4}\t{:8}"
    print(tplt.format("序号","分类","URL"))
#    tplt="{:4}\t{:8}\t{:20}"
#   print(tplt.format("序号","分类","URL"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0]))
        
def CourseList(ilt,html):
    print(html)
    #html=getHTMLText(course_url)
    soup=BeautifulSoup(html,'html.parser')
    soupbody=soup.body.contents
    #print(soupbody)
    #print(soup.body.prettify())
    #soup.get(attrs)
    #ls=re.findall('r\"data-cate=*\"',html)
    #print(ls)
    soup=BeautifulSoup(r.text,'html.parser')
    soup.select(".m-result-view")

    try:
        tlt=re.findall(r'alt="..{2,20}"',html)
        
        print(len(tlt))
        print(tlt)
        
        for i in range(len(tlt)):
                course=eval(tlt[i].split('=')[1])
                print(course)
                #cate1=re.findall(r'.*[^\d{1,2}]',cate)
                #print(cate1)
                ilt.append(course)
    except:
        print("")


def printCourseList(ilt):
    tplt="{:4}\t{:8}"
    print(tplt.format("序号","课程"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0]))


def main():
    infoList=[]
    courseList=[]

    category_url='http://www.icourse163.org/category/all'
    category_url='http://www.icourse163.org/'

    html=getHTMLText(category_url)
    CategoryList1(infoList,html)
    printCategoryList(infoList)

    course_url='http://www.icourse163.org/category/computer'
    #html=getHTMLText(course_url)
    #print(html)
    #CourseList(courseList,html)
    #printCourseList(courseList)
    
if __name__ == '__main__':
    main()
