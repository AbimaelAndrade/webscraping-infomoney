import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    return webdriver.Chrome(options=chrome_options)

def get_infomoney_data():
    url = "https://www.infomoney.com.br/ferramentas/altas-e-baixas/"
    driver = get_driver()
    driver.get(url)

    try:
        wait = WebDriverWait(driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, "//td[text()='Carregando...']")))
        
        element = wait.until(EC.presence_of_element_located((By.ID, "altas_e_baixas")))
        tabela_html = element.get_attribute("outerHTML")

        driver.quit()

        soup = BeautifulSoup(tabela_html, "html.parser")
        return soup
    except Exception as e:
        print("Ocorreu um erro ao buscar a tabela:", e)
        driver.quit()
