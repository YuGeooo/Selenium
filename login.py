from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time   

timeout = 10

def login(driver,username,passwd):

    # time.sleep(1)  
    try:
        WebDriverWait(driver,timeout).until(
            EC.element_to_be_clickable((By.XPATH,"//*[@id='loginBtn']"))
        )

        # 输入账号密码
        driver.find_element(By.XPATH,"//*[@id='phone']").send_keys(username)
        driver.find_element(By.XPATH,"//*[@id='pwd']").send_keys(passwd)

        # 点击登录
        driver.find_element(By.XPATH,"//*[@id='loginBtn']").click()
    
    except:
        print("登录页加载超时")
        driver.quit() 