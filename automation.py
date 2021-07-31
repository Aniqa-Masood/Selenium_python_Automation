from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import datetime 
import dateutil.relativedelta

custom_options = webdriver.ChromeOptions()

prefs = {
  "translate_whitelists": {"ko":"en"},
  "translate":{"enabled":"true"},
  'profile.default_content_setting_values.automatic_downloads': 2
}
custom_options.add_experimental_option("prefs", prefs)
driver=webdriver.Chrome(executable_path='./drivers/chromedriver', options=custom_options)
driver.maximize_window()
driver.get('https://sell.smartstore.naver.com/#/login')

#Login
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.panel.panel-seller > ul > li:nth-child(2) > a'))
)
element.click()

driver.find_element_by_name("id").send_keys("kym790910")
driver.find_element_by_name("pw").send_keys("!kmg0309")
driver.find_element_by_css_selector('#log\.login').click()

#Click on Settlement Management Pay
elementt = WebDriverWait(driver, 80).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-lnb > div > div > ul > li:nth-child(3) > a'))
)
elementt.click()

#Click on Settlement history
eleement = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-lnb > div > div > ul > li.active > ul > li:nth-child(1) > a'))
)
eleement.click()

time.sleep(10)
popup = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#seller-content > div > div > div > div.modal-body > ncp-manager-notice-view > ng-transclude > button > span'))
)
popup.click()

time.sleep(3)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
time.sleep(5)

today = datetime.date.today()
first = today.replace(day=1)
lastMonth = first - datetime.timedelta(days=1)
setfirstdate = lastMonth.strftime("%Y.%m.%d")
print(setfirstdate)

elm = driver.find_element_by_class_name("_vPU3io1OlM._3nQyzAMCad")
driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", elm,  "value",  setfirstdate)

#Excel Down
exceldown = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div._MTTpEfT64i._2pDX4NrI9f > div > button:nth-child(2)'))
)
exceldown.click()


'''Chrome Default Download path'''
folder_download = 'C:\\Users\\Aniqa Masood\\Downloads'
old_file_name = "SellerDailySettle.xlsx"
new_nam=lastMonth.strftime("%Y%m%d")
new_file_name=str(new_nam)+'LALA.xlsx'

#Wait until file download
while not os.path.exists(os.path.join(folder_download, old_file_name)):
    time.sleep(2)

#Rename
if os.path.isfile(os.path.join(folder_download, old_file_name)):
     os.rename(os.path.join(folder_download, old_file_name), os.path.join(folder_download, new_file_name))
else:
    raise ValueError("%s isn't a file!" % old_file_name)
