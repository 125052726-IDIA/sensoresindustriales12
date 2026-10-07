# Informe de Arquitectura Big Data

## 1. Las 5 V del Proyecto
| Concepto | Definición en el Proyecto | Ejemplo | Estado |
| :--- | :--- | :--- | :--- |
| *Volumen* | Escala de datos acumulados. | 100,000 filas actuales. Proyección: Terabytes al añadir más plantas. | Presente / Futuro |
| *Velocidad* | Frecuencia de llegada de datos. | Actual: 1 lectura por minuto. Futuro: lecturas por segundo. | Presente / Futuro |
| *Variedad* | Tipos de formatos de datos. | Actual: Tablas CSV. Futuro: imágenes y texto de mantenimiento. | Presente / Futuro |
| *Veracidad* | Fiabilidad de la información. | Ruido o fallos en los sensores pueden sesgar los promedios. | Futuro |
| *Valor* | Utilidad para el negocio. | Identificar plantas con riesgo térmico para evitar paros. | Presente |

## 2. Clasificación de Datos y Big Data
- *CSV de sensores:* Datos estructurados (esquema tabular fijo).
- *Mensaje JSON:* Datos semiestructurados (etiquetas flexibles).
- *Fotografía:* Datos no estructurados (binario visual).
- *Reporte de texto:* Datos no estructurados (lenguaje natural).

*¿Por qué 100,000 registros no son Big Data?*
Porque el volumen es manejable en memoria RAM y herramientas tradicionales (Pandas/Excel) lo procesan en segundos. Al escalar (miles de sensores por segundo), aparecerán limitaciones de hardware (memoria, CPU) y la necesidad de procesamiento distribuido.

## 3. Procesamiento Batch vs Streaming
- *Análisis actual:* Procesamiento *Batch*, ya que se lee un archivo CSV estático y se procesa en bloque.
- *Alerta inmediata (>85°C):* Requiere *Streaming*, usando tecnologías como Apache Kafka o Spark Streaming para evaluar el dato al instante.
- *Resumen diario:* Requiere *Batch*, acumulando los datos del día para procesarlos en un solo lote al finalizar.

## 4. Arquitecturas Lambda y Kappa
- *Escenario A (Histórico + Tiempo Real):* Arquitectura *Lambda*. Combina una capa Batch (para recalcular históricos) y una capa Speed (para datos recientes), uniendo resultados en una capa de servicio.
- *Escenario B (Una sola lógica, reprocesable):* Arquitectura *Kappa*. Utiliza un único motor de streaming que lee de una cola de mensajes (ej. Kafka), permitiendo reprocesar desde el inicio si hay errores.

## 5. Analítica Descriptiva, Predictiva y Prescriptiva
- *Descriptiva:* [INSERTA AQUÍ TUS PROMEDIOS] y [INSERTA AQUÍ EL TOTAL DE ALERTAS]. (Ej: La planta A promedia 72°C y se detectaron 340 alertas).
- *Predictiva:* ¿Existe alta probabilidad de fallo en el sensor X? Se necesitan datos históricos de mantenimiento y correlación con picos de vibración.
- *Prescriptiva:* Programar mantenimiento preventivo urgente en la planta con más alertas. Se debe evaluar el costo de paro vs. costo de reparación.