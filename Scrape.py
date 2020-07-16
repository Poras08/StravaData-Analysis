import bs4 as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# using chrome web to access the url
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="./chromedriver ", options=chrome_options)
driver.get(" https://www.strava.com/login/")

# User data to access website
email = input(" Enter your email : ")
password = input(" Enter your password : ")
Email_search = driver.find_element_by_id("email")
Email_search.send_keys(email)
Password_search = driver.find_element_by_id("password")
Password_search.send_keys(password)
Login_search = driver.find_element_by_id("login-button")
Login_search.send_keys(Keys.RETURN)

# to delay program so that the next element will load on the page, also for that program would not quit directly
time.sleep(10)

# get the activity id to get link for web page to extract data
Activity_id = input("activity id :")
url = "https://www.strava.com/activities/" + Activity_id + "/overview/"
driver.get(url)
# Title of Page
print(driver.title)

time.sleep(10)
html = driver.page_source
dfs = pd.read_html(html)
dfs[1].to_csv('Activity_id'+Activity_id+'.csv')

# Page Source to get more details
#print(html)
# convert html source to soup data for more analysis
soup = bs.BeautifulSoup(html,'html.parser')
ul_primary_stats = soup.find('ul',class_='inline-stats section')
print(ul_primary_stats.text)

ul_secondary_stats = soup.find('ul',class_='inline-stats section secondary-stats')
print(ul_secondary_stats.text)

