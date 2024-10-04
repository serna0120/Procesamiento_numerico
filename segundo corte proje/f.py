import pandas as pd
import numpy as np
from scipy.interpolate import lagrange

# Función para cargar los datos desde un archivo de Excel
def cargar_datos_excel(file_path):
    df = pd.read_excel(file_path, usecols=[1, 3])  # Cargar las columnas B (índice 1) y D (índice 3)
    print("Datos cargados desde el archivo Excel:")
    print(df)  # Imprimir los datos cargados para verificar
    x = df.iloc[:, 0].values  # Columna B (Tiempo)
    y = df.iloc[:, 1].values  # Columna D (Temperatura)
    print("Valores de X (Tiempo):", x)  # Imprimir los valores de X
    print("Valores de Y (Temperatura):", y)  # Imprimir los valores de Y
    
    return x, y

# Función para calcular la interpolación de Lagrange para un conjunto de puntos dados
def interpolar_lagrange(x, y, indices):
    if len(indices) < 2:
        raise ValueError("Se necesitan al menos 2 puntos para una interpolación.")
    
    polinomio = lagrange(x[indices], y[indices])  # Usar los índices proporcionados
    return polinomio

# Función principal para realizar la interpolación y calcular el valor interpolado
def calcular_y18_interpolacion(file_path):
    x, y = cargar_datos_excel(file_path)

    # Usar y16, y17 y y19 para la interpolación
    indices_y16_y17_y19 = [15, 16, 18]  # Índices para y16 (y[15]), y17 (y[16]), y19 (y[18])
    x18_index = 17  # Índice para x18 (asumiendo que x[17] es el punto donde queremos interpolar)

    try:
        # Interpolamos usando los puntos especificados
        polinomio = interpolar_lagrange(x, y, indices_y16_y17_y19)

        # Evaluar el polinomio en el punto x18
        y18_interpolado = polinomio(x[x18_index])  # Evaluar en x18
        
        # Mostrar resultados
        print(f"Interpolación usando y16, y17 y y19:")
        print(f"y18_interpolación: {y18_interpolado}")

    except Exception as e:
        print(f"Error en la interpolación: {e}")

# Ejemplo de uso
file_path = "datos.xlsx"  # Archivo de Excel con los datos
calcular_y18_interpolacion(file_path)
