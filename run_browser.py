from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import string

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:5000/")


