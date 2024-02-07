from utils.crear_sesion import crear_sesion
from utils.buscar_elemento import buscar_elemento
from webelements import cas, eue
from selenium.webdriver.common.by import By
import time
import pandas as pd
from tabulate import tabulate
from utils.actualizar_dic import actualizar
from tqdm import tqdm
from config import USER, PASSW


def test_caratular_expediente():
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
            buscar_elemento(
                driver, By.CSS_SELECTOR, eue.boton_caratular_interno
            ).click()
            buscar_elemento(
                driver, By.CSS_SELECTOR, eue.textarea_motivo_interno
            ).send_keys("Expediente de prueba. Carece de motivacion administrativa.")
            buscar_elemento(
                driver, By.CSS_SELECTOR, eue.textarea_motivo_externo
            ).send_keys("Expediente de prueba. Carece de motivacion administrativa.")
            buscar_elemento(driver, By.XPATH, eue.input_codigo_tramite).send_keys(
                "TEST0001"
            )
            buscar_elemento(
                driver, By.XPATH, eue.textarea_descripcion_adicional
            ).send_keys("Expediente de prueba. Carece de motivacion administrativa.")
            buscar_elemento(driver, By.XPATH, eue.boton_caratular).click()
            t_ini = time.perf_counter()
            nro_exped = buscar_elemento(
                driver, By.CSS_SELECTOR, eue.span_nro_expediente
            ).text
            nro_exped = nro_exped.split()[4] + " " + nro_exped.split()[5]
            buscar_elemento(driver, By.CSS_SELECTOR, eue.boton_ok).click()
            t_fin = time.perf_counter()
            t_total = t_fin - t_ini
            t_totals = str("%.2f" % t_total)
            nodo = buscar_elemento(driver, By.CSS_SELECTOR, eue.nodo).text
            resultado = "NORMAL" if t_total < 5 else "DEGRADADO"
            break

        except:
            intentos += 1
            if intentos == 3:
                nro_exped = ""
                screenshot = f"./screenshots/error-caratular expediente {nodo}-{time.strftime('%Y-%m-%d-%H-%M-%S')}.png"
                driver.save_screenshot(screenshot)
                resultado = "ERROR"

        finally:
            driver.close()

    return "caratular_expediente", nodo, t_totals, resultado, nro_exped


def test_buscar_expediente(nro_exped):
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
            time.sleep(1)
            buscar_elemento(driver, By.CSS_SELECTOR, eue.input_busqueda).click()
            time.sleep(1)
            driver.switch_to.active_element.send_keys(nro_exped)
            time.sleep(1)
            buscar_elemento(driver, By.CSS_SELECTOR, eue.boton_buscar).click()
            t_ini = time.perf_counter()
            buscar_elemento(driver, By.CSS_SELECTOR, eue.expediente_encontrado)
            t_fin = time.perf_counter()
            t_total = t_fin - t_ini
            t_totals = str("%.2f" % t_total)
            nodo = buscar_elemento(driver, By.CSS_SELECTOR, eue.nodo).text
            resultado = "NORMAL" if t_total < 5 else "DEGRADADO"
            break

        except:
            intentos += 1
            if intentos == 3:
                screenshot = f"./screenshots/error-buscar expediente {nodo}-{time.strftime('%Y-%m-%d-%H-%M-%S')}.png"
                driver.save_screenshot(screenshot)
                resultado = "ERROR"

        finally:
            driver.close()

    return f"buscar_expediente", nodo, t_totals, resultado, nro_exped


def test_guarda_temporal():
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

            buscar_elemento(driver, By.XPATH, eue.boton_ejecutar).click()
            time.sleep(1)
            buscar_elemento(driver, By.CSS_SELECTOR, eue.boton_realizar_pase).click()
            time.sleep(1)
            driver.switch_to.frame(
                buscar_elemento(driver, By.XPATH, eue.iframe_ckeditor)
            )
            buscar_elemento(driver, By.CSS_SELECTOR, "body p").send_keys(
                "Expediente de prueba. Carece de motivacion administrativa."
            )
            driver.switch_to.default_content()

            buscar_elemento(driver, By.CSS_SELECTOR, eue.combobox_estado).send_keys("G")
            buscar_elemento(driver, By.XPATH, eue.boton_realizar_pase_2).click()
            buscar_elemento(driver, By.XPATH, eue.boton_si).click()
            nro_exped = buscar_elemento(
                driver, By.CSS_SELECTOR, eue.span_nro_expediente
            ).text
            nro_exped = (
                nro_exped.split()[2] + " " + nro_exped.split()[3].replace(",", "")
            )
            t_ini = time.perf_counter()
            buscar_elemento(
                driver,
                By.CSS_SELECTOR,
                ".z-messagebox-icon.z-messagebox-information.z-div",
            )
            nro_exped = buscar_elemento(
                driver, By.CSS_SELECTOR, eue.span_nro_expediente
            ).text
            nro_exped = (
                nro_exped.split()[2] + " " + nro_exped.split()[3].replace(",", "")
            )
            t_fin = time.perf_counter()
            buscar_elemento(driver, By.XPATH, eue.boton_ok_2).click()
            t_total = t_fin - t_ini
            t_totals = str("%.2f" % t_total)
            nodo = buscar_elemento(driver, By.CSS_SELECTOR, eue.nodo).text
            resultado = "NORMAL" if t_total < 5 else "DEGRADADO"
            break

        except:
            intentos += 1
            if intentos == 3:
                nro_exped = ""
                screenshot = f"./screenshots/error-guarda temporal {nodo}-{time.strftime('%Y-%m-%d-%H-%M-%S')}.png"
                driver.save_screenshot(screenshot)
                resultado = "ERROR"

        finally:
            driver.close()

    return "guarda_temporal", nodo, t_totals, resultado, nro_exped


