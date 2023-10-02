from utils.crear_sesion import crear_sesion
from utils.buscar_elemento import buscar_elemento
from webelements import cas, eug
from selenium.webdriver.common.by import By
import time
import os
import pandas as pd
from tabulate import tabulate
from utils.actualizar_dic import actualizar
from tqdm import tqdm
from config import USER, PASSW


def test_firmar_gedo(acronimo):
    intentos = 0
    resultado = ""
    nodo = ""
    t_totals = ""
    while intentos < 3:
        try:
            driver = crear_sesion()
            url = "https://cas.gdeba.gba.gob.ar/acceso/login/?service=https://eug.gdeba.gba.gob.ar/gedo-web/j_spring_cas_security_check"
            driver.get(url)
            nodo = ""

            buscar_elemento(driver, By.CSS_SELECTOR, cas.input_usuario).send_keys(USER)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.input_passw).send_keys(PASSW)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.boton_acceder).click()

            buscar_elemento(driver, By.XPATH, eug.boton_inicio_documento).click()
            buscar_elemento(driver, By.CSS_SELECTOR, eug.input_acronimo).send_keys(
                acronimo
            )
            buscar_elemento(
                driver, By.CSS_SELECTOR, eug.boton_producir_yo_mismo
            ).click()
            buscar_elemento(driver, By.XPATH, eug.input_motivo).send_keys(
                "Documento de prueba. Carece de motivacion administrativa"
            )
            time.sleep(1)

            if acronimo == "TESTL":
                driver.switch_to.frame(1)
                # Escribo en el body
                editor_body = driver.find_element(By.XPATH, "//body")
                editor_body.send_keys(
                    "Documento de prueba. Carece de motivacion administrativa."
                )
                # Salgo del ckeditor
                driver.switch_to.default_content()

            if acronimo == "TESTT":
                buscar_elemento(
                    driver, By.CSS_SELECTOR, "input[name='pers']"
                ).send_keys("Sr.")
                buscar_elemento(
                    driver, By.CSS_SELECTOR, "input[name='nomyape']"
                ).send_keys("Prueba")
                buscar_elemento(driver, By.CSS_SELECTOR, "input[name='dni']").send_keys(
                    "12345678"
                )
                buscar_elemento(driver, By.CSS_SELECTOR, "input[name='mes']").send_keys(
                    "Enero"
                )
                buscar_elemento(
                    driver, By.CSS_SELECTOR, "input[name='anio']"
                ).send_keys("2022")
                buscar_elemento(
                    driver, By.CSS_SELECTOR, "input[name='dependencia']"
                ).send_keys("Dirección Provincial de Mejora Administrativa")

            if acronimo == "TESTI":
                buscar_elemento(
                    driver, By.CSS_SELECTOR, 'input[name="file"]'
                ).send_keys(os.path.abspath("imagen.png"))
            time.sleep(1)

            buscar_elemento(driver, By.XPATH, eug.boton_firmar_yo_mismo).click()
            buscar_elemento(driver, By.XPATH, eug.boton_firmar_con_certificado).click()
            t_ini = time.perf_counter()
            nro_gedo = buscar_elemento(
                driver, By.XPATH, eug.span_nro_gedo
            ).text.split()[14]
            t_fin = time.perf_counter()
            t_total = t_fin - t_ini
            t_totals = str("%.2f" % t_total)
            nodo = buscar_elemento(driver, By.CSS_SELECTOR, eug.nodo).text
            resultado = "NORMAL" if t_total < 5 else "DEGRADADO"
            break

        except:
            intentos += 1
            if intentos == 3:
                screenshot = f"./screenshots/error-firmar gedo {nodo}-{time.strftime('%Y-%m-%d-%H-%M-%S')}.png"
                driver.save_screenshot(screenshot)
                resultado = "ERROR"

        finally:
            driver.close()

    return f"firmar_gedo ({acronimo})", nodo, t_totals, resultado, nro_gedo


