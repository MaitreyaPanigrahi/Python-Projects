import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.iplt20.com/auction/2022#:~:text=204%20players%20were%20sold%20and,IPL)%202022%20Auction%20in%20Bengaluru."

r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text , 'lxml')
# print(soup)

table = soup.find_all('table' , class_= "ih-td-tab auction-tbl")[1]
# print(table)

title = table.find_all('th')
# print(title)

header = []
for i in title:
    header.append(i.text)
df = pd.DataFrame(columns = header)

# print(df)

rows =table.find_all('tr')
# print(row)

for i in rows[1:]:
    first_td = i.find_all("td")[0].find('div' , class_ = "ih-pt-ic").text.strip()
    data = i.find_all('td')[1:]
    row = [tr.text for tr in data]
    row.insert(0,first_td)
    l = len(df)
    df.loc[l] = row
    
# print(df)
df.to_csv("tataIPlStats2.csv")