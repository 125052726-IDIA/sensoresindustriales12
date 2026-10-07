import pandas as pd
import os

# Carga de datos
ruta_datos = os.path.join('data', 'sensores_industriales.csv')
datos = pd.read_csv(ruta_datos)
datos['fecha_hora'] = pd.to_datetime(datos['fecha_hora'])

print(" REPORTE DE MONITOREO INDUSTRIAL \n")

# 1. Totales
cant_registros = len(datos)
cant_sensores = datos['id_sensor'].nunique()
print(f"1. Registros totales: {cant_registros} | Sensores únicos: {cant_sensores}")

# 2. Promedio por planta
print("\n2. Temperatura media por planta:")
print(datos.groupby('planta')['temperatura_c'].mean())

# 3. Máximo absoluto y empates
temp_max = datos['temperatura_c'].max()
registros_max = datos[datos['temperatura_c'] == temp_max]
print(f"\n3. Temperatura más alta: {temp_max} °C")
print("   Detalles de los registros con este valor:")
for idx, fila in registros_max.iterrows():
    print(f"   - Sensor: {fila['id_sensor']} | Fecha: {fila['fecha_hora']} | Planta: {fila['planta']}")

# 4. Conteo de alertas (>85 °C)
limite = 85
alertas = datos[datos['temperatura_c'] > limite]
total_alertas = len(alertas)
print(f"\n4. Lecturas que superan los {limite} °C: {total_alertas}")

# 5. Planta con más alertas
if total_alertas > 0:
    conteo_alertas = alertas.groupby('planta').size()
    max_alertas = conteo_alertas.max()
    plantas_criticas = conteo_alertas[conteo_alertas == max_alertas]
    print(f"\n5. Planta(s) con mayor cantidad de alertas ({max_alertas}):")
    for planta, cant in plantas_criticas.items():
        print(f"   - {planta}")
else:
    print("\n5. No se registraron alertas.")

# 6. Exportar alertas
if not os.path.exists('resultados'):
    os.makedirs('resultados')
alertas.to_csv('resultados/alertas.csv', index=False)
print("\n6. Alertas exportadas a resultados/alertas.csv")