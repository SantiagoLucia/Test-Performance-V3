from ingreso_modulos import *
from funcionalidad_ccoo import *
from funcionalidad_ee import *
from funcionalidad_gedo import *
import pandas as pd
from tabulate import tabulate
from utils.actualizar_dic import actualizar
from datetime import datetime
from tqdm import tqdm
import os

if __name__ == '__main__':
    tiempo = datetime.now()
    fecha = tiempo.strftime("%d/%m/%Y")
    hora = tiempo.strftime("%H:%M:%S")
    salida = f'./logs/test_performance_{tiempo.strftime("%Y-%m-%d-%H-%M-%S")}.log'
    result_dic_con = {'TEST': [], 'NODO': [], 'TIEMPO (seg)': [], 'RESULTADO': [], 'NRO GDEBA': []}
    result_dic_log = {'TEST': [], 'NODO': [], 'TIEMPO (seg)': [], 'RESULTADO': [], 'NRO GDEBA': []}
    pbar = tqdm(total=17, ncols=90, colour='green', bar_format = "{l_bar}{bar}| {n_fmt}/{total_fmt}")

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
    
    # Funcionalidad GEDO
    pbar.set_description("Test Firmar gedo (TESTL)")
    d = test_firmar_gedo('TESTL')
    actualizar(result_dic_con, result_dic_log, d)
    pbar.update(1)
    pbar.set_description("Test Firmar gedo (TESTT)")
    actualizar(result_dic_con, result_dic_log, test_firmar_gedo('TESTT'))
    pbar.update(1)
    pbar.set_description("Test Firmar gedo (TESTI)")
    actualizar(result_dic_con, result_dic_log, test_firmar_gedo('TESTI'))
    pbar.update(1)
    pbar.set_description("Test Firmar portafirma")
    actualizar(result_dic_con, result_dic_log, test_firmar_portafirma())
    pbar.update(1)
    pbar.set_description("Test Buscar Documento")
    actualizar(result_dic_con, result_dic_log, test_buscar_documento(d[4]))
    pbar.update(1)

    # Funcionalidad CCOO
    pbar.set_description("Test Firmar ccoo (NOTA)")
    actualizar(result_dic_con, result_dic_log, test_firmar_ccoo('NOTA'))
    pbar.update(1)
    pbar.set_description("Test Firmar ccoo (MEMO)")
    actualizar(result_dic_con, result_dic_log, test_firmar_ccoo('MEMO'))    
    pbar.update(1)

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
    pbar.set_description("Finalizado")
    pbar.close()
    
    pdtabulate=lambda df:tabulate(df,headers='keys',tablefmt='pretty', showindex="never")
    
    df_con = pd.DataFrame(result_dic_con)
    print(pdtabulate(df_con))

    df_log = pd.DataFrame(result_dic_log)
    with open(salida, 'w') as f:
        f.write("TEST DE PERFORMANCE\n")
        f.write("====================\n")
        f.write("AMBIENTE: PRODUCCION\n")
        f.write(f"FECHA:    {fecha}\n")
        f.write(f"HORA:     {hora}\n")
        f.write("\n")
        f.write(pdtabulate(df_log))
    
    path=os.path.realpath(salida)
    os.startfile(path)
    input('---Finalizado---')