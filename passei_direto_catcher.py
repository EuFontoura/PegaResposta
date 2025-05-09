from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL_PAGINA = input("Insira o url da página: ")

# Inicializa o WebDriver
driver = webdriver.Chrome()

# Abre a página
driver.get(URL_PAGINA)

# Aguarda até que o parágrafo esteja presente na página
paragrafo = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/section/section[2]/div/section/div/div/div/div/section/div/div/p"))
)

# Pega o texto do parágrafo
texto_paragrafo = paragrafo.text
print(texto_paragrafo)

# Encerra o WebDriver
driver.quit()
