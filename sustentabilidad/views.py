from django.shortcuts import render

def calcular_emisiones_carbono(consumo_kwh,factor_emision=0.4):
 if consumo_kwh<0: raise ValueError()
 return consumo_kwh*factor_emision

def obtener_metricas_consumo(registros):
 emisiones=sum(calcular_emisiones_carbono(x["consumo_kwh"]) for x in registros)
 mayor=max(registros,key=lambda x:x["consumo_kwh"])
 return {"emisiones_totales":emisiones,"planta_mayor_consumo":mayor}

def vista_panel_sustentabilidad(request):
 datos=[{"planta":"Norte","consumo_kwh":1200},{"planta":"Sur","consumo_kwh":1500}]
 return render(request,"sustentabilidad/panel.html",obtener_metricas_consumo(datos))
