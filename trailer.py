
#import requests
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import validators

def trailerisvalid(trailer):
    if validators.url(trailer)==True:
        return True
    else:
        return False
def getTrailer(s):
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-sh-usage')
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument('--log-level=3')

    driver = webdriver.Chrome(options=option)

    try:
        url = 'https://www.imdb.com/title/tt10872600' + s + '/'
        driver.get('url') # Getting page HTML through request

        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "video.jw-video.jw-reset")))
        videoElement = driver.find_element(By.CSS_SELECTOR, "video.jw-video.jw-reset")
        #print(videoElement.get_attribute('src'))
        trailer = videoElement.get_attribute('src')
        if trailerisvalid(trailer):
            return trailer
        return 'failed'
    except Exception as e:
        print(e)
        return 'failed'
