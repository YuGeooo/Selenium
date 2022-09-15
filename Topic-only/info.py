username = ""
passwd = ""

topic_url = ''
topicdata_loc = ''

def user(a):
    if(a=='username'):
        return username
    elif(a=='passwd'):
        return passwd

def url(a):   
    if(a=='topic'):
        return topic_url

def save_loc(a):
    if(a=='topic'):
        return topicdata_loc
