from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Cargar datos
df = pd.read_excel("datos.xlsx")

# Seleccionar variables
variable_x = "tiempo"  # Tiempo en minutos o segundos
variable_y = "temperatura"  # Temperatura del agua en grados C

# Función de enfriamiento de Newton
def enfriamiento_newton(t, T_0, T_amb, k):
    return T_amb + (T_0 - T_amb) * np.exp(-k * t)

# Parámetros iniciales
T_0 = 90  # Temperatura inicial (en grados C)
T_amb = 32.8  # Temperatura ambiente (en grados C)

# Ajustar k usando curve_fit
popt, pcov = curve_fit(lambda t, k: enfriamiento_newton(t, T_0, T_amb, k), df[variable_x], df[variable_y])

# Valor óptimo de k
k_opt = popt[0]
print(f"Valor ajustado de k: {k_opt}")

# Generar la curva ajustada con el valor óptimo de k
t_vals = np.linspace(df[variable_x].min(), df[variable_x].max(), 100)
temp_enfriamiento = enfriamiento_newton(t_vals, T_0, T_amb, k_opt)

# Predecir las temperaturas con el valor ajustado de k
temp_pred = enfriamiento_newton(df[variable_x], T_0, T_amb, k_opt)

# Calcular el error estimado
mse = mean_squared_error(df[variable_y], temp_pred)
mae = mean_absolute_error(df[variable_y], temp_pred)

# Mostrar los errores
print(f"Error cuadrático medio (MSE): {round(mse, 3)}")
print(f"Error absoluto medio (MAE): {round(mae, 3)}")

# Graficar datos originales y la curva ajustada
plt.scatter(df[variable_x], df[variable_y], color='black', label='Datos experimentales')
plt.plot(t_vals, temp_enfriamiento, color='blue', linestyle='--', label=f'Enfriamiento de Newton (k={round(k_opt, 4)})')
plt.title('Ajuste de Enfriamiento de Newton')
plt.xlabel(variable_x)
plt.ylabel(variable_y)
plt.legend()
plt.show()
