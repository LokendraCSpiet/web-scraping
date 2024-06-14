import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
import time
from urllib.parse import urlparse, urlunparse
chromedriver_autoinstaller.install()
options = Options()
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
urls = ["https://blinkit.com/cn/milk/cid/14/922","https://blinkit.com/cn/bread-pav/cid/14/953","https://blinkit.com/cn/eggs/cid/14/1200","https://blinkit.com/cn/flakes-kids-cereals/cid/14/954","https://blinkit.com/cn/muesli-granola/cid/14/614","https://blinkit.com/cn/oats/cid/14/584","https://blinkit.com/cn/paneer-tofu/cid/14/923","https://blinkit.com/cn/curd-yogurt/cid/14/123","https://blinkit.com/cn/butter-more/cid/14/952","https://blinkit.com/cn/cheese/cid/14/2253","https://blinkit.com/cn/cream-whitener/cid/14/1092","https://blinkit.com/cn/condensed-milk/cid/14/130","https://blinkit.com/cn/vermicelli/cid/14/1140","https://blinkit.com/cn/poha-daliya-other-grains/cid/14/1295","https://blinkit.com/cn/peanut-butter/cid/14/644","https://blinkit.com/cn/energy-bars/cid/14/2557","https://blinkit.com/cn/milk-drinks/cid/14/1184","https://blinkit.com/cn/breakfast-mixes/cid/14/1612","https://blinkit.com/cn/honey-chyawanprash/cid/14/609","https://blinkit.com/cn/sausage-salami-ham/cid/14/1388","https://blinkit.com/cn/batter/cid/14/1425"]
data = {'Product Name': [], 'Product Price': [], 'Product Image': [], 'Product URL': []}
for url in urls:
    driver.get(url)
    time.sleep(2)
    # Image sources
    image_elements = driver.find_elements(By.CSS_SELECTOR, 'div.Product__UpdatedImage-sc-11dk8zk-4 img')
    if image_elements:
        for image_element in image_elements:
            src = image_element.get_attribute('src')
            parsed_url = urlparse(src)
            clean_url = urlunparse(parsed_url._replace(query=""))
            data['Product Image'].append(clean_url)
            print("clean_url : ", clean_url)
    else:
        data['Product Image'].append("NA")
    # Product titles
    title_elements = driver.find_elements(By.CLASS_NAME, 'Product__UpdatedTitle-sc-11dk8zk-9')
    if title_elements:
        for title_element in title_elements:
            product_title = title_element.text
            data['Product Name'].append(product_title)
            print("product_title: ", product_title)
    else:
        data['Product Name'].append("NA")
    # Prices
    price_elements = driver.find_elements(By.CSS_SELECTOR, '.Product__UpdatedPriceAndAtcContainer-sc-11dk8zk-10 > div > div')
    if price_elements:
        for price_element in price_elements:
            price_text = price_element.text
            data['Product Price'].append(price_text)
            print("price_text: ", price_text)
    else:
        data['Product Price'].append("NA")
    # Product links
    link_elements = driver.find_elements(By.CSS_SELECTOR, 'a[data-test-id="plp-product"]')
    if link_elements:
        for link_element in link_elements:
            href = link_element.get_attribute('href')
            data['Product URL'].append(href)
            print("href: ", href)
    else:
        data['Product URL'].append("NA")
driver.quit()
# Check all lists are the same length and append "NA" if not
max_length = max(len(lst) for lst in data.values())
for key in data.keys():
    while len(data[key]) < max_length:
        data[key].append("NA")
# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)
# Filter out rows where any column has "NA"
filtered_df = df.replace("NA", pd.NA).dropna()
# Save the filtered DataFrame to an Excel file
filtered_df.to_excel('dairy_and_breakfast.xlsx', index=False)
print("Data collection completed and filtered data saved to Excel.")