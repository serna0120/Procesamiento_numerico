# Importar librerías
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt 

# Cargar datos
df = pd.read_excel("datos.xlsx")
df.head(2)

# Seleccionar variables
variable_x = "tiempo"
variable_y = "temperatura"

# Generar análisis
modelo = LinearRegression() 
modelo.fit(df[[variable_x]], df[variable_y]) 

# Predicciones
predicciones = modelo.predict(df[[variable_x]])

# Calcular el error estimado
mse = mean_squared_error(df[variable_y], predicciones)
mae = mean_absolute_error(df[variable_y], predicciones)

# Imprimir resultados
print('Ecuación de la recta: y = ', round(modelo.coef_[0],3), 'x + ', round(modelo.intercept_,3))  # Ecuación de la recta
print('Coeficiente de correlación: ', round(np.corrcoef(df[variable_x], df[variable_y])[0,1], 3))  # Coeficiente de correlación
print('Coeficiente de determinación (R^2): ', round(r2_score(df[variable_y], predicciones), 3))  # Coeficiente de determinación
print('Error cuadrático medio (MSE): ', round(mse, 3))  # Error cuadrático medio
print('Error absoluto medio (MAE): ', round(mae, 3))  # Error absoluto medio

# Gráfica con intervalo de confianza
sns.regplot(x=df[variable_x], y=df[variable_y], ci=95, line_kws={"color": "red"}, scatter_kws={"color": "black"})
plt.title('Regresión lineal') 
plt.show()
