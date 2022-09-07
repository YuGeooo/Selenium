from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   

timeout = 10

def reading_data(driver):
    
    try:
        WebDriverWait(driver,timeout).until(
            EC.element_to_be_clickable((By.XPATH,"//*[@id='bbsTopicDetail']/div/div[2]/div[1]/p/span[5]"))
        )
        #driver.refresh()
        num = driver.find_element(By.XPATH,"//*[@id='bbsTopicDetail']/div/div[2]/div[1]/p/span[5]").text
        num = int(num[3:]) # System langue should be zh_CN
        #num = int(num[7:]) # EN
        return num
        
    except:
        print('Error: Fill to get topic reading_data')
        return -999999


    