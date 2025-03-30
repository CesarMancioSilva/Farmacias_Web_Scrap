import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getFarmacias():

    driver = webdriver.Chrome()
    url_farmacia = os.getenv("URL_FARMACIA")

    driver.get(url_farmacia)


    botao = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'btn-address--full-size')]"))
    )
    botao.click()

    elementos = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "merchant-v2__link"))
    )
    farmacias=[]
    for elemento in elementos:
        link = elemento.get_attribute("href")
        farmacia={}
        farmacia['id']=link.split('/')[-1]
        farmacia['name']=link.split('/')[-2].replace('-',' ').replace('  ',' ')
        farmacias.append(farmacia)

    driver.quit()
    return farmacias