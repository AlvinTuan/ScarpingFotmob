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


URL_for_match = "https://www.fotmob.com/match/3901098/matchfacts/player-match-card/796974"
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

position_player = info_player[0].find_all("span")
if (position_player[1].get_text().strip() == "GK"):
    ul_dict = tag_profile_player.find("ul", "css-1szro0h-StatSection e1fnykti12")
    li_list = ul_dict.find_all("li")
    hearder = li_list[0].get_text().strip()
    print(hearder)
    fotmob_rating = li_list[1].find("span").get_text().strip()
    fotmob_rating_value = li_list[1].find("div").find("span").get_text().strip()
    print(fotmob_rating, fotmob_rating_value)
    for entry in li_list[2:]:
        criteria_span_list = entry.find_all("span")
        evaluation_criteria = criteria_span_list[0].get_text().strip()
        value_ec = criteria_span_list[1].get_text().strip()
        print(evaluation_criteria, value_ec)
else:
    ul_dict = tag_profile_player.find_all("ul", "css-1szro0h-StatSection e1fnykti12")[0]
    li_list = ul_dict.find_all("li")
    hearder = li_list[0].get_text().strip()
    print(hearder)
    fotmob_rating = li_list[1].find("span").get_text().strip()
    fotmob_rating_value = li_list[1].find("div").find("span").get_text().strip()
    print(fotmob_rating, fotmob_rating_value)
    for entry in li_list[2:]:
        criteria_span_list = entry.find_all("span")
        evaluation_criteria = criteria_span_list[0].get_text().strip()
        value_ec = criteria_span_list[1].get_text().strip()
        print(evaluation_criteria, value_ec)
    # ul_attack
    ul_attack = tag_profile_player.find_all("ul", "css-1szro0h-StatSection e1fnykti12")[1]
    li_attack = ul_dict.find_all("li")
    hearder = li_list[0].get_text().strip()
    print(hearder)
    for entry in li_attack[1:]:
        criteria_span_list = entry.find_all("span")
        evaluation_criteria = criteria_span_list[0].get_text().strip()
        value_ec = criteria_span_list[1].get_text().strip()
        print(evaluation_criteria, value_ec)


print(name_player)
# print(info_player)