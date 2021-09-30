import json
import time
import random
import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from urllib3.exceptions import MaxRetryError

from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException


with open('videos.json') as videos_file:
  videos = json.load(videos_file)["videos"]

driver = webdriver.Chrome()

try:

  while(True):
    try:
      video = random.choice(videos)
      driver.get(video["url"])
      time.sleep(3)
      try:
        driver.find_element_by_xpath("//button[@class='ytp-large-play-button ytp-button']").click()
        driver.find_element_by_xpath("//button[@class='ytp-mute-button ytp-button']").click()
      except (ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException):
        pass

      watch_time = random.randint(int(video["duration"] * 0.7), video["duration"] + 180)

      print("Watching {0} for {1} minutes".format(
        video["name"], str(datetime.timedelta(seconds=watch_time))
      ))

      if watch_time > video["duration"]:

        time.sleep(video["duration"] + 2)

        try:
          driver.find_element_by_xpath("//button[@class='ytp-upnext-cancel-button ytp-button']").click()
        except (ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException):
          pass

        time.sleep(watch_time - (video["duration"]))
      
      else:
        time.sleep(watch_time)
    
    except WebDriverException:
      driver = webdriver.Chrome()
      

except (KeyboardInterrupt, MaxRetryError, ValueError) as e:
  driver.close()
  print("Closed by {0}".format(e))
