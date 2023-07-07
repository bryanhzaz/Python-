import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("PRUEBA.csv")
print(df.info())
media = df["Bill Cost"].mean()
#print(media)
suma = df["Bill Cost"].sum()
#print(suma)

estadísticas = df["Bill Cost"].describe()
#print(estadísticas)

plt.scatter(df["Agent"], df["Bill Cost"])
plt.show()

#plt.plot( df["Bill Cost"], df["Agent"])
#GRAFICAS = pd.plotting.scatter_matrix(df["Agent"], df["Bill Cost"])
#plt.show()