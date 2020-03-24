# -*- coding: utf-8 -*-
import sys

from selenium import webdriver

#required for wait untill
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains



hashtags=""


import csv

def SaveHashTagsCSV(name,tagsinfo,hashtags):

    print("=====")
    with open(name+'.csv', mode='w', encoding="utf-8",newline="\n") as file:
        file = csv.writer(file, delimiter=',')#, quotechar='"', quoting=csv.QUOTE_MINIMAL

        file.writerow(["Hashtags","Publications","DailyPosts","AvgLikes"])
        for h in hashtags:
            
            print(h)
            if h in tagsinfo:
                file.writerow([h,tagsinfo[h]['publications'],tagsinfo[h]['avglikes'],tagsinfo[h]['avgcomments']])
            else:
                file.writerow([h])

def GetHashtagInformation(browser):

    try:

        #get number of publications
        test = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div[1]/div[2]/span/span')
        #print("testis boy")
        #print(test.text)
        pubnumber = int(test.text.replace(" ",""))
    except:
        print("number of publications not found or # does not exist")
        pubnumber = -1



    #get average likes and comments on top 9 posts
    try:
        test = browser.find_elements_by_css_selector(".EZdmt a")
        likes=0
        comments=0
        for el in test:

            lik, com = GetLikesandComments(el,browser)
           
            #increase counts
            likes = likes + lik
            comments = comments + com


        #average them
        comments = round(comments / len(test),2)
        likes = round(likes / len(test),2) 

    except:
        print("comments and likes not found")

    return {"publications":pubnumber,"avglikes":likes,"avgcomments":comments}

def GetLikesandComments(post,browser):
    hover = ActionChains(browser).move_to_element(post)
    hover.perform()

    #likes , comments
    try:
        return instastring2number(post.find_element_by_css_selector("li:nth-child(1) span").text) ,  instastring2number(post.find_element_by_css_selector("li:nth-child(2) span").text)
    except:
        return -1,-1

def instastring2number(s):
    s = s.replace('k','000')
    s = s.replace('m','000000')
    s = s.replace(',','')
    s = s.replace(' ','')
    return float(s)

def GetTextFromHashtaglist(hashtags): 

    hashtagtext=""

    for i in range(len(hashtags)):
        #print(hashtags[i])
        hashtagtext=hashtagtext +"#"+hashtags[i]+" "

        
    hashtagtext = hashtagtext.strip()
    print(len(hashtags))
    print(hashtagtext)
    return hashtagtext

def Gettxt2hashtagtext(path):
    
    with open(path,encoding="utf-8") as file:
        data = file.read()
        
        hashtags=data.split()
        
        return GetTextFromHashtaglist(hashtags)

         
        


def ConvertToHashtags(hashtags):

    #removes the hash
    hashtags= hashtags.replace("#","")

    #separates bt spaces
    hashtags = hashtags.split()

    #removes leading and trailing spaces
    for i in range(len(hashtags)):
        hashtags[i]=hashtags[i].strip()

    return hashtags

def readCSV(path):
    hashtags = []
    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        
        count = 0
        
        for row in spamreader:
            
            count = count+1

            if count == 1:
                continue
            
            hashtags.append(row[0])

        print(str(count) + " Hashtags loaded")
        return hashtagswith

def GetHashtags():
    return readCSV('hashtags.csv')

def removeDuplicates(l):
    prevcount = len(l)
    newlist = list( dict.fromkeys(l) )
    print(str(prevcount-len(newlist))+" duplicates found")

    return newlist

def main():

    fileCleaner()
    hashtags = readCSV('hashtags2.csv')
    hashtags = removeDuplicates(hashtags)
    print(hashtags)
    quit()
    with open('hashtags2.csv', mode='w') as file:
        file = csv.writer(file, delimiter=';')#, quotechar='"', quoting=csv.QUOTE_MINIMAL

        #file.writerow(["Hashtags","Publications","DailyPosts","AvgLikes"])
        for h in hashtags:
            #print(h)
            file.writerow([h])
    



def fileCleaner():
    file = open("hashtags.csv")

    data = file.read()

    data= data.replace("\t","")
    data= data.replace(" ","")
    file.close()
    
    with open('hashtags2.csv', 'w') as file:  # Use file to refer to the file object

        file.write(data)






if __name__ == "__main__":
    main()
