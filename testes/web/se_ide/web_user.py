# Generated by Selenium IDE
# 1- Bibliotecas
import pytest
import time
import json


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 2- Classes (Grupos de Definições / Métodos e funções)
class TestIncluirusuario():

    # 3- Definições/métodos ou funções
    # 3.1 - Configura
    # 3.1.1 - Método de inicialização do WebDriver


    def setup_method(self, method):
        self.driver = webdriver.Chrome('C:\\Users\\Particular\\PycharmProjects\\133pets\\vendors\\driver\\chrome\\chromedriver.exe')  # instanciando o Selenium / Carregando na memória
        self.vars = {}  # Criando uma lista vazia

    # 3.1.2 - Método de encerramento para desligar o Selenium
    def teardown_method(self, method):
        self.driver.quit()  # Destroi o objeto do Selenium / descarrega da memória

    # 4- Executa
    def test_incluirusuario(self):
        self.driver.get("https://blazedemo.com/")
        self.driver.set_window_size(848, 1006)
        self.driver.find_element(By.LINK_TEXT, "home").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("Brunno Cavalcante Dornelas da Silva")
        self.driver.find_element(By.ID, "company").send_keys("Iterasys")
        self.driver.find_element(By.ID, "email").send_keys("dornellas_12@hotmail.com")
        self.driver.find_element(By.ID, "password").send_keys("dornellas123")
        self.driver.find_element(By.ID, "password-confirm").send_keys("dornellas123")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".message").click()

    # 5- Valida
        assert self.driver.find_element(By.CSS_SELECTOR, ".message").text == "Page Expired"

