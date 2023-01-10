import time
from schedule import repeat, every, run_pending
import os

@repeat(every(2).seconds)
def scraping_data():
    os.system('python understat_data_scraping.py')
    os.system('python mysql_connect_and_upload.py')
    os.system('python data_dashboard.py')

while True:
    run_pending()
    time.sleep(1)