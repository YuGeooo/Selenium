from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time   

timeout = 10

def number_of_Group_members(driver):
    
    try:
        WebDriverWait(driver,timeout).until(
            EC.element_to_be_clickable((By.XPATH,"//*[@id='centerMain']/div[5]/div/a[1]"))
        )
        #driver.refresh()
        num = driver.find_element(By.XPATH,"//*[@id='centerMain']/div[1]/div/div/span[3]").text
        num = int(num[:-1])
        return num
    except:
        return 'timeout'

def number_of_Topics(driver):
    try:
        WebDriverWait(driver,timeout).until(
            EC.element_to_be_clickable((By.XPATH,"//*[@id='centerMain']/div[5]/div/a[1]"))
        )
        #driver.refresh()
        num = driver.find_element(By.XPATH,"//*[@id='centerMain']/div[1]/div/div/span[1]").text
        num = int(num[:-2])
        return num
    except:
        return 'timeout'
