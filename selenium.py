from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# Set up Firefox WebDriver with auto-installation
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# URL to open
url = "https://example.com"

# Open the URL in Firefox
driver.get(url)

# Close the browser window
driver.quit()
