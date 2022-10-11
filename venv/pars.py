import requests
from bs4 import BeautifulSoup
import json
import lxml
from time import sleep
import csv

# url = 'https://weather.rambler.ru/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# quotes = soup.find_all('div', class_='_1HBR _3mFL')
# f=soup.find_all('div', class_='Hixd')
#
# f1=f[0]
# s1=''
# for i in f1:
#     s1+=i
# a=quotes[0]
# s=''
# for i in a:
#     s+=i


def Urfu():
    url='https://urfu.ru/index.php?id=31050'
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    r = s.get(url)

    soup = BeautifulSoup(r.text, 'lxml')
    zapr=soup.find_all(class_='dataRow')
    mas=[]


    for i in range(len(zapr)):
       # print(zapr[i].text)
        if (zapr[i].text).count('09.03.01 Информатика и вычислительная техника')==1:
            #mas.append(zapr[i-4])
            mas.append(zapr[i].text.replace('\n',' '))


    m=[]

    with open("rr.csv", mode="w", encoding='utf-16') as w_file:
        file_writer = csv.writer(w_file, delimiter=" ", lineterminator="\r")
        for i in mas:

            m.append(i)
            file_writer.writerow(m)
            m=[]
    #print(mas)
def pars():
    url = 'https://soccer365.ru/competitions/12/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    zapros=soup.find_all('table',class_='stngs')
    m=[]
    for i in zapros:
        a=i.find_all('div',class_='img16')
        k=0
        for z in a:
            k+=1
            z=str(k)+' '+z.text
            m.append(z)
    return m

def pars1():
    url='https://soccer365.ru/competitions/13/'
    resp=requests.get(url)
    soup=BeautifulSoup(resp.text,'lxml')
    zapros=soup.find_all('table',class_='stngs')
    m = []
    for i in zapros:
        a = i.find_all('div', class_='img16')
        k = 0
        for z in a:
            k += 1
            z = str(k) + ' ' + z.text
            m.append(z)
    return m
def pars2():
    url='https://cbr.ru/'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    zapros = soup.find_all('div', class_='col-md-2 col-xs-9 _right mono-num')
    return zapros[0].text
def pars3():
    url='https://tabiturient.ru/np/1027/'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    zapros = soup.find_all('div',class_='mobpadd20')
    for i in zapros:
        m1=[]
        m2=[]
        a=i.find_all('span',class_='font3')
        a2=i.find_all('div',class_='circusonram')
        for z in a:
            m1.append(z.text)
        for t in a2:
            m2.append(t.text)

        for i in range(len(m1)):
            print(m1[i],m2[i])
def pars3():
    mas = []
    url = f'https://ekaterinburg.hh.ru/search/vacancy?text=Python&area=3&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20&no_magic=true&L_save_area=true&page=0&hhtmFrom=vacancy_search_list'
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    r = s.get(url)

    soup = BeautifulSoup(r.text, 'lxml')
    test_soup = soup.find_all('span', class_='pager-item-not-in-short-range')
    num=int(test_soup[-1].text)

    for i in range(0,num):
        url=f'https://ekaterinburg.hh.ru/search/vacancy?text=Python&area=3&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20&no_magic=true&L_save_area=true&page={i}&hhtmFrom=vacancy_search_list'
        s = requests.Session()
        s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        r = s.get(url)

        soup=BeautifulSoup(r.text,'lxml')
        qu=soup.find_all('div',class_='vacancy-serp-item')
        for i in qu:

            a=i.find('a')
            mas.append(a.text)
            mas.append(a['href'])
    print(len(mas))
    m=[]
    with open("hh.csv", mode="w", encoding='utf-16') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        for i in range(0,len(mas),2):
            m.append(mas[i])
            m.append(mas[i+1])
            file_writer.writerow(m)
            m=[]





def main():
    Urfu()

if __name__=="__main__":
    main()