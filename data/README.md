# Sistema de Monitoreo Predictivo para Sensores Industriales

## Propósito
Evaluar un conjunto de 100,000 lecturas simuladas provenientes de sensores en plantas industriales. El fin es detectar anomalías térmicas, calcular promedios y exportar reportes de alertas.

## Datos Utilizados
El archivo data/sensores_industriales.csv incluye las columnas:
- id_registro: Código único de la medición.
- fecha_hora: Marca temporal de la lectura.
- id_sensor: Identificador del dispositivo.
- planta: Ubicación de la planta.
- temperatura_c: Temperatura registrada en Celsius.
- vibracion_mm_s: Nivel de vibración en mm/s.

Los datos son simulados exclusivamente para fines académicos.

## Instalación y Uso
1. Clona el repositorio e ingresa a la carpeta:
   ```bash
   git clone <URL_DEL_REPO>
   cd sensoresindustriales12