from selenium import webdriver
import time

import info
import login 
import groupdata
import TimeToSave
import onetopic

timeout = 10

def main():

    group_url = info.url('group')
    topic_url = info.url('topic')
    username = info.user('username')
    passwd = info.user('passwd')
    groupdata_loc = info.save_loc('group')
    topicdata_loc = info.save_loc('topic')

    option = webdriver.ChromeOptions()
    option.add_argument('headless') # 设置option
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=option)  # 调用带参数的谷歌浏览器

    #driver = webdriver.Chrome()
    #driver.set_window_size(1280, 720)

    # get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
    driver.get(group_url)  
    topicdata_loc = '/root/Desktop/Group/Data/onetopic.csv'
    
    # 登录
    login.login(driver,username,passwd)

    # 获取话题、人数信息
    member = groupdata.number_of_Group_members(driver)
    topic = groupdata.number_of_Topics(driver)

    last_member = int(TimeToSave.last_data(fileloc=groupdata_loc,n=4))
    last_topic = int(TimeToSave.last_data(fileloc=groupdata_loc,n=2))
    
    # 定时保存数据
    member_increase = member - last_member
    topic_increase = topic - last_topic

    TimeToSave.save_csv(data1=topic, data2=topic_increase,data3=member,data4=member_increase,fileolc=groupdata_loc)

    # 单话题阅读量跟踪

    driver.get(topic_url)

    topic_read = onetopic.reading_data(driver)
    last_read = int(TimeToSave.last_data(fileloc=topicdata_loc,n=2))
    read_increase = topic_read - last_read
    
    TimeToSave.save_csv(data1=topic_read,data2=read_increase,fileolc=topicdata_loc)

    driver.quit()  

if __name__ == '__main__':
    main()  
    # 以下区域可以写入测试代码，且不会在import入其它程序时被执行
