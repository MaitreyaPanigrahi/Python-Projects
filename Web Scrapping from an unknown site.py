import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
#print(r)

soup = BeautifulSoup(r.text,'lxml')
#print(soup)

# boxes = soup.find_all("div" , class_= "col-md-4 col-xl-4 col-lg-4")
# print(len(boxes))

productName = []
productDetails = {}

names = soup.find_all("a" , class_ = "title")
# print(names)
for i in names:
    productName.append(i.text)

# print(productName)





productPrice = []
prices = soup.find_all("h4",class_="float-end price card-title pull-right")
# # print(prices)
for i in prices:
    productPrice.append(i.text)

productReview =[]
review = soup.find_all("p" , class_="float-end review-count")

for i in review:
    productReview.append(i.text)

productNameAndPrice= dict(zip(productName,productPrice))
print(productNameAndPrice)
productNameAndReview = dict(zip(productName , productReview))
print(productNameAndReview)

