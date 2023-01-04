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


if __name__ == "__main__":
    data_save_file_csv = [] # để 1 biến này chứa data lưu vào 
    url_file_driver = os.path.join("etc", "chromedriver.exe") # từ thư mục hiện tại. nối với thư mục etc và lấy file chomedriver nhé
    driver = webdriver.Chrome(executable_path=url_file_driver)

    #Test 1 match
    URL_for_match = "https://www.fotmob.com/match/3901098/matchfacts/leeds-united-vs-manchester-city"
    driver.get(URL_for_match)
    page_source = BeautifulSoup(driver.page_source, "html.parser")
    name_match = URL_for_match[URL_for_match.rfind("/")+1:]

    # try:

    score_div = page_source.find("div", "css-vargkq")
    score = score_div.find_all("span")[0].get_text().strip()
    full_time = score_div.find_all("span")[1].get_text().strip()
    
    print(f"{full_time}: {score}")

    lineup_home_info = page_source.find("div", "css-whn3yu-TeamContainer eu5dgts3").find_all("div", "css-11d04mc-RowContainer eu5dgts4")
    # print(lineup_home_info)
    # print(len(lineup_home_info))
    for player in lineup_home_info:
        player_proflies = player.find_all("a")
        for player_info in player_proflies:
            number_of_player = player_info.find("span", "css-1y4ddg1-Shirt elhbny55").get_text().strip()
            url_player_in_match = "https://www.fotmob.com" + player_info.get("href")
            driver.get(url_player_in_match)
            tag_profile_player = page_source.find("div", "css-146rg3s-StyledReactModal__Overlay css-146rg3s-StyledReactModal__Overlay--after-open")
            print(tag_profile_player)
            
        break
            # ---------------------------------------------------
            # name_player = tag_profile_player.find("div", "css-10x6lqx-PlayerName e1fnykti13").get_text().strip()
            # print(number_of_player, name_player)

    #     # player_profile = player.find("a").get("href")
    #     # print(player_profile)
    # name_file_output = f"{name_match}.csv"
    
    # # print(name_folder_number)
    # # print(name_match)
    # with open(os.path.join("testFiles", name_file_output), "w+", newline="", encoding="utf-8") as file_output:
    #     headers = ["Evaluation criteria", "Home", "Away"]
    #     writer = csv.DictWriter(file_output, delimiter=',',lineterminator="\n", fieldnames=headers)
    #     writer.writeheader()

    #     writer.writerow({headers[0]:"Shots",headers[1]: "", headers[2]:""})
    #     for entry in stat_shot_list:
    #         criteria = entry[0]
    #         home = entry[1]
    #         away = entry[2]
    #         writer.writerow({headers[0]:criteria, headers[1]:home, headers[2]:away})

    #     writer.writerow({headers[0]:"Expected goals (xG)",headers[1]: "", headers[2]:""})
    #     for entry in stat_expected_goals_list:
    #         criteria = entry[0]
    #         home = entry[1]
    #         away = entry[2]
    #         writer.writerow({headers[0]:criteria, headers[1]:home, headers[2]:away})
        
    #     writer.writerow({headers[0]:"Passes",headers[1]: "", headers[2]:""})
    #     for entry in stat_passes_list:
    #         criteria = entry[0]
    #         home = entry[1]
    #         away = entry[2]
    #         writer.writerow({headers[0]:criteria, headers[1]:home, headers[2]:away})
        
    #     writer.writerow({headers[0]:"Discipline",headers[1]: "", headers[2]:""})
    #     for entry in stat_discipline_list:
    #         criteria = entry[0]
    #         home = entry[1]
    #         away = entry[2]
    #         writer.writerow({headers[0]:criteria, headers[1]:home, headers[2]:away})

    #     writer.writerow({headers[0]:"Defence",headers[1]: "", headers[2]:""})
    #     for entry in stat_defence_list:
    #         criteria = entry[0]
    #         home = entry[1]
    #         away = entry[2]
    #         writer.writerow({headers[0]:criteria, headers[1]:home, headers[2]:away})

    #     writer.writerow({headers[0]:"Duels",headers[1]: "", headers[2]:""})
    #     for entry in stat_duels_list:
    #         criteria = entry[0]
    #         home = entry[1]
    #         away = entry[2]
    #         writer.writerow({headers[0]:criteria, headers[1]:home, headers[2]:away})
    # print(f"The match {name_match} hasn't happened yet!!!")

    
    time.sleep(3)
    driver.close() # nhớ phải đóng 