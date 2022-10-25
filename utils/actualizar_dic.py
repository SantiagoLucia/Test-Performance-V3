from colorama import Fore, Back, Style, init

init(autoreset=True)

def actualizar(dic_con, dic_log, test):
    dic_con['TEST'].append(test[0])
    dic_log['TEST'].append(test[0])
    
    dic_con['NODO'].append(test[1])
    dic_log['NODO'].append(test[1])
    
    dic_con['TIEMPO (seg)'].append(test[2])
    dic_log['TIEMPO (seg)'].append(test[2])
    
    if test[3] == 'NORMAL':
        dic_con['RESULTADO'].append(Fore.GREEN+test[3]+Style.RESET_ALL)
        dic_log['RESULTADO'].append(test[3])

    if test[3] == 'DEGRADADO':
        dic_con['RESULTADO'].append(Fore.YELLOW+test[3]+Style.RESET_ALL)
        dic_log['RESULTADO'].append(test[3])

    if test[3] == 'ERROR':
        dic_con['RESULTADO'].append(Fore.RED+test[3]+Style.RESET_ALL)
        dic_log['RESULTADO'].append(test[3])

    if len(test) == 5:
        dic_con['NRO GDEBA'].append(test[4])
        dic_log['NRO GDEBA'].append(test[4])
    else:
        dic_con['NRO GDEBA'].append('')
        dic_log['NRO GDEBA'].append('') 