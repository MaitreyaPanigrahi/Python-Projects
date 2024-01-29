import requests
from bs4 import BeautifulSoup
import pandas as pd

ProductName =[]
Prices =[]
Description =[]
# Reviews =[]

for i in range(1,12):

    url = "https://www.flipkart.com/search?q=laptops+under+100000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="  + str(i)

    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text,"lxml")
    # print(soup)

    box = soup.find("div",class_ = "_1YokD2 _3Mn1Gg")

    names = box.find_all("div" ,class_ = "_4rR01T")
    # print(names)

    for i in names:
        name = i.text
        ProductName.append(name)
    # print(ProductName)
    # print(len(ProductName))
        
    prices = box.find_all("div" , class_ = "_30jeq3 _1_WHN1")
    # print(prices)

    for i in prices:
        Prices.append(i.text)
    # print(Prices)

    desc = box.find_all("ul" , "_1xgFaf")
    # print(desc)

    for i in desc:
        Description.append(i.text)
    # print(Description)
        
    # rev = box.find_all("div" , class_ = "_3LWZlK")
    # for i in rev:
    #     Reviews.append(i.text)
    # print(len(Reviews))
    
df = pd.DataFrame({"Product Name" : ProductName , "Price" : Prices , "Description" : Description })

# print(df)

df.to_csv("FlipkartScrapLaptop.csv")





