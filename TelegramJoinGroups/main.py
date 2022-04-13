import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
with open("log.txt", "a") as log:
    log.write("***********Новый запуск****************************************************************************\n"*3)
with open("settings.txt", "r") as file:
    settings = file.read().split()
username = settings[1]
pauseForCheckBan = int(settings[3])
pauseForAntiBan = int(settings[5])
pauseInBann = int(settings[7])
wainingTimeElements = int(settings[9])
FILE_NAME_PROFILE = fr'C:\Users\{username}\AppData\Local\Google\Chrome\User Data'
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=" + FILE_NAME_PROFILE)
driver = webdriver.Chrome(executable_path="driver\\chromedriver.exe", chrome_options=options)
wait = WebDriverWait(driver, 500)
url = "https://web.telegram.org/"

try:
    with open("sites.txt", "r") as file:
        sites = file.read().split()
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
            for j in range(wainingTimeElements):
                time.sleep(1)
                if check_exists_by_xpath('//*[text()="Open in Web"]'):
                    driver.find_element(By.XPATH, '//*[text()="Open in Web"]').click()
                    break
                if j == (wainingTimeElements-1):
                    print('Наверно что-то с сылкой', url_Site)
                    with open("log.txt", "a") as log:
                        log.write(f"Наверно что-то с ссылкой {url_Site} \n")

        if check_exists_by_xpath('//*[text()="Join Group"]') == False and check_exists_by_xpath('//*[text()="Join Channel"]') == False:
            for j in range(wainingTimeElements):
                if check_exists_by_xpath('//*[text()="Join Group"]') is True or check_exists_by_xpath('//*[text()="Join Channel"]') is True:
                    break
                time.sleep(1)

        if check_exists_by_xpath('//*[text()="Join Group"]'):
            driver.find_element(By.XPATH, '//*[text()="Join Group"]').click()
            time.sleep(pauseForCheckBan)
            count = 0
            while check_exists_by_xpath('//*[text()="Join Group"]') and count < 20:
                count += 1
                print("we are in ban, waiting time second= ", pauseInBann, "try=", count)
                with open("log.txt", "a") as log:
                    log.write(f"we are in ban, waiting time second=  {pauseInBann} try = {count} \n")
                time.sleep(pauseInBann)
                if check_exists_by_xpath('//*[text()="Join Group"]'):
                    driver.find_element(By.XPATH, '//*[text()="Join Group"]').click()
            else:
                if count > 19:
                    print('Try > 19, some error', url_Site)
                    with open("log.txt", "a") as log:
                        log.write(f"Count > 19, some error=  {url_Site} \n")
                else:
                    print('We join to group', url_Site)
                    with open("log.txt", "a") as log:
                        log.write(f"We join to Group =  {url_Site} \n")
                    time.sleep(pauseForAntiBan)

        elif check_exists_by_xpath('//*[text()="Join Channel"]'):
            driver.find_element(By.XPATH, '//*[text()="Join Channel"]').click()
            time.sleep(pauseForCheckBan)
            count = 0
            while check_exists_by_xpath('//*[text()="Join Channel"]' and count < 20):
                count += 1
                print("We are in ban, waiting time second=", pauseInBann, "try=", count)
                with open("log.txt", "a") as log:
                    log.write(f"we are in ban, waiting time second=  {pauseInBann} try = {count} \n")
                time.sleep(pauseInBann)
                if check_exists_by_xpath('//*[text()="Join Channel"]'):
                    driver.find_element(By.XPATH, '//*[text()="Join Channel"]').click()
            else:
                if count > 19:
                    print('try > 19, some error', url_Site)
                    with open("log.txt", "a") as log:
                        log.write(f"Count > 19, some error=  {url_Site} \n")
                else:
                    print('We join to Channel', url_Site)
                    with open("log.txt", "a") as log:
                        log.write(f"We join to Channel =  {url_Site} \n")
                    time.sleep(pauseForAntiBan)
        else:
            print("don't have button Join ", url_Site)
            with open("log.txt", "a") as log:
                log.write(f"don't have button Join =  {url_Site} \n")

except Exception as ex:
    print(ex)
    with open("log.txt", "a") as log:
        log.write(f"{ex}\n")
finally:
    driver.close()
    driver.quit()