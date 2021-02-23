from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38"
connect_with_page = ureq(my_url)
page_html = connect_with_page.read()
connect_with_page.close()
#html parsing
page_soup = BeautifulSoup(page_html,"html.parser")
#print(page_soup.h1)
#print(soup.prettify())

product_container =page_soup.find_all("div",{"class":"item-container"})
print(len(product_container))
#print(product_container[1])
#save the data in csv file
file_name = "productsinfo.csv"
f = open(file_name,"w")
headers = "brand,product_name,shipping"
f.write(headers)
for i in product_container:
    product_brand = i.div.div.a.img["title"]
    product_title = i.findAll("a",{"class":"item-title"})
    shipping_container = i.findAll("li",{"class":"price-ship"})
    #print(i.get_text(),"\n")
    #print(product_brand)
    product_name = product_title[0].text
    shipping = shipping_container[0].text.strip()
    print("brand: " + product_brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)
    f.write(product_brand+","+product_name.replace(",","|")+","+shipping+"\n")
f.close()