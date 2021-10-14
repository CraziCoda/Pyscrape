from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.get("https://www.google.com")
time.sleep(10)

try:
    assert "Google" in driver.title
except AssertionError:
    print("Couldn't open page")
search = driver.find_element_by_name('q')
search.clear()
q = input("Enter Search: ")
search.send_keys(q)
search.send_keys(Keys.RETURN)


def grab_data(soup):
    results = soup.find_all(class_="yuRUbf")
    file = open("Results.txt", "w")
    file.write("")
    file.close
    for result in results:
        link = result.find('a')['href']
        contents = result.find('h3').string
        # print(link + " : " + contents)
        with open("Results.txt", "a") as file:
            file.write(link + " : " + contents + "\r\n")


try:
    el = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "g"))
    )
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    grab_data(soup)

    time.sleep(10)
    print("All Done")
    driver.close()

except:
    print("An error occured")
    driver.close()
