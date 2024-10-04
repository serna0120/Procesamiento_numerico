# Importar librerías
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_excel("datos.xlsx")
df.head(2)

# Seleccionar variables
variable_x = "tiempo"
variable_y = "temperatura"

# Crear características polinómicas (de segundo grado)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(df[[variable_x]])

# Ajustar el modelo polinomial
modelo_poly = LinearRegression()
modelo_poly.fit(X_poly, df[variable_y])

# Mostrar la ecuación del modelo polinomial
print(f"Ecuación del modelo polinomial: y = {round(modelo_poly.coef_[2], 3)}x^2 + {round(modelo_poly.coef_[1], 3)}x + {round(modelo_poly.intercept_, 3)}")

# Predecir los valores
y_pred_poly = modelo_poly.predict(X_poly)

# Calcular el error estimado
mse_poly = mean_squared_error(df[variable_y], y_pred_poly)
mae_poly = mean_absolute_error(df[variable_y], y_pred_poly)

# Mostrar coeficiente de determinación R^2
r2_poly = r2_score(df[variable_y], y_pred_poly)
print(f"Coeficiente de determinación (R^2) del modelo polinomial: {round(r2_poly, 3)}")

# Mostrar errores
print(f"Error cuadrático medio (MSE) del modelo polinomial: {round(mse_poly, 3)}")
print(f"Error absoluto medio (MAE) del modelo polinomial: {round(mae_poly, 3)}")

# Graficar datos y la curva de regresión polinomial
plt.scatter(df[variable_x], df[variable_y], color='black')  # puntos originales
plt.plot(df[variable_x], y_pred_poly, color='red')  # curva ajustada
plt.title('Regresión Polinomial de Segundo Grado')
plt.xlabel(variable_x)
plt.ylabel(variable_y)
plt.show()
