"""
file code
etc để lưu driver chrome
data để lưu data lúc crawl về được.
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import datetime # lấy time lưu file
import os, time # time.sleep() và os để nói đường dẫn
import csv

def getURL():
    page_source = BeautifulSoup(driver.page_source)
    matches = page_source.find_all("a")
    all_matches_URL = []
    for match in matches[8:18]:
        match_ID = match.get("href")
        match_URL = "https://www.fotmob.com" + match_ID
        if (match_URL not in all_matches_URL):
            all_matches_URL.append(match_URL)
    return all_matches_URL


def get_criteria_of_home_away(stat_li_list):
    all_criteria_list = []
    for i in range(1,len(stat_li_list)):
        stat_span = stat_li_list[i].find_all("span")
        if (len(stat_span) == 1):
            stat_criteria = stat_span[0].get_text().strip()
            stat_home = "0"
            stat_away = "0"
        if (len(stat_span) == 2):
            if (stat_span[0].get_text().strip().isdigit()):
                stat_criteria = stat_span[1].get_text().strip()
                stat_home = stat_span[0].get_text().strip()
                stat_away = "0"
            elif (stat_span[1].get_text().strip().isdigit()):
                stat_criteria = stat_span[0].get_text().strip()
                stat_home = "0"
                stat_away = stat_span[1].get_text().strip()
            # print(f"{stat_criteria} {stat_home} {stat_away}")
        if (len(stat_span) == 3):
            stat_criteria = stat_span[1].get_text().strip()
            stat_home = stat_span[0].get_text().strip()
            stat_away = stat_span[2].get_text().strip()
        # print(f"- {stat_criteria} {stat_home} {stat_away}")
        all_criteria_list.append([stat_criteria, stat_home, stat_away])
    return all_criteria_list



if __name__ == "__main__":
    data_save_file_csv = [] # để 1 biến này chứa data lưu vào 
    url_file_driver = os.path.join("etc", "chromedriver.exe") # từ thư mục hiện tại. nối với thư mục etc và lấy file chomedriver nhé
    driver = webdriver.Chrome(executable_path=url_file_driver)
        
    
    """ all match for round
    # dropdown_box = driver.find_elements(By.TAG_NAME, value="Option")
    i = 0
    URLs_all_page = []
    while (i < len(dropdown_box)):
        dropdown_box[i].click()
        URLs_one_page = getURL()
        URLs_all_page += URLs_one_page
        if (dropdown_box[i].text == "Round 17"):
            break
        i += 1
    """
    
    # driver.get(URLs_all_page[0])
    #Test 1 match
    URL_for_match = "https://www.fotmob.com/match/3901098/matchfacts/leeds-united-vs-manchester-city"
    driver.get(URL_for_match)
    page_source = BeautifulSoup(driver.page_source, "html.parser")
    name_match = URL_for_match[URL_for_match.rfind("/")+1:]
    
    # try:

    all_stat_div = page_source.find_all("div", class_ = "css-iksjgu-ExpandableContainer e360fsv0")[1].find("div")
    middle_stat_div = all_stat_div.find("div", class_ = "middle css-1sa7xom-StatContainer-commonTitleCSS e683amr9")
    middle_ul_div = middle_stat_div.find_all("ul")
    shots = middle_ul_div[0].find_all("li")
    stat_shot_list = get_criteria_of_home_away(shots)
    expected_goals = middle_ul_div[1].find_all("li")
    stat_expected_goals_list = get_criteria_of_home_away(expected_goals)
    last_stat_div = all_stat_div.find("div", class_ = "last css-1sa7xom-StatContainer-commonTitleCSS e683amr9")
    last_ul_div = last_stat_div.find_all("ul")
    passes = last_ul_div[0].find_all("li")[:8]
    stat_passes_list = get_criteria_of_home_away(passes)
    discipline = last_ul_div[0].find_all("li")[8:]
    stat_discipline_list = get_criteria_of_home_away(discipline)
    defence = last_ul_div[1].find_all("li")[:6]
    stat_defence_list = get_criteria_of_home_away(defence)
    duels = last_ul_div[1].find_all("li")[6:]
    stat_duels_list = get_criteria_of_home_away(duels)

    
    name_file_output = f"{name_match}.csv"
    
    # print(name_folder_number)
    # print(name_match)
    with open(os.path.join(name_folder_number, name_file_output), "w+", newline="", encoding="utf-8") as file_output:
        headers = ["Evaluation criteria", "Home", "Away"]
        writer = csv.DictWriter(file_output, delimiter=',',lineterminator="\n", fieldnames=headers)
        writer.writeheader()

        writer.writerow({headers[0]:"Shots",headers[1]: "", headers[2]:""})
        for entry in stat_shot_list:
            criteria = entry[0]
            home = entry[1]
            away = entry[2]
            writer.writerow({headers[0]:criteria, headers[1]:home, headers[2]:away})

        writer.writerow({headers[0]:"Expected goals (xG)",headers[1]: "", headers[2]:""})
        for entry in stat_expected_goals_list:
            criteria = entry[0]
            home = entry[1]
            away = entry[2]
            writer.writerow({headers[0]:criteria, headers[1]:home, headers[2]:away})
        
        writer.writerow({headers[0]:"Passes",headers[1]: "", headers[2]:""})
        for entry in stat_passes_list:
            criteria = entry[0]
            home = entry[1]
            away = entry[2]
            writer.writerow({headers[0]:criteria, headers[1]:home, headers[2]:away})
        
        writer.writerow({headers[0]:"Discipline",headers[1]: "", headers[2]:""})
        for entry in stat_discipline_list:
            criteria = entry[0]
            home = entry[1]
            away = entry[2]
            writer.writerow({headers[0]:criteria, headers[1]:home, headers[2]:away})

        writer.writerow({headers[0]:"Defence",headers[1]: "", headers[2]:""})
        for entry in stat_defence_list:
            criteria = entry[0]
            home = entry[1]
            away = entry[2]
            writer.writerow({headers[0]:criteria, headers[1]:home, headers[2]:away})

        writer.writerow({headers[0]:"Duels",headers[1]: "", headers[2]:""})
        for entry in stat_duels_list:
            criteria = entry[0]
            home = entry[1]
            away = entry[2]
            writer.writerow({headers[0]:criteria, headers[1]:home, headers[2]:away})
    # print(f"The match {name_match} hasn't happened yet!!!")

    
    time.sleep(3)
    driver.close() # nhớ phải đóng 