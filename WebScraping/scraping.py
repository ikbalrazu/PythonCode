import urllib.request
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
#global variable
address = "https://www.rottentomatoes.com/m/you_go_to_my_head/reviews"
page = urllib.request.urlopen(address)
soup = BeautifulSoup(page,'html.parser')
#print(soup.prettify())

Movie_Name = soup.find_all('div',attrs={'class':'the_review'})
#print(Movie_Name)
for i in Movie_Name:
    print(i.get_text(),"\n")