import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from urllib.parse import urlparse, urlunparse
import os


chromedriver_autoinstaller.install()
options = Options()
driver = webdriver.Chrome(options=options)

# driver.get('https://www.dmart.in/')
# https://www.dmart.in/category/grocery-aesc-grocerycore
# https://www.dmart.in/category/appliances-aesc-appliancescore
# https://www.dmart.in/category/dairy---beverages-aesc-dairyandbeveragescore
# https://www.dmart.in/category/personal-care-aesc-personalcarecore


# Define a function to scroll to the bottom of the page
def scroll_to_bottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait for a brief moment to allow content to load
        time.sleep(2)
        # Calculate new scroll height and compare with the last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


urls = ["https://www.dmart.in/category/grocery-aesc-grocerycore","https://www.dmart.in/category/baby---kids-aesc-babyandkidscore","https://www.dmart.in/category/clothing-accessories-aesc-clothingaccessories","https://www.dmart.in/category/dairy---beverages-aesc-dairyandbeveragescore","https://www.dmart.in/category/personal-care-aesc-personalcarecore","https://www.dmart.in/category/specials-aesc-specialscore"]
# data = {
#     "Product Name" : [],
#     "Product Dmart Price" : [],
#     "Product MRP Price" : [],
#     "Product Image" : [],
#     # "Product URL" : []
# }

try:
    for url in urls:
        driver.get(url)
        data = {
            "Product Name" : [],
            "Product Dmart Price" : [],
            "Product MRP Price" : [],
            "Product Image" : [],
            "Product URL" : []
        }
        # Scroll to the bottom of the page to load all content
        scroll_to_bottom(driver)

        # images = driver.find_elements(By.CLASS_NAME, "vertical-card_image__UIjvR.vertical-card_grow-no-stock__JLXUE")
        images = driver.find_elements(By.CSS_SELECTOR, "div.vertical-card_image__UIjvR")
        for image in images:
            style_attr = image.get_attribute('style')
            imgUrls = style_attr.split('url("')[1:]
            first_url = imgUrls[0].split('"')[0]
            data['Product Image'].append(first_url)
        
        names = driver.find_elements(By.CLASS_NAME, "vertical-card_title__awihj")
        for name in names:
            data['Product Name'].append(name.text)
        
        # prices = driver.find_elements(By.CLASS_NAME,"vertical-card_amount__muVeb")
        # prices = driver.find_elements(By.CLASS_NAME,"vertical-card_price-container__EtssH")   
        prices = driver.find_elements(By.CSS_SELECTOR,"section.vertical-card_price-container__EtssH")
        # print((prices[1].text).strip().splitlines())
        for price in prices:
            p_text = price.text

            dmart_index = p_text.find("DMart")
            if dmart_index != -1:  # Check if "DMart" is found in the text
                dmart_price = p_text[dmart_index:].split("₹")[1].strip()  # Extract DMart price
                # print("DMart Price:", dmart_price)
                data['Product Dmart Price'].append(dmart_price)

            MRP_index = p_text.find("MRP")
            if MRP_index != -1:  # Check if "MRP" is found in the text
                MRP_price = p_text[MRP_index:].split("₹")[1].strip()  # Extract MRP price
                # print("MRP Price:", MRP_price)
                data['Product MRP Price'].append(MRP_price)

            # else:
            #     print("DMart price not found in:", p_text)
                

        # print("All Data")
        # print(data['Product Name'])
        # print(len(data['Product Name']))
        # print(len(data['Product Dmart Price']))
        # print(len(data['Product MRP Price']))
        # print(len(data['Product Image']))
        # print(len(data['Product URL']))
        max_lenght = max(len(lst) for lst in data.values())
        for key in data.keys():
            while len(data[key]) < max_lenght:
                if(key == "Product URL"):
                    data[key].append(url)
                else:
                    data[key].append("NA")
        df = pd.DataFrame(data)

        dir = "Projects/"
        file_name = url.split("-")[-1]
        df.to_excel(dir+file_name+"(Test).xlsx", index=False)
    print("Data collection completed and filtered data saved to Excel.")
except Exception as e:
    print(f"An error occurred: {e}")


