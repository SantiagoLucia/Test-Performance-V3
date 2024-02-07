from utils.crear_sesion import crear_sesion
from utils.buscar_elemento import buscar_elemento
from webelements import cas, euc
from selenium.webdriver.common.by import By
import time
import pandas as pd
from tabulate import tabulate
from utils.actualizar_dic import actualizar
from tqdm import tqdm
from config import USER, PASSW


def test_firmar_ccoo(acronimo):
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

            buscar_elemento(driver, By.XPATH, euc.boton_inicio_documento).click()
            buscar_elemento(driver, By.CSS_SELECTOR, euc.input_acronimo).send_keys(
                acronimo
            )
            buscar_elemento(
                driver, By.CSS_SELECTOR, euc.boton_producir_yo_mismo
            ).click()
            buscar_elemento(driver, By.XPATH, euc.input_motivo).send_keys(
                "Documento de prueba. Carece de motivacion administrativa"
            )
            time.sleep(5)
            driver.switch_to.frame(1)
            # Escribo en el body
            editor_body = driver.find_element(By.XPATH, "//body")
            editor_body.send_keys(
                "Documento de prueba. Carece de motivacion administrativa."
            )
            # Salgo del ckeditor
            driver.switch_to.default_content()
            buscar_elemento(driver, By.XPATH, euc.boton_destinatarios).click()
            buscar_elemento(driver, By.XPATH, euc.input_destinatario).send_keys(USER)
            buscar_elemento(driver, By.XPATH, euc.boton_cargar).click()
            buscar_elemento(driver, By.XPATH, euc.boton_aceptar).click()
            time.sleep(1)
            buscar_elemento(driver, By.XPATH, euc.boton_firmar_yo_mismo).click()
            buscar_elemento(driver, By.XPATH, euc.boton_firmar_con_certificado).click()
            t_ini = time.perf_counter()
            nro_gedo = buscar_elemento(
                driver, By.XPATH, euc.span_nro_gedo
            ).text.split()[14]
            t_fin = time.perf_counter()
            t_total = t_fin - t_ini
            t_totals = str("%.2f" % t_total)
            nodo = buscar_elemento(driver, By.CSS_SELECTOR, euc.nodo).text
            resultado = "NORMAL" if t_total < 5 else "DEGRADADO"
            break

        except:
            intentos += 1
            if intentos == 3:
                nro_gedo = ""
                screenshot = f"./screenshots/error-firmar ccoo {nodo}-{time.strftime('%Y-%m-%d-%H-%M-%S')}.png"
                driver.save_screenshot(screenshot)
                resultado = "ERROR"

        finally:
            driver.close()

    return f"firmar_ccoo ({acronimo})", nodo, t_totals, resultado, nro_gedo


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
        total=2,
        ncols=90,
        colour="green",
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}",
    )

    # Funcionalidad CCOO
    pbar.set_description("Test Firmar ccoo (NOTA)")
    actualizar(result_dic_con, result_dic_log, test_firmar_ccoo("NOTA"))
    pbar.update(1)
    pbar.set_description("Test Firmar ccoo (MEMO)")
    actualizar(result_dic_con, result_dic_log, test_firmar_ccoo("MEMO"))
    pbar.update(1)
    pbar.set_description("Finalizado")
    pbar.close()

    pdtabulate = lambda df: tabulate(
        df, headers="keys", tablefmt="pretty", showindex="never"
    )

    df_con = pd.DataFrame(result_dic_con)
    print(pdtabulate(df_con))
