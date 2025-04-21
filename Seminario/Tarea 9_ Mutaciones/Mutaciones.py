# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 19:32:41 2025

@author: SANTIAGO
"""

referencia = "ATGCTAGCTAAT"

def detectar_mutaciones(ref, muestra):
    mutaciones = []
    if len(ref) != len(muestra):
        return {"error": "Las secuencias tienen longitudes diferentes"}
    
    for i, (r, m) in enumerate(zip(ref, muestra)):
        if m not in "ATCG":
            mutaciones.append({"posicion": i+1, "error": f"Base inválida: '{m}'"})
        elif r != m:
            mutaciones.append({"posicion": i+1, "base_referencia": r, "base_mutada": m})
    
    return mutaciones


def leer_secuencias(archivo):
    with open(archivo, 'r') as file:
        return [linea.strip().upper() for linea in file]


secuencias_sensor = leer_secuencias("sensor_data.txt")  


for idx, secuencia in enumerate(secuencias_sensor):
    print(f"\nAnalizando Secuencia {idx+1}: {secuencia}")
    resultado = detectar_mutaciones(referencia, secuencia)
    
    if isinstance(resultado, dict) and "error" in resultado:
        print(f"Error: {resultado['error']}")
    else:
        for mut in resultado:
            if "error" in mut:
                print(f"Posición {mut['posicion']}: {mut['error']}")
            else:
                print(f"Mutación en {mut['posicion']}: {mut['base_referencia']} -> {mut['base_mutada']}")