# Optimización del Horario de Estudio con Programación Dinámica 📚🧠

Este proyecto presenta una solución algorítmica al problema de cómo distribuir de manera óptima el tiempo de estudio para maximizar el rendimiento académico durante una semana de exámenes.

Se utiliza el enfoque de **programación dinámica** para resolver una versión adaptada del clásico problema de la **mochila 0/1**, aplicándolo a un caso del mundo real en el entorno universitario.

## 📌 Descripción del problema
Dado un conjunto de materias, cada una con un número de horas necesarias para estudiarla y un valor estimado en cuanto al impacto en la calificación, se busca seleccionar las materias que maximicen el rendimiento sin superar un número total de horas disponibles (por ejemplo, 6 horas en un día).

## 📁 Contenido del repositorio

- `propuesta/`: Documento PDF con la formulación teórica del problema y su análisis completo.
- `codigo/`: Implementación en Python con comentarios explicativos y ejemplo funcional.
- `video/`: Guion listo para grabar un video explicando el código paso a paso.

## 🧠 Algoritmo
El algoritmo usa una tabla de programación dinámica `dp[i][t]` donde:
- `i` representa la cantidad de materias consideradas
- `t` representa las horas disponibles
La solución recorre la tabla para encontrar la combinación óptima de materias y luego recupera la selección final.

## 🧮 Complejidad
- Tiempo: `O(n·T)`
- Espacio: `O(n·T)`

## 🎥 Video
Se acompaña un guion para grabar la explicación detallada de cada parte del código, ideal para presentación académica.

## 🚀 Autor
Julio Alberto Bonilla Romero – Mayo 2025
