from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def buscar_elemento(driver, tipo_selector, elemento):
    return WebDriverWait(driver, 20).until(
        ec.presence_of_element_located((tipo_selector, elemento))
    )
