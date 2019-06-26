
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'yourusername'
passwordStr = 'yourpassword'

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(('https:/enter page url here/'))

# fill in username and hit the next button

username = browser.find_element_by_id('username input tag id')
username.send_keys(usernameStr)

password = browser.find_element_by_id('password input tag id')
password.send_keys(passwordStr)

# nextButton = browser.find_element_by_id('identifierNext')
# nextButton.click()

# wait for transition then continue to fill items

# password = WebDriverWait(browser, 10).until(
#     EC.presence_of_element_located((By.NAME, "password")))

# password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('submit button id')
signInButton.click()