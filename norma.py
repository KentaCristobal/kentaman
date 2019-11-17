# import csv
# import urllib.request, urllib.error
# from bs4 import BeautifulSoup
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#
# # URLの指定
#
# url="http://www.ordenjuridico.gob.mx/despliegaedo.php?idMunicipio=331&edo=11&vienedeojn=si"
# html=urllib.request.urlopen(url=url)
# bsObj = BeautifulSoup(html, "html.parser")
#
# # テーブルを指定
# table = bsObj.findAll("table", {"class":"txt_gral"})[1]
# rows = table.findAll("tr")
# print(rows)
# # with open("ebooks.csv", "w", encoding='utf-8') as file:
# #     writer = csv.writer(file)
# # for row in rows:
# #         csvRow = []
# #         for cell in row.findAll(['td', 'th']):
# #             csvRow.append(cell.get_text())
# #         writer.writerow(csvRow)
#






import requests,openpyxl
from bs4 import BeautifulSoup
result1='http://www.ordenjuridico.gob.mx/despliegaedo.php?idMunicipio=331&edo=11&vienedeojn=si.'
Result1=requests.get(result1)
soup1=BeautifulSoup(Result1.text,'html.parser')
print(soup1)
#
# title1=soup1.find_all('div',id_='testTable' )
# print(title1)
# for i in title1:
#     print(title1.a.get_text())
