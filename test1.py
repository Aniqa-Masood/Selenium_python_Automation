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

def tiny_file_rename(newname, folder_of_download):
    filename = max([f for f in os.listdir(folder_of_download)], key=lambda xa :   os.path.getctime(os.path.join(folder_of_download,xa)))
    if '.part' in filename:
        time.sleep(1)
        os.rename(os.path.join(folder_of_download, filename), os.path.join(folder_of_download, newname))
    else:
        os.rename(os.path.join(folder_of_download, filename),os.path.join(folder_of_download,newname))

element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/ui-view[1]/div[3]/div/div/div/form/div[1]/ul/li[2]/a'))
)
element.click()

driver.find_element_by_name("id").send_keys("kym790910")
driver.find_element_by_name("pw").send_keys("!kmg0309")
driver.find_element_by_xpath("""//*[@id="log.login"]""").click()


elementt = WebDriverWait(driver, 80).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/button'))
)
elementt.click()

eleement = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/span[2]/button'))
)
eleement.click()

driver.find_element_by_xpath("""//*[@id="seller-lnb"]/div/div[1]/ul/li[3]/a""").click()
driver.find_element_by_xpath("""//*[@id="seller-lnb"]/div/div[1]/ul/li[3]/ul/li[1]/a""").click()

time.sleep(3)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
time.sleep(10)
lastdate=driver.find_element_by_xpath("""//*[@id="endDate"]/input""")
lastdate=lastdate.get_attribute("value")
print(lastdate)

lastdate = datetime.datetime.strptime(lastdate, "%Y.%m.%d")
firstdate = lastdate + dateutil.relativedelta.relativedelta(months=-1)
setfirstdate=firstdate.strftime("%Y.%m.%d")
print(setfirstdate)

driver.find_element_by_xpath("""//*[@id="startDate"]/input""").click()
driver.execute_script('document.getElementsByName("startDate")[0].removeAttribute("readonly")')
driver.find_element_by_xpath("""//*[@id="startDate"]/input""").clear()
driver.find_element_by_xpath("""//*[@id="startDate"]/input""").send_keys(setfirstdate)
driver.find_element_by_xpath("""//*[@id="content"]/div/div[2]/div[8]/div[1]/div/button[2]""").click()
time.sleep(4)

'''Chrome Default Download path'''
folder_download='D:\\Downloads'
new_nam=firstdate.strftime("%Y%m%d")
new_name=str(new_nam)+'LALA.xlsx'
tiny_file_rename(new_name, folder_download)