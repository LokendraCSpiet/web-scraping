# If You want to scrape a website:
# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4

# Step 0: Install All Requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/"
# url = "https://www.codewithharry.com/tutorials/"

# STEP 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# STEP 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)
# print(soup.prettify)

# STEP 3: HTML Tree Traversal
#
# title = soup.title
# Commonly used types of objects:
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup
# # 4. Comment
# markup = "<p><!-- This is comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(soup2.p)
# print(soup2.p.string)
# print(type(soup2.p.string))



# Get the title of the HTML page
# title = soup.title
# print(title)

# Get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)

# Get First element in the HTML page
firstP = soup.find('p')
# print(firstP)  

# Get classes of any element in the HTML page
getElement = soup.find('p')['class']
# print(getElement)

# Find all the element with class leading-relaxed
clsParas = soup.find_all('p', class_="leading-relaxed")
# print(clsParas)

# Get the text from the tags/soup
texts = soup.find('p').get_text()
soupText = soup.get_text()
# print(texts)
# print(soupText)


# Get all the anchor from the page
anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
    # print(link)
    # print(link.get('href'))
    linkText = "https://www.codewithharry.com" + link.get('href')
    if (link.get('href') != "#" and link.get('href') != "/"):
        all_links.add(linkText)
# for lks in all_links:
    # print(lks)
        

# ----------------------Not Clear Due to proper id unavailable ------------ 
        
# navbarSupportedContent = soup.find(id="navbarSupportedContent")
# navbarSupportedContent = soup.find(id="__NEXT_DATA__")

# print(navbarSupportedContent)
# .contents - A tag's are avaiable as a list
# .children - A tag's are avaiable as a generator
# print(navbarSupportedContent.children)
# print(navbarSupportedContent.contents)
# for elem in navbarSupportedContent.contents:
#     print(elem)

# for elem in navbarSupportedContent.strings:
# for elem in navbarSupportedContent.stripped_strings:
#     print(elem)

# print(navbarSupportedContent.parent)
# print(navbarSupportedContent.parents)
# for item in navbarSupportedContent.parents:
    # print(item)
    # print(item.name)

# print(navbarSupportedContent.next_sibling.next_sibling)    # space also count as next sibling that's why we use two next
# print(navbarSupportedContent.previous_sibling)

# -------------------------------------------------------------------------------------------------------


# elem = soup.select("#__NEXT_DATA__")
elem = soup.select(".flex")
print(elem)