from selenium import webdriver
import credentials
import time

browser = webdriver.Chrome('./chromedriver.exe')


browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

time.sleep(5)

elem = browser.find_element_by_name("username")
elem.send_keys(credentials.username)

elem = browser.find_element_by_name("password")
elem.send_keys(credentials.password)

#login
elem = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
elem.click()

#agora nao

time.sleep(2)
elem = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
elem.click()

#pesquizar
elem = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
elem.click()



elem.send_keys("teste")


#https://www.instagram.com/explore/search/
#search for hashtag
elem = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/a')
elem.click()

#https://www.facebook.com/login/?next=%2Fcreatorstudio%2F%3Freference%3Dvisit_from_seo