def test_solicitud_caratulacion():
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

            buscar_elemento(driver, By.XPATH, eue.boton_crear_nueva_solicitud).click()
            time.sleep(1)
            buscar_elemento(
                driver, By.CSS_SELECTOR, eue.textarea_motivo_interno
            ).send_keys("Expediente de prueba. Carece de motivacion administrativa")
            buscar_elemento(
                driver, By.CSS_SELECTOR, eue.textarea_motivo_externo
            ).send_keys("Expediente de prueba. Carece de motivacion administrativa")
            buscar_elemento(driver, By.XPATH, eue.input_codigo_tramite).send_keys(
                "TEST0001"
            )
            time.sleep(1)
            buscar_elemento(driver, By.XPATH, eue.boton_solicitar_caratulacion).click()
            time.sleep(1)
            buscar_elemento(driver, By.CSS_SELECTOR, eue.checkbox_usuario).click()
            time.sleep(1)
            buscar_elemento(driver, By.CSS_SELECTOR, eue.input_usuario).send_keys(
                "Test Performance "
            )
            time.sleep(3)
            buscar_elemento(driver, By.XPATH, eue.boton_enviar_solicitud).click()

            t_ini = time.perf_counter()
            buscar_elemento(driver, By.XPATH, eue.boton_crear_nueva_solicitud)
            t_fin = time.perf_counter()
            t_total = t_fin - t_ini
            t_totals = str("%.2f" % t_total)
            nodo = buscar_elemento(driver, By.CSS_SELECTOR, eue.nodo).text
            resultado = "NORMAL" if t_total < 5 else "DEGRADADO"
            break

        except:
            intentos += 1
            if intentos == 3:
                screenshot = f"./screenshots/error-solicitud caratulacion {nodo}-{time.strftime('%Y-%m-%d-%H-%M-%S')}.png"
                driver.save_screenshot(screenshot)
                resultado = "ERROR"

        finally:
            driver.close()

    return "solicitud_caratulacion", nodo, t_totals, resultado


def test_pase_en_bloque():
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

            buscar_elemento(driver, By.XPATH, eue.boton_realizar_pase_3).click()
            time.sleep(1)
            buscar_elemento(driver, By.XPATH, eue.checkbox_pase_block_1).click()
            time.sleep(1)
            buscar_elemento(driver, By.XPATH, eue.boton_generar_pase_bloque).click()
            time.sleep(1)
            driver.switch_to.frame(
                buscar_elemento(driver, By.XPATH, eue.iframe_ckeditor)
            )
            buscar_elemento(driver, By.CSS_SELECTOR, "body p").send_keys(
                "Expediente de prueba. Carece de motivacion administrativa."
            )
            driver.switch_to.default_content()
            buscar_elemento(driver, By.CSS_SELECTOR, eue.combobox_estado).send_keys("G")
            buscar_elemento(driver, By.XPATH, eue.boton_realizar_pase_2).click()
            buscar_elemento(driver, By.XPATH, eue.boton_si).click()

            t_ini = time.perf_counter()
            buscar_elemento(driver, By.XPATH, eue.span_realizado).click()
            t_fin = time.perf_counter()
            t_total = t_fin - t_ini
            t_totals = str("%.2f" % t_total)
            nodo = buscar_elemento(driver, By.CSS_SELECTOR, eue.nodo).text
            resultado = "NORMAL" if t_total < 20 else "DEGRADADO"
            break

        except:
            intentos += 1
            if intentos == 3:
                screenshot = f"./screenshots/error-pase en bloque {nodo}-{time.strftime('%Y-%m-%d-%H-%M-%S')}.png"
                driver.save_screenshot(screenshot)
                resultado = "ERROR"

        finally:
            driver.close()

    return "pase_en_bloque", nodo, t_totals, resultado


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

    # Funcionalidad EE
    pbar.set_description("Test Caratular expediente")
    e = test_caratular_expediente()
    actualizar(result_dic_con, result_dic_log, e)
    pbar.update(1)
    pbar.set_description("Test Buscar expediente")
    actualizar(result_dic_con, result_dic_log, test_buscar_expediente(e[4]))
    pbar.update(1)
    pbar.set_description("Test Guarda temporal")
    actualizar(result_dic_con, result_dic_log, test_guarda_temporal())
    pbar.update(1)
    pbar.set_description("Test Solicitar caratulación")
    actualizar(result_dic_con, result_dic_log, test_solicitud_caratulacion())
    pbar.update(1)
    pbar.set_description("Test Pase en bloque")
    actualizar(result_dic_con, result_dic_log, test_pase_en_bloque())
    pbar.update(1)
    pbar.set_description("Finalizado")
    pbar.close()

    pdtabulate = lambda df: tabulate(
        df, headers="keys", tablefmt="pretty", showindex="never"
    )

    df_con = pd.DataFrame(result_dic_con)
    print(pdtabulate(df_con))
