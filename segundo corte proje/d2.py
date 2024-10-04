# Interpolacion de Lagrange con cálculo de error
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INGRESO , Datos de prueba
xi =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
          21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 
          39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 
          57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 
          75, 76, 77, 78, 79, 80]
fi = [90, 83.3, 78.9, 75.5, 71.9, 69.5, 66.9, 65.1, 63.3, 61.5, 60.1, 
               58.6, 57.3, 56, 55, 53.9, 52.8, 52, 51.1, 50.3, 49.5, 48.8, 48, 
               47.5, 46.8, 46.3, 45.8, 45.1, 44.8, 44.2, 43.8, 43.3, 42.8, 42.4, 
               42.1, 41.6, 41.3, 40.9, 40.6, 40.2, 39.9, 39.6, 39.3, 39.1, 38.8, 
               38.5, 38.3, 38.1, 37.8, 37.6, 37.4, 37.1, 37, 36.8, 36.6, 36.4, 
               36.2, 36, 35.8, 35.6, 35.5, 35.4, 35.2, 35, 34.9, 34.8, 34.6, 
               34.5, 34.3, 34.3, 34.1, 34, 33.9, 33.8, 33.6, 33.5, 33.5, 33.3, 
               33.2, 33.1, 32.9]

# PROCEDIMIENTO
xi = np.array(xi,dtype=float)
fi = np.array(fi,dtype=float)

# Polinomio de Lagrange
n = len(xi)
x = sym.Symbol('x')
polinomio = 0
divisorL = np.zeros(n, dtype = float)

for i in range(0,n,1):
    
    # Termino de Lagrange
    numerador = 1
    denominador = 1
    for j  in range(0,n,1):
        if (j!=i):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
    terminoLi = numerador/denominador

    polinomio = polinomio + terminoLi*fi[i]
    divisorL[i] = denominador

# simplifica el polinomio
polisimple = polinomio.expand()

# para evaluación numérica
px = sym.lambdify(x, polisimple)

# Cálculo de los valores interpolados y del error
valores_interpolados = px(xi)
errores_relativos = np.abs((fi - valores_interpolados) / fi) * 100

# Puntos para la gráfica
muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a, b, muestras)
pfi = px(pxi)

# SALIDA
print('    valores de fi: ', fi)
print('divisores en L(i): ', divisorL)
print()
print('Polinomio de Lagrange, expresiones')
print(polinomio)
print()
print('Polinomio de Lagrange: ')
print(polisimple)
print()
print('Valores interpolados: ', valores_interpolados)
print('Errores relativos porcentuales: ', errores_relativos)

# Gráfica
plt.plot(xi, fi, 'o', label = 'Puntos')
plt.plot(pxi, pfi, label = 'Polinomio')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Interpolación Lagrange')
plt.show()

# Gráfica de errores
plt.plot(xi, errores_relativos, 'r-o', label = 'Error Relativo (%)')
plt.legend()
plt.xlabel('xi')
plt.ylabel('Error relativo (%)')
plt.title('Error Relativo Porcentual')
plt.show()
