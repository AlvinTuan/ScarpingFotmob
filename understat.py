from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import os, time # time.sleep() và os để nói đường dẫn
import csv


def data_gga_to_CSV(name_league):
    with open(os.path.join(f"data/{name_league}/", f"g-and-ga-{name_league}.csv"), "w+", newline="", encoding="utf-8") as file_output:
        headers = ["Team", "G", "GA"]
        writer = csv.DictWriter(file_output, delimiter=',',lineterminator="\n", fieldnames=headers)
        writer.writeheader()

        for entry in mem_g_ga:
            team_name = entry[0]
            goals_for = entry[1]
            goals_againist = entry[2]
            writer.writerow({headers[0]:team_name, headers[1]:goals_for, headers[2]:goals_againist})

def data_xgxga_to_CSV(name_league):
    with open(os.path.join(f"data/{name_league}/", f"xg-and-xga-{name_league}.csv"), "w+", newline="", encoding="utf-8") as file_output:
        headers = ["Team", "xG", "xGA"]
        writer = csv.DictWriter(file_output, delimiter=',',lineterminator="\n", fieldnames=headers)
        writer.writeheader()

        for entry in mem_xg_xga:
            team_name = entry[0]
            expected_goals_for = entry[1]
            expected_goals_againist = entry[2]
            writer.writerow({headers[0]:team_name, headers[1]:expected_goals_for, headers[2]:expected_goals_againist})

if __name__ == "__main__":

    NAME_LEAGUES = ["EPL", "La_liga", "Bundesliga" , "Serie_A", "Ligue_1"]

    url_file_driver = os.path.join("etc", "chromedriver.exe")
    driver = webdriver.Chrome(executable_path=url_file_driver)


    for league in NAME_LEAGUES:
        driver.get(f"https://understat.com/league/{league}/2022")
        page_source = BeautifulSoup(driver.page_source, "html.parser")

        table_div = page_source.find("div", "chemp margin-top jTable").find("table")
        table_team_row = table_div.find("tbody").find_all("tr")

        mem_g_ga = []
        mem_xg_xga = []
        for row in table_team_row:
            data = row.find_all("td")
            team = data[1].find("a").get_text().strip()
            g = data[6].get_text().strip()
            ga = data[7].get_text().strip()
            xg_value = data[9].get_text().strip()
            xg = xg_value[:5]
            xga_value = data[10].get_text().strip()
            xga = xga_value[:5]
            mem_g_ga.append([team,g,ga])
            mem_xg_xga.append([team,xg,xga])
        data_gga_to_CSV(league)
        data_xgxga_to_CSV(league)

time.sleep(3)
driver.close()

