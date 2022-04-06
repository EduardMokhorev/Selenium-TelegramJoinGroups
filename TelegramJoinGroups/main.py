from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
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

    def check_exists_by_xpath(xpath):
        try:
            driver.find_element(By.XPATH,xpath)
        except NoSuchElementException:
            return False
        return True

    urlTelegram = "https://web.telegram.org/"
    urlDinamic = "https://t.me/DeepWeb_Chatt"
    driver.get(url=urlTelegram)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="telegram-search-input"]').send_keys(urlDinamic)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="telegram-search-input"]').send_keys(Keys.RETURN)
    time.sleep(2)
    if check_exists_by_xpath('//*[text()="Join Group"]'):
        driver.find_element(By.XPATH, '//*[text()="Join Group"]').click()
        print('Have Element')
        time.sleep(100)
    else:
        print("SomeTroubleWith",urlDinamic)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
