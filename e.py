# -*- coding: utf-8 -*-
import sys

from selenium import webdriver

#required for wait untill
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.action_chains import ActionChains

import credentials
import time
import datetime
import csv

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import Gdrive

import hashtags as hashtagsfuncs

browser = webdriver.Chrome('./chromedriver.exe')

#default url where tags will be appended
baseurl = "https://www.instagram.com/explore/tags/"

#from file
#hashtags = hashtags.GetHashtags()
#from text
hashtags = hashtagsfuncs.ConvertToHashtags(
"trabalhandoemcasa inovacao dinheironainternet")
hashtags = hashtagsfuncs.removeDuplicates(hashtags)



tagsinfo={}
print("================")

#cycles all hashtags
count = 0
for hashtag in hashtags:
    
    count=count+1
    browser.get(baseurl+hashtag)
    print(str(count)+"/"+str(len(hashtags))+"\t"+hashtag)


    #wait to see if pageloads/hashtagexists
    try:
        myElem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/header/div[2]/div[1]/div[1]/h1')))
        #print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!, possibly no hastag found")
        continue 

    time.sleep(1)
    
    tagsinfo[hashtag]=hashtagsfuncs.GetHashtagInformation(browser)

    print(tagsinfo[hashtag])

browser.quit()
quit()


filename ='hashtags' +  datetime.datetime.now().strftime("%m-%d-%Y %H-%M-%S")
# Save CSV
hashtagsfuncs.SaveHashTagsCSV(filename,tagsinfo,hashtags)


        




drive = Gdrive.GoogleDriveAuthenticate()
Gdrive.SaveFile(filename,'1JV2o1QnS1xc1c3tnQzvgOQKTsJZ-qnAb',filename+".csv",drive)
