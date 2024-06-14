import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.geeksforgeeks.org/python-programming-language/")

print(r)

# print(r.content)
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())
s = soup.find('div', class_='entry-content')
content = s.find_all('p')

print(content)

