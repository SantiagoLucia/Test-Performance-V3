from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import logging
import os

# desactiva el log del webdriver manager
os.environ["WDM_LOG"] = str(logging.NOTSET)

# guardo binarios en local
os.environ["WDM_LOCAL"] = "1"


def crear_sesion():
    """inicia Chrome con los parametros indicados y devuelve el driver"""
    # OPCIONES DE CHROME:
    options = ChromeOptions()  # instanciar las opciones de Chrome
    # options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")  # maximiza la ventana de Chrome
    # options.add_argument("--headless")  # ejecutar sin abrir la ventana
    # options.add_argument("--disable-gpu")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")  # no muestre nada en la terminal
    options.add_argument(
        "--allow-running-insecure-content"
    )  # desactiva el aviso de contenido no seguro
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_argument("--no-proxy-server")
    options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )  # evita que selenium sea detectado por el navegador
    # parametros para omitir en el inicio
    exp_opt = [
        "enable-automation",
        "ignore-certificate-errors",
        "enable-logging",  # para que no muestre el devtools listening
    ]
    options.add_experimental_option("excludeSwitches", exp_opt)
    # parametros de preferencias
    prefs = {
        "profile.default_content_setting_values.notificatios": 2,  # notificaciones: 0=preguntar 1=permitir 2=no permitir
        "credentials_enable_service": False,  # para evitar que chrome pregunte si quiero guardar contraseñas
    }
    options.add_experimental_option("prefs", prefs)

    # instanciar webdriver de selenium con Chrome
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options,
    )
    return driver


if __name__ == "__main__":
    driver = crear_sesion()
