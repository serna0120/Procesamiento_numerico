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
    
    # Verificar si hay valores NaN o datos no numéricos
    if np.any(np.isnan(x)) or np.any(np.isnan(y)):
        print("Advertencia: Hay valores NaN en los datos.")
    
    return x, y

# Función para calcular la interpolación de Lagrange para un grado dado
def interpolar_lagrange(x, y, grado):
    if len(x) <= grado:
        raise ValueError(f"Se necesitan al menos {grado+1} puntos para una interpolación de grado {grado}.")
    
    polinomio = lagrange(x[:grado+1], y[:grado+1])
    return polinomio

# Función para calcular el error verdadero y el error relativo
def calcular_errores(valor_real, valor_interpolado):
    error_verdadero = abs(valor_real - valor_interpolado)
    
    # Evitar división por cero en el cálculo del error relativo
    if valor_real != 0:
        error_relativo = abs(error_verdadero / valor_real) * 100
    else:
        error_relativo = np.nan  # O puedes asignar 0 si prefieres

    return error_verdadero, error_relativo

# Función principal para realizar las interpolaciones y calcular errores
def calcular_interpolaciones(file_path):
    x, y = cargar_datos_excel(file_path)
    
    # Asegurarse de que no haya duplicados en X
    if len(set(x)) != len(x):
        print("Advertencia: Hay valores duplicados en X, lo cual puede causar errores en la interpolación.")
    
    grados = [1, 2, 3, 4]
    resultados = []
    
    for grado in grados:
        try:
            polinomio = interpolar_lagrange(x, y, grado)
            valor_real = y[grado]  # Supongamos que el valor real es el último punto de los usados en la interpolación
            valor_interpolado = polinomio(x[grado])  # Evaluar el polinomio en el punto x[grado]
            
            # Imprimir para depuración
            print(f"Grado: {grado}, Valor Real: {valor_real}, Valor Interpolado: {valor_interpolado}")
            
            error_verdadero, error_relativo = calcular_errores(valor_real, valor_interpolado)
            
            resultados.append({
                'Grado': grado,
                'Polinomio': polinomio,
                'Valor Real': valor_real,
                'Valor Interpolado': valor_interpolado,
                'Error Verdadero': error_verdadero,
                'Error Relativo (%)': error_relativo
            })
        except Exception as e:
            print(f"Error en la interpolación de grado {grado}: {e}")
    
    return pd.DataFrame(resultados)

# Ejemplo de uso
file_path = "datos.xlsx"  # Archivo de Excel con los datos
resultados = calcular_interpolaciones(file_path)
print(resultados)
