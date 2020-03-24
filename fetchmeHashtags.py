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

drive = Gdrive.GoogleDriveAuthenticate()



# Initialize GoogleDriveFile instance with file id.
file6 = drive.CreateFile({'id': '1CRMNtKquIblI6ZnOvszqPzYXKX7xFlkc'})
file6.GetContentFile('catlove.xlsx') # Download file as 'catlove.png'.

# Initialize GoogleDriveFile instance with file id.
file7 = drive.CreateFile({'id': '1CRMNtKquIblI6ZnOvszqPzYXKX7xFlkc'})
content = file7.GetContentString()
# content: '{"firstname": "Claudio", "lastname": "Afshar"}'

print(content)




