# -*- coding: utf-8 -*-
import sys

from selenium import webdriver

#required for wait untill
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.action_chains import ActionChains

import time
import datetime
import csv

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import Gdrive

import hashtags as hashtagsfuncs



hashtagsfuncs.Gettxt2hashtagtext("hashtags_genericas.txt")