import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Função para pegar o caminho do chromedriver
def caminho_driver():
    if getattr(sys, 'frozen', False):  # Verifica se o código está rodando como .exe
        return os.path.join(sys._MEIPASS, 'chromedriver.exe')  # Pega o caminho do temporário do PyInstaller
    return os.path.join(os.getcwd(), 'chromedriver.exe')  # Pega o caminho normal quando está rodando o .py

def extrair_conteudo(url):
    try:
        # Opcional: abrir minimizado
        options = Options()
        driver = webdriver.Chrome(executable_path=caminho_driver(), options=options)

        print("Abrindo página...")
        driver.get(url)
        driver.minimize_window()

        print("Aguardando o conteúdo carregar...")

        xpaths_para_tentar = [
            "/html/body/div[1]/div[1]/div[2]/section/section[2]/div/section/div/div/div/div/section/div/div/p",
            "/html/body/div[1]/div[1]/div[2]/section/section[2]/div/section/div/div/div/div/section/div/p"
        ]

        paragrafo = None
        for xpath in xpaths_para_tentar:
            try:
                paragrafo = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                break  # achou, então sai do loop
            except:
                continue  # tenta o próximo

        if paragrafo:
            texto_paragrafo = paragrafo.text
            print("\nConteúdo extraído com sucesso!")
            print("\nTexto do parágrafo extraído:")
            print(texto_paragrafo)
        else:
            print("Não foi possível encontrar o conteúdo com os XPaths informados.")

    except Exception as e:
        print(f"Erro ao tentar extrair o conteúdo: {e}")
    finally:
        driver.quit()

def main():
    print("Bem-vindo ao Extrator de Conteúdo do Passei Direto!")
    url = input("Insira o URL da página: ").strip()
    if url:
        extrair_conteudo(url)
    else:
        print("URL inválida ou não fornecida.")

if __name__ == "__main__":
    main()
