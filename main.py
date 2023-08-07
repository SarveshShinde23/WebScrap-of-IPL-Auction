#Import the lib. requests, bs4 and pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd
#url is cpoy from the website where we are working
url="https://www.iplt20.com/auction"
r= requests.get(url)

#we need to lxml lib. we need to install for run this following code"pip install lxml"
soup=BeautifulSoup(r.text,"lxml")
#print(soup)

#getting table Header
table=soup.find("table",class_ = "ih-td-tab auction-tbl")
title=table.find_all("th")

#creating the Item header to store the values of columns and its is used by the for loop
header=[]
for i in title:
    name=i.text
    header.append(name)

df=pd.DataFrame(columns=header)

row=table.find_all("tr")
for i in row[1:]:
    first_td=i.find_all("td")[0].find("div", class_="ih-pt-ic").text.strip()
    data=i.find_all("td")[1:]
    row=[tr.text for tr in data]
    row.insert(0,first_td)
    l=len(df)
    df.loc[l]=row
print(df)

#To store the data in CSV
df.to_csv("IPL Auction File")
