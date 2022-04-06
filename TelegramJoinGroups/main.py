from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
FILE_NAME_PROFILE = r'C:\Users\pc\AppData\Local\Google\Chrome\User Data'
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=" + FILE_NAME_PROFILE)
driver = webdriver.Chrome(executable_path="C:\\Users\\chromedriver.exe", chrome_options=options)
wait = WebDriverWait(driver, 500)
url = "https://web.telegram.org/"
try:
    urlDinamic = "https://web.telegram.org/z/#-1405303803"
    driver.get(url=urlDinamic)
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="MiddleColumn"]/div[3]/div[1]/div[2]/div/button[1]/div').click()
    time.sleep(3)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
