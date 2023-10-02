from utils.crear_sesion import crear_sesion
from utils.buscar_elemento import buscar_elemento
from webelements import cas, eu, euc, eue, eug, rlm, redip
from selenium.webdriver.common.by import By
import time
import pandas as pd
from tabulate import tabulate
from utils.actualizar_dic import actualizar
from tqdm import tqdm
from config import USER, PASSW


def test_ingreso_eu():
    intentos = 0
    resultado = ""
    nodo = ""
    t_totals = ""
    url = "https://cas.gdeba.gba.gob.ar/acceso/login/?service=https://eu.gdeba.gba.gob.ar/eu-web/j_spring_cas_security_check"
    while intentos < 3:
        try:
            driver = crear_sesion()
            driver.get(url)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.input_usuario).send_keys(USER)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.input_passw).send_keys(PASSW)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.boton_acceder).click()
            t_ini = time.perf_counter()
            buscar_elemento(driver, By.CSS_SELECTOR, eu.logo)
            t_fin = time.perf_counter()
            time.sleep(3)
            t_total = t_fin - t_ini
            t_totals = str("%.2f" % t_total)
            nodo = buscar_elemento(driver, By.CSS_SELECTOR, eu.nodo).text
            resultado = "NORMAL" if t_total < 5 else "DEGRADADO"
            break

        except:
            intentos += 1
            if intentos == 3:
                screenshot = f"./screenshots/error-ingreso eu {nodo}-{time.strftime('%Y-%m-%d-%H-%M-%S')}.png"
                driver.save_screenshot(screenshot)
                resultado = "ERROR"

        finally:
            driver.close()

    return "ingreso_eu", nodo, t_totals, resultado


def test_ingreso_eug():
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
            t_ini = time.perf_counter()
            buscar_elemento(driver, By.CSS_SELECTOR, eug.logo)
            t_fin = time.perf_counter()
            time.sleep(3)
            t_total = t_fin - t_ini
            t_totals = str("%.2f" % t_total)
            nodo = buscar_elemento(driver, By.CSS_SELECTOR, eug.nodo).text
            resultado = "NORMAL" if t_total < 5 else "DEGRADADO"
            break

        except:
            intentos += 1
            if intentos == 3:
                screenshot = f"./screenshots/error-ingreso_eug {nodo}-{time.strftime('%Y-%m-%d-%H-%M-%S')}.png"
                driver.save_screenshot(screenshot)
                resultado = "ERROR"

        finally:
            driver.close()

    return "ingreso_eug", nodo, t_totals, resultado


def test_ingreso_euc():
    intentos = 0
    resultado = ""
    nodo = ""
    t_totals = ""
    while intentos < 3:
        try:
            driver = crear_sesion()
            url = "https://cas.gdeba.gba.gob.ar/acceso/login/?service=https://euc.gdeba.gba.gob.ar/ccoo-web/j_spring_cas_security_check"
            driver.get(url)
            nodo = ""

            buscar_elemento(driver, By.CSS_SELECTOR, cas.input_usuario).send_keys(USER)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.input_passw).send_keys(PASSW)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.boton_acceder).click()
            t_ini = time.perf_counter()
            buscar_elemento(driver, By.CSS_SELECTOR, euc.logo)
            t_fin = time.perf_counter()
            time.sleep(3)
            t_total = t_fin - t_ini
            t_totals = str("%.2f" % t_total)
            nodo = buscar_elemento(driver, By.CSS_SELECTOR, euc.nodo).text
            resultado = "NORMAL" if t_total < 5 else "DEGRADADO"
            break

        except:
            intentos += 1
            if intentos == 3:
                screenshot = f"./screenshots/error-ingreso_euc {nodo}-{time.strftime('%Y-%m-%d-%H-%M-%S')}.png"
                driver.save_screenshot(screenshot)
                resultado = "ERROR"

        finally:
            driver.close()

    return "ingreso_euc", nodo, t_totals, resultado


def test_ingreso_eue():
    intentos = 0
    resultado = ""
    nodo = ""
    t_totals = ""
    while intentos < 3:
        try:
            driver = crear_sesion()
            url = "https://cas.gdeba.gba.gob.ar/acceso/login/?service=https://eue.gdeba.gba.gob.ar/expedientes-web/j_spring_cas_security_check"
            driver.get(url)
            nodo = ""

            buscar_elemento(driver, By.CSS_SELECTOR, cas.input_usuario).send_keys(USER)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.input_passw).send_keys(PASSW)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.boton_acceder).click()
            t_ini = time.perf_counter()
            buscar_elemento(driver, By.CSS_SELECTOR, eue.logo)
            t_fin = time.perf_counter()
            time.sleep(3)
            t_total = t_fin - t_ini
            t_totals = str("%.2f" % t_total)
            nodo = buscar_elemento(driver, By.CSS_SELECTOR, eue.nodo).text
            resultado = "NORMAL" if t_total < 5 else "DEGRADADO"
            break

        except:
            intentos += 1
            if intentos == 3:
                screenshot = f"./screenshots/error-ingreso_eue {nodo}-{time.strftime('%Y-%m-%d-%H-%M-%S')}.png"
                driver.save_screenshot(screenshot)
                resultado = "ERROR"

        finally:
            driver.close()

    return "ingreso_eue", nodo, t_totals, resultado


