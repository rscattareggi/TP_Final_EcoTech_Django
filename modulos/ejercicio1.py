def limpiar_registro_sensor(r):
 return {"sensor_id":str(r.get("sensor_id","")).strip(),"temperatura":float(str(r.get("temperatura","0")).replace("C","")),"ubicacion":r.get("ubicacion") or "Ubicación no informada"}
