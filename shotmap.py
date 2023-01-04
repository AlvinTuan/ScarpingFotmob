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


URL_for_match = "https://www.fotmob.com/match/3901098/matchfacts/leeds-united-vs-manchester-city"
driver.get(URL_for_match)
page_source = BeautifulSoup(driver.page_source, "html.parser")
name_match = URL_for_match[URL_for_match.rfind("/")+1:]
# name_home_div = page_source.find("div", "css-1f66mx0-TeamMarkup e3q4wbq5")
map_div = page_source.find("div", "css-kfmc1b-FullscreenShotmapContainer-applyLightHover-ShotmapAnimations-commonShotMapContainer e1786a3a20")
# print(map_div)
circle_map_div = map_div.find_all("circle")
# print(circle_map_div)
dot_x = []
dot_y = []
for circle in circle_map_div:
    dot_x.append(circle.get("cx"))
    dot_y.append(circle.get("cy"))

with open(os.path.join("data", "shotmaps.csv"), "w+", newline="", encoding="utf-8") as file_output:
    headers = ["x", "y"]
    writer = csv.DictWriter(file_output, delimiter=',',lineterminator="\n", fieldnames=headers)
    writer.writeheader()

    for entry in zip(dot_x, dot_y):
        shot_x = entry[0]
        shot_y = entry[1]
        writer.writerow({headers[0]:shot_x, headers[1]:shot_y})

driver.close()