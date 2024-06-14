import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
from urllib.parse import urlparse, urlunparse
chromedriver_autoinstaller.install()
options = Options()
driver = webdriver.Chrome(options=options)

driver.get('https://www.dmart.in/')

# pincodeInput

try:
    search_box = driver.find_element(By.ID, "pincodeInput")
    search_box.clear()
    search_box.send_keys("302003") # enter your name in the search box
    search_box.submit # submit the search
    sleep(10)

    # results = driver.find_elements(By.XPATH, "//*[@id='b_tween']/span")
    # for result in results:
    #     text = result.text.split()[1] # extract the number of results
    #     print(text)
    # # save it to a file
    # with open("results.txt", "w") as f:
    #     f.write(text)
except Exception as e:
    print(f"An error occurred: {e}")





# send = driver.find_element(By.ID,"pincodeInput").send_keys("Jaipur", Keys.ENTER)




# send = driver.find_element(By.NAME,"select-locality").send_keys("Jaipur", Keys.ENTER)
# btn location-box mask-button


# # players = driver.find_elements_by_xpath('//td[@class="name"]')
# # players_list = []
# # for p in range(len(players)):
# #     players_list.append(players[p].text)

# # print(players_list)
# # driver.close()
