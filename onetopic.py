from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   
import time
import locale

timeout = 10

def reading_data(driver):
    
    try:
        WebDriverWait(driver,timeout).until(
            EC.element_to_be_clickable((By.XPATH,"//*[@id='bbsTopicDetail']/div/div[2]/div[1]/p/span[5]"))
        )
        #driver.refresh()
        num = driver.find_element(By.XPATH,"//*[@id='bbsTopicDetail']/div/div[2]/div[1]/p/span[5]").text

        lang = locale.getdefaultlocale()
        if(lang[0] == 'zh_CN'):
            num = int(num[3:]) # System langue should be zh_CN
        else:
            num = int(num[7:]) # System langue is not zh_CN
        return num
        
    except:
        print('Error: Fill to get topic reading_data')
        errortime = time.strftime("%H:%M:%S")
        driver.get_screenshot_as_file('/root/Desktop/Group/Screenshot/%s.png'%errortime)
        return -999999


    