def test_ingreso_rlm():
    intentos = 0
    resultado = ""
    nodo = ""
    t_totals = ""
    while intentos < 3:
        try:
            driver = crear_sesion()
            url = "https://cas.gdeba.gba.gob.ar/acceso/login/?service=https://eur.gdeba.gba.gob.ar/rlm-web/j_spring_cas_security_check"
            driver.get(url)
            nodo = ""

            buscar_elemento(driver, By.CSS_SELECTOR, cas.input_usuario).send_keys(USER)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.input_passw).send_keys(PASSW)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.boton_acceder).click()
            t_ini = time.perf_counter()
            buscar_elemento(driver, By.CSS_SELECTOR, rlm.logo)
            t_fin = time.perf_counter()
            time.sleep(3)
            t_total = t_fin - t_ini
            t_totals = str("%.2f" % t_total)
            nodo = buscar_elemento(driver, By.CSS_SELECTOR, rlm.nodo).text
            resultado = "NORMAL" if t_total < 5 else "DEGRADADO"
            break

        except:
            intentos += 1
            if intentos == 3:
                screenshot = f"./screenshots/error-ingreso_rlm {nodo}-{time.strftime('%Y-%m-%d-%H-%M-%S')}.png"
                driver.save_screenshot(screenshot)
                resultado = "ERROR"

        finally:
            driver.close()

    return "ingreso_rlm", nodo, t_totals, resultado


def test_ingreso_redip():
    intentos = 0
    resultado = ""
    nodo = ""
    t_totals = ""
    while intentos < 3:
        try:
            driver = crear_sesion()
            url = "https://cas.gdeba.gba.gob.ar/acceso/login/?service=https://redip.gdeba.gba.gob.ar/redip-web/j_spring_cas_security_check"
            driver.get(url)
            nodo = ""

            buscar_elemento(driver, By.CSS_SELECTOR, cas.input_usuario).send_keys(USER)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.input_passw).send_keys(PASSW)
            buscar_elemento(driver, By.CSS_SELECTOR, cas.boton_acceder).click()
            t_ini = time.perf_counter()
            buscar_elemento(driver, By.CSS_SELECTOR, redip.bandbox_delegacion).click()
            buscar_elemento(driver, By.CSS_SELECTOR, redip.delegacion).click()
            buscar_elemento(driver, By.CSS_SELECTOR, redip.boton_aceptar).click()
            t_fin = time.perf_counter()
            time.sleep(3)
            t_total = t_fin - t_ini
            t_totals = str("%.2f" % t_total)
            nodo = buscar_elemento(driver, By.CSS_SELECTOR, redip.nodo).text
            resultado = "NORMAL" if t_total < 5 else "DEGRADADO"
            break

        except:
            intentos += 1
            if intentos == 3:
                screenshot = f"./screenshots/error-ingreso_redip {nodo}-{time.strftime('%Y-%m-%d-%H-%M-%S')}.png"
                driver.save_screenshot(screenshot)
                resultado = "ERROR"

        finally:
            driver.close()

    return "ingreso_redip", nodo, t_totals, resultado


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
        total=6,
        ncols=90,
        colour="green",
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}",
    )

    # Ingreso Modulos
    pbar.set_description("Test Ingreso EU")
    actualizar(result_dic_con, result_dic_log, test_ingreso_eu())
    pbar.update(1)
    pbar.set_description("Test Ingreso EUG")
    actualizar(result_dic_con, result_dic_log, test_ingreso_eug())
    pbar.update(1)
    pbar.set_description("Test Ingreso EUC")
    actualizar(result_dic_con, result_dic_log, test_ingreso_euc())
    pbar.update(1)
    pbar.set_description("Test Ingreso EUE")
    actualizar(result_dic_con, result_dic_log, test_ingreso_eue())
    pbar.update(1)
    pbar.set_description("Test Ingreso RLM")
    actualizar(result_dic_con, result_dic_log, test_ingreso_rlm())
    pbar.update(1)
    pbar.set_description("Test Ingreso REDIP")
    actualizar(result_dic_con, result_dic_log, test_ingreso_redip())
    pbar.update(1)
    pbar.set_description("Finalizado")
    pbar.close()

    pdtabulate = lambda df: tabulate(
        df, headers="keys", tablefmt="pretty", showindex="never"
    )

    df_con = pd.DataFrame(result_dic_con)
    print(pdtabulate(df_con))
