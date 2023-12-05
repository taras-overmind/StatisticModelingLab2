import numpy as np
import matplotlib.pyplot as plt
# Параметри
M = 10000 # Реалiзацiї
N = 500 # Кроки
T = 3.0 # Час
dt = T / N # Крок у часi
level = 0.5 # Заданий рiвень
# Моделювання вiнерiвського процесу
def model_wiener_process(m, n, dt):
    # Реалiзацiї
    w = np.zeros((m, n+1))
    # Симуляцiя
    for i in range(1, n+1):
         w[:, i] = w[:, i-1] + np.sqrt(dt) * np.random.randn(m)
    return w
# Симуляцiя вiнерiвського процесу
wiener_process = model_wiener_process(M, N, dt)
mean = np.mean(wiener_process[:, -1]) # Середнє значення
print(f"Середнє значення: {mean}")
means = np.mean(wiener_process, axis=0) # Середнi значення у рiзнi моменти часу
# Створення графiка середнiх значень вiнерiвського процесу у рiзнi моменти часу
plt.figure(figsize=(14, 7))
plt.plot(np.linspace(0, T, N+1), means)
plt.title("Графiк середнiх значень вiнерiвського процесу у рiзнi моменти часу")
plt.xlabel("Час")
plt.ylabel("Середнє значення")
plt.legend()
plt.show()
variance = np.var(wiener_process[:, -1]) # Дисперсiя
print(f"Дисперсiя: {variance}")
variances = np.var(wiener_process,
axis=0) # Дисперсiї вiнерiвського процесу у рiзнi моменти часу
# Створення графiка дисперсiй вiнерiвського процесу у рiзнi моменти часу
plt.figure(figsize=(14, 7))
plt.plot(np.linspace(0, T, N+1), variances, color='green')
plt.title("Графiк дисперсiй вiнерiвського процесу у рiзнi моменти часу")
plt.xlabel("Час")
plt.ylabel("Дисперсiя")
plt.legend()
plt.show()