from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# this function gets the info we want using beautifullsoup 
def sourcingPage(driver):
    src = driver.page_source
    
    soup = BeautifulSoup(src, 'html.parser')
    html_class = 'top-card-layout__entity-info flex-grow flex-shrink-0 basis-0 babybear:flex-none babybear:w-full babybear:flex-none babybear:w-full'
    intro = soup.find_all('div', {'class': html_class })[0]
    
    name_html = intro.find('h1', {'class':'top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0'})
    
    job_html = intro.find('h2', {'class':'top-card-layout__headline break-words font-sans text-md leading-open text-color-text'})
    
    location_html = intro.find('div',{'class':'top-card__subline-item'})
    
    data = {'name': name_html.text.strip() , 
            'job': job_html.text.strip(),
            'location': location_html.text.strip()
            }
    return data
    

path = 'C:\Program Files (x86)\chromedriver.exe'



driver = webdriver.Chrome(path)

link = 'https://www.linkedin.com/in/kunalshah1/'

driver.get(link)
# sleep is used as the webpage takes time to load 
time.sleep(5)

try:
    # closing initial popup login prompt
    element = WebDriverWait(driver , 10).until(
        EC.presence_of_element_located((By.XPATH ,'//*[@id="public_profile_contextual-sign-in"]/div/section/button' ))
    )
    element.click()
    time.sleep(5)
    doc = sourcingPage(driver)
    print(doc)
    print('pass')
    time.sleep(2)
except:
    print('fail')












