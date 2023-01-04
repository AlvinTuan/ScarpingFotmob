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


URL_for_match = "https://www.fotmob.com/match/3901098/matchfacts/player-match-card/952029"
driver.get(URL_for_match)
page_source = BeautifulSoup(driver.page_source, "html.parser")
# name_home_div = page_source.find("div", "css-1f66mx0-TeamMarkup e3q4wbq5")

tag_profile_player = page_source.find("div", "css-yw6u9s-ModalContainer e1fnykti5")
# print(tag_profile_player)
name_player = tag_profile_player.find("div", "css-10x6lqx-PlayerName e1fnykti13").get_text().strip()
info_player = tag_profile_player.find("div", "css-1jaujlu-PlayerInfoContainer-applyMediumHover e1fnykti6").find_all("div")
for ip in info_player:
    info_i = ip.find_all("span")
    name_info = info_i[0].get_text().strip()
    value_info = info_i[1].get_text().strip()
    print(f"{name_info}: {value_info}")
print(name_player)
# print(info_player)