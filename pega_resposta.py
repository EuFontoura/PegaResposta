import tkinter as tk
from tkinter import scrolledtext
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import threading

def extrair_conteudo(url, output_widget):
    try:
        options = Options()
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        driver.minimize_window()

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
                break
            except:
                continue

        output_widget.delete('1.0', tk.END)
        if paragrafo:
            texto_paragrafo = paragrafo.text
            output_widget.insert(tk.END, "✅ Conteúdo extraído com sucesso:\n\n" + texto_paragrafo)
        else:
            output_widget.insert(tk.END, "❌ Não foi possível encontrar o conteúdo com os XPaths informados.")

    except Exception as e:
        output_widget.insert(tk.END, f"⚠️ Erro ao tentar extrair o conteúdo: {e}")
    finally:
        driver.quit()

def iniciar_extracao(entry, output):
    url = entry.get().strip()
    if url:
        threading.Thread(target=extrair_conteudo, args=(url, output)).start()
    else:
        output.delete('1.0', tk.END)
        output.insert(tk.END, "❗ URL inválida ou não fornecida.")

def criar_interface():
    janela = tk.Tk()
    janela.title("Extrator do Passei Direto")
    janela.geometry("600x400")

    tk.Label(janela, text="Insira a URL da página:").pack(pady=10)

    entrada_url = tk.Entry(janela, width=80)
    entrada_url.pack(pady=5)

    botao_extrair = tk.Button(janela, text="Extrair Conteúdo", command=lambda: iniciar_extracao(entrada_url, saida_texto))
    botao_extrair.pack(pady=10)

    saida_texto = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=70, height=15)
    saida_texto.pack(padx=10, pady=10)

    janela.mainloop()

if __name__ == "__main__":
    criar_interface()
