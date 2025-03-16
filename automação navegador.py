from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

senha = os.environ.get("SENHA_ZPE")
email = os.environ.get("EMAIL_SEI")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

navegador.get("https://sei.pi.gov.br/")

navegador.find_element('xpath','/html/body/div[1]/div[3]/div/div[2]/form/div/div[2]/input[1]').send_keys (email)

navegador.find_element('xpath','/html/body/div[1]/div[3]/div/div[2]/form/div/div[2]/input[2]').send_keys (senha)

navegador.find_element('xpath','/html/body/div[1]/div[3]/div/div[2]/form/div/div[2]/select[1]').send_keys('z')

navegador.find_element('xpath',"/html/body/div[1]/div[3]/div/div[2]/form/div/div[4]/div[2]/button").click()

navegador.find_element('xpath','/html/body/div[1]/div[2]/div[1]/div[5]/span/form/select').click()

# **clausula de espera caso precise, trecho não adaptado
try:
    element = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located('xpath',"/html/body/div[1]/div[2]/div[1]/div[5]/span/form/select"))
    
finally:
    navegador.quit()

#navegador.find_element('xpath','/html/body/div[1]/div[2]/div[1]/div[5]/span/form/select/option[17]').click()

navegador.find_element('xpath','/html/body/div[1]/div[2]/div[1]/div[5]/span/form/select/option[17]').click()
#/html/body/div[1]/div[2]/div[1]/div[5]/span/form/select
