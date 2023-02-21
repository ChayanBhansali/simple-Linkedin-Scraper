from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
time.sleep(5)

try:
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













# classname = 'modal__overlay flex items-center bg-color-background-scrim justify-center fixed bottom-0 left-0 right-0 top-0 opacity-0 invisible pointer-events-none z-[1000] transition-[opacity] ease-[cubic-bezier(0.25,0.1,0.25,1.0)] duration-[0.17s] modal__overlay--full-page p-0 modal__overlay--visible'
# try:
#     element = WebDriverWait(driver , 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME , classname))
#     )
#     # element.click()

#     print('done')
# except:
#     print('fail')
#     driver.quit()    
# # cross = driver.find_element(By.CLASS_NAME ,"modal__dismiss btn-tertiary h-[40px] w-[40px] p-0 rounded-full indent-0 contextual-sign-in-modal__modal-dismiss absolute right-0 m-[20px] cursor-pointer" )
# # cross.click()
# time.sleep(50)
# # contextual-sign-in-modal__modal-dismiss-icon lazy-loaded