
import requests,openpyxl
from bs4 import BeautifulSoup

result1='https://kentacristobal.com'
# title1=soup1.find_all('div', class_='title' )

def get_soup(url):
    # """URLのSoupを取得する"""
    html = requests.get(url)
    return BeautifulSoup(html.text, "html.parser")

def scraping():
    result =get_soup(result1)
    return result.find_all('header',class_="post-header">

all=scraping()
print(all)
# Result1=requests.get(result1)
# soup1=BeautifulSoup(Result1.text,'html.parser')
#
# Result2=requests.get(result2)
# soup2=BeautifulSoup(Result2.text,'html.parser')
#
# Result3=requests.get(result3)
# soup3=BeautifulSoup(Result3.text,'html.parser')
#
# Result4=requests.get(result4)
# soup4=BeautifulSoup(Result4.text,'html.parser')
#
# Result5=requests.get(result5)
# soup5=BeautifulSoup(Result5.text,'html.parser')
#
# Result6=requests.get(result5)
# soup6=BeautifulSoup(Result5.text,'html.parser')
#
# Result7=requests.get(result5)
# soup7=BeautifulSoup(Result5.text,'html.parser')
#
# Result8=requests.get(result5)
# soup8=BeautifulSoup(Result5.text,'html.parser')

# title2=soup2.find_all('div', class_='title' )
# title3=soup3.find_all('div', class_='title' )
# title4=soup4.find_all('div', class_='title' )
# title5=soup5.find_all('div', class_='title' )
# title6=soup6.find_all('div', class_='title' )
# title7=soup7.find_all('div', class_='title' )
# title8=soup8.find_all('div', class_='title' )


# result2='https://www.indeed.com.mx/jobs?q=ingeniero+calidad&l=Gto.&start=10'
# result3='https://www.indeed.com.mx/jobs?q=ingeniero+calidad&l=Gto.&start=20'
# result4='https://www.indeed.com.mx/jobs?q=ingeniero+calidad&l=Gto.&start=30'
# result5='https://www.indeed.com.mx/jobs?q=ingeniero+calidad&l=Gto.&start=40'
# result6='https://www.indeed.com.mx/jobs?q=ingeniero+calidad&l=Gto.&start=40'
# result7='https://www.indeed.com.mx/jobs?q=ingeniero+calidad&l=Gto.&start=40'
# result8='https://www.indeed.com.mx/jobs?q=ingeniero+calidad&l=Gto.&start=40'

 # salario1=soup1.find_all('div',class_="salarySnippet salarySnippetDemphasize")
# salario2=soup2.find_all('div',class_="salarySnippet salarySnippetDemphasize")
# salario3=soup3.find_all('div',class_="salarySnippet salarySnippetDemphasize")
# salario4=soup4.find_all('div',class_="salarySnippet salarySnippetDemphasize")
# salario5=soup5.find_all('div',class_="salarySnippet salarySnippetDemphasize")
# salario6=soup6.find_all('div',class_="salarySnippet salarySnippetDemphasize")
# salario7=soup7.find_all('div',class_="salarySnippet salarySnippetDemphasize")
# salario8=soup8.find_all('div',class_="salarySnippet salarySnippetDemphasize")
#
# for t ,s in zip(title1,salario1):
#     name1= t.a.get_text()
#     salary1=s.get_text()
#     if 'Ingeniero '  or 'ingenero' in name1 and '0' in salary1:
#         print(salary1.replace('$' ,' '))
#     else:
#         print("no date")
#
# for ti,sa in zip(title2,salario2):
#     name2= ti.a.get_text()
#     salary2=sa.get_text()
#     if  'Ingeniero ' or 'ingeniero' in name2 and '0' in salary2:
#         print(salary2.replace('$' ,' '))
#     else:
#         print("no date")
#
# for tit,sal in zip(title3,salario3):
#     name3= tit.a.get_text()
#     salary3=sal.get_text()
#     if  'Inigeniero'or 'ingeniero' in name3 and '0' in salary3:
#         print(salary3.replace('$' ,' '))
#     else:
#         print("no date")
# for titi,sala in zip(title4,salario4):
#     name4= titi.a.get_text()
#     salary4=sala.get_text()
#     if ' Ingeniero ' or 'ingeniero' in name4 and '0' in salary4:
#         print(salary4.replace('$' ,' '))
#     else:
#         print("no date")
#
# for titl,salar in zip(title5,salario5):
#     name5= titl.a.get_text()
#     salary5=salar.get_text()
#     if  'Ingeniero ' or 'ingeniero' in name5 and '0' in salary5 :
#         print(salary5.replace('$' ,' '))
#     else:
#         print("no date")
#
# for titl,salar in zip(title6,salario5):
#     name6= titl.a.get_text()
#     salary6=salar.get_text()
#     if  'Ingeniero ' or 'ingeniero' in name6 and '0' in salary6 :
#         print(salary6.replace('$' ,' '))
#     else:
#         print("no date")
#
# for titl,salar in zip(title7,salario7):
#     name7= titl.a.get_text()
#     salary7=salar.get_text()
#     if  'Ingeniero ' or 'ingeniero' in name7 and '0' in salary7 :
#         print(salary7.replace('$' ,' '))
#     else:
#         print("no date")
#
# for titl,salar in zip(title8,salario8):
#     name8= titl.a.get_text()
#     salary8=salar.get_text()
#     if  'Ingeniero ' or 'ingeniero' in name8 and '0' in salary8 :
#         print(salary8.replace('$' ,' '))
#     else:
#         print("no date")