def test_firmar_portafirma():
    intentos = 0
    resultado = ""
    nodo = ""
    t_totals = ""
    while intentos < 3:
        try:
            driver = crear_sesion()
            url = "https://cas.gdeba.gba.gob.ar/acceso/login/?service=https://eug.gdeba.gba.gob.ar/gedo-web/j_spring_cas_security_check"
            driver.get(url)
            nodo = ""

            buscar_elemento(driver, By.CSS_SELECTOR, cas.input_usuario).send_keys(USER)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.input_passw).send_keys(PASSW)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.boton_acceder).click()

            buscar_elemento(driver, By.XPATH, eug.boton_portafirma).click()
            for num in range(
                11, 16
            ):  # Evaluamos que el problema se encuentra en esta linea. El problema evaluado surgede la necesidad de creacion de nuevas tareas
                buscar_elemento(
                    driver,
                    By.XPATH,
                    f"(//span[@class='z-listitem-checkable z-listitem-checkbox'])[{num}]",
                ).click()
            buscar_elemento(driver, By.XPATH, eug.boton_firmar_seleccionados).click()
            buscar_elemento(driver, By.XPATH, eug.boton_firmar_con_certificado).click()
            t_ini = time.perf_counter()
            buscar_elemento(driver, By.XPATH, eug.boton_volver).click()
            t_fin = time.perf_counter()
            t_total = t_fin - t_ini
            t_totals = str("%.2f" % t_total)
            nodo = buscar_elemento(driver, By.CSS_SELECTOR, eug.nodo).text
            resultado = "NORMAL" if t_total < 25 else "DEGRADADO"
            break

        except:
            intentos += 1
            if intentos == 3:
                screenshot = f"./screenshots/error-firmar portafirma {nodo}-{time.strftime('%Y-%m-%d-%H-%M-%S')}.png"
                driver.save_screenshot(screenshot)
                resultado = "ERROR"

        finally:
            driver.close()

    return f"firmar_gedo (5 GEDOS)", nodo, t_totals, resultado


def test_buscar_documento(nro_gedo):
    intentos = 0
    resultado = ""
    nodo = ""
    t_totals = ""
    while intentos < 3:
        try:
            driver = crear_sesion()
            url = "https://cas.gdeba.gba.gob.ar/acceso/login/?service=https://eug.gdeba.gba.gob.ar/gedo-web/j_spring_cas_security_check"
            driver.get(url)
            nodo = ""

            buscar_elemento(driver, By.CSS_SELECTOR, cas.input_usuario).send_keys(USER)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.input_passw).send_keys(PASSW)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.boton_acceder).click()
            buscar_elemento(
                driver, By.XPATH, "//input[@placeholder='Ingrese el número']"
            ).send_keys(nro_gedo)
            time.sleep(1)
            buscar_elemento(driver, By.XPATH, "//button[@title='Buscar']").click()
            t_ini = time.perf_counter()
            buscar_elemento(
                driver,
                By.XPATH,
                "//div[contains(text(),'Cantidad de registros encontrados: 1')]",
            )
            t_fin = time.perf_counter()
            t_total = t_fin - t_ini
            t_totals = str("%.2f" % t_total)
            nodo = buscar_elemento(driver, By.CSS_SELECTOR, eug.nodo).text
            resultado = "NORMAL" if t_total < 5 else "DEGRADADO"
            break

        except:
            intentos += 1
            if intentos == 3:
                screenshot = f"./screenshots/error-buscar documento {nodo}-{time.strftime('%Y-%m-%d-%H-%M-%S')}.png"
                driver.save_screenshot(screenshot)
                resultado = "ERROR"

        finally:
            driver.close()

    return f"buscar_documento", nodo, t_totals, resultado, nro_gedo


if __name__ == "__main__":
    result_dic_con = {
        "TEST": [],
        "NODO": [],
        "TIEMPO (seg)": [],
        "RESULTADO": [],
        "NRO GDEBA": [],
    }
    result_dic_log = {
        "TEST": [],
        "NODO": [],
        "TIEMPO (seg)": [],
        "RESULTADO": [],
        "NRO GDEBA": [],
    }
    pbar = tqdm(
        total=5,
        ncols=90,
        colour="green",
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}",
    )

    # Funcionalidad GEDO
    pbar.set_description("Test Firmar gedo (TESTL)")
    d = test_firmar_gedo("TESTL")
    actualizar(result_dic_con, result_dic_log, d)
    pbar.update(1)
    pbar.set_description("Test Firmar gedo (TESTT)")
    actualizar(result_dic_con, result_dic_log, test_firmar_gedo("TESTT"))
    pbar.update(1)
    pbar.set_description("Test Firmar gedo (TESTI)")
    actualizar(result_dic_con, result_dic_log, test_firmar_gedo("TESTI"))
    pbar.update(1)
    pbar.set_description("Test Firmar portafirma")
    actualizar(result_dic_con, result_dic_log, test_firmar_portafirma())
    pbar.update(1)
    pbar.set_description("Test Buscar Documento")
    actualizar(result_dic_con, result_dic_log, test_buscar_documento(d[4]))
    pbar.update(1)
    pbar.set_description("Finalizado")
    pbar.close()

    pdtabulate = lambda df: tabulate(
        df, headers="keys", tablefmt="pretty", showindex="never"
    )

    df_con = pd.DataFrame(result_dic_con)
    print(pdtabulate(df_con))
