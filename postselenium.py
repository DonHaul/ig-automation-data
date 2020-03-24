from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
import pandas
import FileIO

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
    


def LogIn( credentials):
    '''
    Start WebDriver and LogIn,
    Requires a dictionary with the username and the password
    '''

    #If you want emojis it only works in firefox
    browser = webdriver.Firefox()

    #default url where tags will be appended
    baseurl = "https://www.facebook.com/login/?next=%2Fcreatorstudio%2F%3Freference%3Dvisit_from_seo"
    browser.get(baseurl)

    elem = browser.find_element_by_name("email")
    elem.send_keys(credentials["username"])

    elem = browser.find_element_by_name("pass")
    elem.send_keys(credentials["password"])

    elem = browser.find_element_by_name("login")
    elem.click()

    #switch to insta tab
    elem = browser.find_element_by_xpath('//*[@id="media_manager_chrome_bar_instagram_icon"]')
    elem.click()

    return browser


def SchedulePost(data,browser):
    '''
    receive data to post
    and the driver or browser
    '''
    
    #wait to post pan to close, used after every post is posted
    readytopost = False
    while(readytopost == False):
        
        try:
            #if window is open stay in loop
            elem =  browser.find_element_by_xpath("//*[contains(text(), 'Post to Instagram')]")
            print("Waiting")
        except:
            readytopost = True
    
        time.sleep(1)

    #Ready to post


    #Click Create Post
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Create Post"))).click()

    #Click instagram feed button    
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Instagram feed')]"))).click()


    #insert description in new post pan
    descriptionelem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='creator_studio_sliding_tray_root']/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div[2]/div")))

    #send description. Line breaks are replaced by ENTERs    
    descriptionelem.send_keys(data["Description"].replace("\n",Keys.ENTER))


    if pandas.isnull(data['Location']) == False:

        #find location and insert location
        browser.find_element_by_xpath("//*[contains(text(), 'Add location')]/../following-sibling::span//input").click()

        elem.send_keys(data['Location'])
        elem.send_keys(Keys.RETURN)

        #loose focus on location
        elem = browser.find_element_by_xpath("//*[contains(text(), 'Add location')]/../following-sibling::span").click()


        
    #set image
    #click the add content button, to make the input appear
    browser.find_elements_by_xpath("//*[contains(text(), 'Add content')]")[-1].click()
  
    elem = browser.find_element_by_xpath('//input[@accept="video/*, image/*"]')
    elem.send_keys(data['Image']);

    

    #set date

    #dropdown publish button and then click the shedule
    browser.find_elements_by_xpath('//i')[-1].click()
    browser.find_elements_by_xpath("//*[contains(text(), 'Schedule')]")[-1].click()


    #if date is set, fetch it and inser it here
    if pandas.isnull(data['Post Date']) == False:    
        post_date = data['Post Date'].date().strftime("%d/%m/%Y")
        
        #date
        elem = browser.find_element_by_xpath("//input[@placeholder='dd/mm/yyyy']")
        elem.click()
        elem.send_keys(post_date)

    if pandas.isnull(data['Post Time']) == False:
        hours = data['Post Time'].strftime("%H")
        minutes = data['Post Time'].strftime("%M")
    else:
        #default time
        hours = "17"
        minutes = "00"

    #set hours
    elem = browser.find_element_by_xpath("//span[@aria-label='hours']/preceding-sibling::input")
    elem.send_keys(hours)

    #set minutes
    elem = browser.find_element_by_xpath("//span[@aria-label='minutes']/preceding-sibling::input")
    elem.send_keys(minutes)


    #submit
    elem =  browser.find_element_by_xpath("//button//div[contains(text(), 'Schedule')]")
    elem.click()


    