ingresos_mensuales = 40000
gasto_mensual = 80000

if ingresos_mensuales >= 100000:
    if gasto_mensual - ingresos_mensuales < 1000:
        print("Hay que regular los gastos")
    else:
        print("estas bien") 
    print("Estas bien en cualquier parte del mundo")

elif ingresos_mensuales >= 10000:
    print("Estas bien en america latina")
elif ingresos_mensuales >= 1000:
    print("Estas bien en Argentina")
elif ingresos_mensuales >= 200:
    print("Estas bien en Venezuela")
    
else:
    print("Sos pobre en cualquier lado")