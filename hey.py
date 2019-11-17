import requests,openpyxl
from bs4 import BeautifulSoup

wb=openpyxl.Workbook()
wa=wb.active

result=requests.get('https://www.indeed.com.mx/jobs?q=ingeniero&l=irapuato')
soup=BeautifulSoup(result.text,'html.parser')
title_html_list=soup.find_all('div', class_='title' )
title_html_list_salary=soup.find_all('div',class_="salarySnippet salarySnippetDemphasize")

for title_html in title_html_list :
    name= title_html.a.get_text()
    wa.cell(row=1,column=1).value=name

# for list_salary in  title_html_list_salary :
#     salary=list_salary.get_text()
#     wa.cell().value=salary


wb.save(r'C:\Users\kenta takayasu\Desktop\practica\sample.xlsx')
