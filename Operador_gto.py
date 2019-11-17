
import requests,openpyxl
from bs4 import BeautifulSoup

wb=openpyxl.Workbook()
wa=wb.active

result1='https://www.indeed.com.mx/jobs?q=operador+de+produccion&l=GTO'
result2='https://www.indeed.com.mx/jobs?q=operador+de+produccion&l=GTO&start=10'
result3='https://www.indeed.com.mx/jobs?q=operador+de+produccion&l=GTO&start=20'
# result4='https://www.indeed.com.mx/jobs?q=operador+de+produccion&l=GTO&start=30'
# result5='https://www.indeed.com.mx/jobs?q=Supervisor+de+produccion&l=Monterrey%2C+N.+L.&start=40'
# result6='https://www.indeed.com.mx/jobs?q=ingeniero+calidad&l=Edo.+de+M%C3%A9xico&start=50'
# result7='https://www.indeed.com.mx/jobs?q=ingeniero+calidad&l=Edo.+de+M%C3%A9xico&start=60'
# result8='https://www.indeed.com.mx/jobs?q=ingeniero+calidad&l=Edo.+de+M%C3%A9xico&start=70'

Result1=requests.get(result1)
soup1=BeautifulSoup(Result1.text,'html.parser')

Result2=requests.get(result2)
soup2=BeautifulSoup(Result2.text,'html.parser')

Result3=requests.get(result3)
soup3=BeautifulSoup(Result3.text,'html.parser')

# Result4=requests.get(result4)
# soup4=BeautifulSoup(Result4.text,'html.parser')
#
# Result5=requests.get(result5)
# soup5=BeautifulSoup(Result5.text,'html.parser')

# Result6=requests.get(result5)
# soup6=BeautifulSoup(Result5.text,'html.parser')
#
# Result7=requests.get(result5)
# soup7=BeautifulSoup(Result5.text,'html.parser')
#
# Result8=requests.get(result5)
# soup8=BeautifulSoup(Result5.text,'html.parser')

title1=soup1.find_all('div', class_='title' )
title2=soup2.find_all('div', class_='title' )
title3=soup3.find_all('div', class_='title' )
# title4=soup4.find_all('div', class_='title' )
# title5=soup5.find_all('div', class_='title' )
# title6=soup6.find_all('div', class_='title' )
# title7=soup7.find_all('div', class_='title' )
# title8=soup8.find_all('div', class_='title' )



salario1=soup1.find_all('div',class_="salarySnippet salarySnippetDemphasize")
salario2=soup2.find_all('div',class_="salarySnippet salarySnippetDemphasize")
salario3=soup3.find_all('div',class_="salarySnippet salarySnippetDemphasize")
# salario4=soup4.find_all('div',class_="salarySnippet salarySnippetDemphasize")
# salario5=soup5.find_all('div',class_="salarySnippet salarySnippetDemphasize")
# salario6=soup6.find_all('div',class_="salarySnippet salarySnippetDemphasize")
# salario7=soup7.find_all('div',class_="salarySnippet salarySnippetDemphasize")
# salario8=soup8.find_all('div',class_="salarySnippet salarySnippetDemphasize")

for t in range(title1):
    name1= t.a.get_text()

    if 'Operador ' or 'OPERADOR' or 'operador' in name1 and '0' in salary1:
         wa.cell(row=1,column=1).value = name1

for t in range(salario1):
    salary1=s.get_text()
    wa.cell(row=1,column=2).value=salary1

wb.save(r'C:\Users\kenta takayasu\Desktop\practica\sample.xlsx')
# for ti,sa in zip(title2,salario2):
#     name2= ti.a.get_text()
#     salary2=sa.get_text()
#     if 'Operador' or 'OPERADOR' or 'operador' in name2 and '0' in salary2:
#         print(name2,salary2.replace('$' ,' '))
#     else:
#         print("no date")
#
# for tit,sal in zip(title3,salario3):
#     name3= tit.a.get_text()
#     salary3=sal.get_text()
#     if 'Operador' or 'OPERADOR' or 'operador' in name3 and '0' in salary3:
#         print(name3,salary3.replace('$' ,' '))
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
