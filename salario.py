
import requests,openpyxl
from bs4 import BeautifulSoup
result1='https://www.indeed.com.mx/trabajo?q=ingeniero+calidad&l=Gto.'
result2='https://www.indeed.com.mx/jobs?q=ingeniero+calidad&l=Gto.&start=10'
result3='https://www.indeed.com.mx/jobs?q=ingeniero+calidad&l=Gto.&start=20'
# result4='www.indeed.com.mx/jobs?q=ingeniero+calidad&l=Gto.&start=30'
# result5='www.indeed.com.mx/jobs?q=ingeniero+calidad&l=Gto.&start=40'
Result=requests.get(result1,result2,result3)
soup=BeautifulSoup(Result.text,'html.parser')

title_html_list=soup.find_all('div', class_='title' )
title_html_list_salary=soup.find_all('div',class_="salarySnippet salarySnippetDemphasize")

for title_html , salary in zip(title_html_list , title_html_list_salary) :
     name= title_html.a.get_text()
     salario=salary.get_text()
     print(name,salario)
