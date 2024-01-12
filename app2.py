import requests
from bs4 import BeautifulSoup
import pandas as pd

productName = []
prices =[]
decription = []
reviews = [4.5,5,4]
for i in range(2,12):


    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page= " + str(i)

    r = requests.get(url)
        # print(r)
    soup = BeautifulSoup(r.text , "lxml")

    box = soup.find("div" , class_= "_1YokD2 _3Mn1Gg")
    names = box.find_all("div" , class_ = "_4rR01T")
    # print(names)

    for i in names:
        name = i.text
        productName.append(name)
    # print(productName)
        # print(len(productName))


    price = box.find_all("div" , class_= "_30jeq3 _1_WHN1")
    # print(price)

    for i in price:
        prices.append(i.text)
    # print(prices)
        # print(len(prices))



    desc = box.find_all("ul" , class_= "_1xgFaf")
    # print(desc)

    for i in desc:
        decription.append(i.text)
    # print(decription)
        # print(len(decription))



    rev = box.find_all("div" , class_= "_3LWZlK")

    # print(rev)

    for i in rev:
        reviews.append(i.text)
    # print(reviews)
        # print(len(reviews))


df = pd.DataFrame({"Product Name" : productName ,"Price" : prices ,"Description" : decription , })

# print(df)

df.to_csv("FlipkartScrap.csv" )













    # print(soup)

    # np = soup.find("a", class_= "_1LKTO3").get("href")
    # cnp = "https://www.flipkart.com " + np 
    # print(cnp)



