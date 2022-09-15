from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   
import time
import locale

import TimeToSave

timeout = 10

def reading_data(xpath,driver):
    
    if(xpath == 1):
        x = "//*[@id='bbsTopicDetail']/div/div[2]/div[1]/p/span[5]"
    elif(xpath == 2):
        x = "//*[@id='noteMainWrap']/div/div[3]/div[1]/span[4]/span"
        #print('2')
    try:
        WebDriverWait(driver,timeout).until(
            EC.element_to_be_clickable((By.XPATH,x))
        )
        #driver.refresh()
        num = driver.find_element(By.XPATH,x).text
        print(num)
        lang = locale.getdefaultlocale()
        if(lang[0] == 'zh_CN'):
            num = int(num[3:]) # System langue should be zh_CN
            print('zh')
        else: 
            num = int(num[6:]) # System langue is not zh_CN
            print('En')
        return num
        
    except:
        print('Error: Fill to get topic reading_data')
        errortime = time.strftime("%H:%M:%S")
        driver.get_screenshot_as_file('/root/Desktop/Group/Screenshot/%s.png'%errortime)
        return -999999

def topicdata(xpath,driver,topicdata_loc):
            
    topic_read = reading_data(xpath,driver)
    last_read = int(TimeToSave.last_data(fileloc=topicdata_loc,n=2))
    read_increase = topic_read - last_read
    TimeToSave.save_csv(data1=topic_read,data2=read_increase,fileolc=topicdata_loc)


    
