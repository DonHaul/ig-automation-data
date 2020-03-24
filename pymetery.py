
#file dialog
#elem = browser.find_element_by_xpath('/html/body/div[12]/div/div/div/div/div/a/div/input')
elem = browser.find_elements_by_css_selector("#js_cq6")
path = os.getcwd()
path = os.path.join(path, "Kiyosaki.jpg")

import autoit

#input dialog
#//*[@id="js_hum"]

autoit.win_active("Open")
autoit.control_send("Open","Edit1",r"C:\Users\uu\Desktop\TestUpload.txt")
autoit.control_send("Open","Edit1","{ENTER}")