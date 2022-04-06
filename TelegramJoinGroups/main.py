import random
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
FILE_NAME_PROFILE = r'C:\Users\pc\AppData\Local\Google\Chrome\User Data'
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=" + FILE_NAME_PROFILE)
driver = webdriver.Chrome(executable_path="C:\\Users\\chromedriver.exe", chrome_options=options)
wait = WebDriverWait(driver, 500)
url = "https://web.telegram.org/"
try:
    sites = ["https://t.me/DarkProbiv", "https://t.me/RaychatDM", "https://t.me/city_blackkk", "https://t.me/opencardingchat", "https://t.me/CicadaHere", "https://t.me/RaychatDM", "https://t.me/carding_chatik", "https://t.me/probivclub", "https://t.me/freeesaucee", "https://t.me/freeesaucee", "https://t.me/hack_mom", "https://t.me/city_blackkk", "https://t.me/carding_chatik", "https://t.me/delovoy_sng", "https://t.me/hack_mom", "https://t.me/S_Y_P_E_R_S"]
    pauseForCheckBan = 10
    pauseForAntiBan = random.randint(100, 200)
    pauseInBann = random.randint(600, 900)

    def check_exists_by_xpath(xpath):
        try:
            driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True

    for url_Site in sites:
        driver.get(url_Site)

        if check_exists_by_xpath('//*[text()="Open in Web"]'):
            driver.find_element(By.XPATH, '//*[text()="Open in Web"]').click()
        else:
            for j in range(10):
                time.sleep(1)
                if check_exists_by_xpath('//*[text()="Open in Web"]'):
                    driver.find_element(By.XPATH, '//*[text()="Open in Web"]').click()
                    break
                if j == 9:
                    print('не найдена кнопка open in web')

        if check_exists_by_xpath('//*[text()="Join Group"]') == False and check_exists_by_xpath('//*[text()="Join Channel"]') == False:
            for j in range(10):
                time.sleep(1)
                if check_exists_by_xpath('//*[text()="Join Group"]') is not False and check_exists_by_xpath('//*[text()="Join Channel"]') is not False:
                    break

        if check_exists_by_xpath('//*[text()="Join Group"]'):
            driver.find_element(By.XPATH, '//*[text()="Join Group"]').click()
            time.sleep(pauseForCheckBan)
            if check_exists_by_xpath('//*[text()="Join Group"]'):
                print("we are in ban, waiting time =", pauseInBann)
                time.sleep(pauseInBann)
            else:
                print('We join to group', url_Site)

        elif check_exists_by_xpath('//*[text()="Join Channel"]'):
            driver.find_element(By.XPATH, '//*[text()="Join Channel"]').click()
            time.sleep(pauseForCheckBan)
            if check_exists_by_xpath('//*[text()="Join Channel"]'):
                print("We are in ban, waiting time =", pauseInBann)
                time.sleep(pauseInBann)
            else:
                print('We join to Channel', url_Site)

        else:
            print("don't have button Join ", url_Site)
    time.sleep(pauseForAntiBan)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()