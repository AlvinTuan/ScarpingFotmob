from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import datetime # lấy time lưu file
import os, time # time.sleep() và os để nói đường dẫn
import csv

data_save_file_csv = [] # để 1 biến này chứa data lưu vào 
url_file_driver = os.path.join("etc", "chromedriver.exe") # từ thư mục hiện tại. nối với thư mục etc và lấy file chomedriver nhé
driver = webdriver.Chrome(executable_path=url_file_driver)


URL_for_match = "https://www.fotmob.com/match/3901094/matchfacts/brentford-vs-tottenham-hotspur"
driver.get(URL_for_match)
page_source = BeautifulSoup(driver.page_source, "html.parser")
name_match = URL_for_match[URL_for_match.rfind("/")+1:]
# name_home_div = page_source.find("div", "css-1f66mx0-TeamMarkup e3q4wbq5")
name_div = page_source.find_all("span", "css-er0nau-TeamName e3q4wbq4")
name_home_div = name_div[0].find("span").get_text().strip()
name_away_div = name_div[1].find("span").get_text().strip()
name_match = f"{name_home_div} VS {name_away_div}"
print(name_match)

# next_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/main[1]/main[1]/div[1]/div[1]/div[5]/section[1]/section[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]/*[name()='svg'][1]/*[name()='g'][1]/*[name()='g'][1]/*[name()='circle'][1]")
# next_button.click()

