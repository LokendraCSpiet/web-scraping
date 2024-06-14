from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.by import By

# Set up Firefox WebDriver service
service = webdriver.firefox.service.Service(GeckoDriverManager().install())
service.start()

# Set up Firefox WebDriver with the service
driver = webdriver.Firefox(service=service)

# URL to open
# https://www.example.com/
# url = "https://www.geeksforgeeks.org/python-programming-language/"
url = "https://authoraditiagarwal.com/"


# Open the URL in Firefox
driver.get(url)
sleep(1)
data = driver.find_elements(By.XPATH,'//*[@id="panel-58-1-0-0"]/div/a[1]/h4')
# print(data)
for i in data:
    print(i.text)

# Close the browser window
driver.quit()
