from selenium import webdriver
import time


import login 
import groupdata
import TimeToSave
import onetopic

timeout = 10

def main():

    url = ''
    username = ""
    passwd = ""

    option = webdriver.ChromeOptions()
    option.add_argument('headless') # 设置option
    driver = webdriver.Chrome(chrome_options=option)  # 调用带参数的谷歌浏览器

    #driver = webdriver.Chrome()
    #driver.set_window_size(1280, 720)

    # get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
    driver.get(url)  
    
    # 登录
    login.login(driver,username,passwd)

    # 获取话题、人数信息
    member = groupdata.number_of_Group_members(driver)
    topic = groupdata.number_of_Topics(driver)

    # 定时保存数据
    TimeToSave.save_csv(topic=topic[:-2], member=member[:-1],fileolc='C://Users//pc//Desktop//Codes//Group//data.csv')

    # 单话题阅读量跟踪

    url = ''
    driver.get(url)

    topic_read = onetopic.reading_data(driver)
    last_read = int(TimeToSave.last_data(fileloc='C://Users//pc//Desktop//Codes//Group//onetopic.csv',n=2))
    read_increase = topic_read - last_read
    
    TimeToSave.save_csv(topic=topic_read,member=read_increase,fileolc='C://Users//pc//Desktop//Codes//Group//onetopic.csv')

    driver.quit()  

if __name__ == '__main__':
    main()  
    # 以下区域可以写入测试代码，且不会在import入其它程序时被执行