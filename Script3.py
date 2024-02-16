import numpy as np
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt

# Definimos la función de la Ley de Amdahl (Para cálcular el SpeedUp)
def amdahl_speedup(P, S):
    return 1 / ((1 - P) + (P / S))

# Definimos el rango de valores para P y S
P_values = np.linspace(0, 1, 100)  # Fracción de cálculo paralelizable
S_values = [2, 4, 8]  # Aceleración de velocidad de la parte paralelizable

# Graficamos la Ley de Amdahl para diferentes valores de S
plt.figure(figsize=(10, 6))
for S in S_values:
    speedup_values = amdahl_speedup(P_values, S)
    plt.plot(P_values, speedup_values, label=f'S={S}')

# Configuraciones de la gráfica
plt.title('Ley de Amdahl')
plt.xlabel('Fracción del cálculo paralelizable (P)')
plt.ylabel('Speedup')
plt.legend()
plt.grid(True)
plt.show()