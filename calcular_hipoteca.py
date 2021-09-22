'''
Calcula el total pagado de un préstamo.
@author: Mariana Blanco
'''

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0

# Estas dos variables son cantidad de meses
pago_extra_mes_comienzo = 61 
pago_extra_mes_fin = 108   

# Entre los meses comienzo y fin, realiza este pago extra
pago_extra = 1000

while saldo > 0:
    pago_mensual = 2684.11
    mes = mes + 1
    
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        pago_mensual += pago_extra
        
    if saldo > pago_mensual:
        saldo = saldo * (1+tasa/12) - pago_mensual
    else:
        saldo = round(saldo * (1+tasa/12), 2)
        pago_mensual = saldo
        saldo = saldo - pago_mensual
    
    total_pagado = total_pagado + pago_mensual
    f'Mes: {mes:3d} - Pago mensual: ${pago_mensual:07.2f} - Total pagado: ${total_pagado:09.2f} - Saldo: ${saldo:09.2f}'

f'El total pagado es de ${total_pagado:0.2f} en {mes} meses'
