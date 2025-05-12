
"""
Optimizador de Horario de Estudio con Programación Dinámica
-----------------------------------------------------------
Este script resuelve el problema de asignación óptima de horas de estudio a materias
para maximizar el rendimiento académico, basado en el clásico problema de la mochila (0/1 Knapsack).
"""

from typing import List, Tuple

def optimizar_estudio(horas_totales: int, materias: List[Tuple[str, int, int]]) -> Tuple[int, List[str], List[List[int]]]:
    """
    Parámetros:
        horas_totales (int): número total de horas disponibles
        materias (list): lista de tuplas (nombre, horas requeridas, valor académico)
    
    Retorna:
        beneficio_maximo (int): valor total alcanzado
        materias_seleccionadas (list): nombres de materias elegidas
        dp (list): tabla completa de programación dinámica
    """
    n = len(materias)
    dp = [[0] * (horas_totales + 1) for _ in range(n + 1)]

    # Llenar tabla DP
    for i in range(1, n + 1):
        nombre, horas_i, valor_i = materias[i - 1]
        for t in range(horas_totales + 1):
            if horas_i <= t:
                dp[i][t] = max(dp[i - 1][t], dp[i - 1][t - horas_i] + valor_i)
            else:
                dp[i][t] = dp[i - 1][t]

    # Recuperar las materias seleccionadas
    t = horas_totales
    seleccionadas = []
    for i in range(n, 0, -1):
        if dp[i][t] != dp[i - 1][t]:
            seleccionadas.append(materias[i - 1][0])
            t -= materias[i - 1][1]

    return dp[n][horas_totales], seleccionadas[::-1], dp

def imprimir_tabla_dp(dp: List[List[int]]):
    """Imprime la tabla de programación dinámica de forma clara"""
    print("\nTabla de Programación Dinámica (DP):")
    for fila in dp:
        print(fila)

def main():
    # Definimos materias como: (nombre, horas, valor)
    materias = [
        ("Matemáticas", 3, 8),
        ("Física", 2, 6),
        ("Química", 4, 9),
        ("Historia", 1, 3)
    ]
    horas_disponibles = 6

    print("\nHoras disponibles:", horas_disponibles)
    print("Materias disponibles:")
    for nombre, h, v in materias:
        print(f"- {nombre}: {h} h, valor {v}")

    beneficio, seleccionadas, dp = optimizar_estudio(horas_disponibles, materias)

    print("\nBeneficio académico máximo alcanzado:", beneficio)
    print("Materias seleccionadas:")
    for mat in seleccionadas:
        print(f"- {mat}")

    imprimir_tabla_dp(dp)

if __name__ == "__main__":
    main()
