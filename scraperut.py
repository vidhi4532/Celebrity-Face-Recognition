# import requests
# from bs4 import BeautifulSoup
# name= ['scarlett+johansson','emilia+clarke']
# for i in name:
#     url='https://www.google.com/search?q='+i+'&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi20ryc9ZXqAhXuyzgGHS2sBrAQ_AUoAXoECCEQAw&biw=1920&bih=969'
#     source_code = requests.get(url)
#     html_code = source_code.text
#     soup = BeautifulSoup(html_code)
#     for link in soup.find_all("img"):
#         src=link.get('src')
#         print(src)

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
print("What do you want to download?")
download = input()
site = 'https://www.google.com/search?tbm=isch&q='+download


driver = webdriver.Chrome()
driver.get(site)


for i in range(1,2):
    print(i)
    try :
        element = driver.find_element_by_xpath(f"/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[{i}]/a[1]")
        element.click()

        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img"))
        )

        smallerElement = driver.find_element_by_xpath(f"/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[{i}]/a[1]/div[1]/img")
        smallerImg = smallerElement.get_attribute("src")
        
        bigimage = driver.find_element_by_xpath(f"/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img")
        j=0
        while (bigimage.get_attribute("src") == smallerImg):
            time.sleep(0.01)
            j+=1
            if j==1000:
                break
        if j == 1000:
            continue
        url = bigimage.get_attribute('src')

        ext = url.split('/')[-1].split('.')[-1]
        if ext!='jpg':
            ext='jpg'
        r = requests.get(url)
        open(f"{i}.{ext}", 'wb').write(r.content)
    except:
        pass

driver.close()






