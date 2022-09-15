from selenium import webdriver
import time

import info
import login 
import onetopic

timeout = 10

def main():

    username = info.user('username')
    passwd = info.user('passwd')

    topic_url = info.url('topic')
    topicdata_loc = info.save_loc('topic')

    # Chrome参数设置

    option = webdriver.ChromeOptions()
    option.add_argument('headless') # 设置option
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=option)  # 调用带参数的谷歌浏览器

    #driver = webdriver.Chrome()
    #driver.set_window_size(1280, 720)
    
    # 单话题阅读量跟踪
    
    driver.get(topic_url)
    login.login(driver,username,passwd)
    onetopic.topicdata(1,driver,topicdata_loc)

    # 关闭浏览器
    
    driver.quit()  

if __name__ == '__main__':
    main()  
    # 以下区域可以写入测试代码，且不会在import入其它程序时被执行
