import numpy as np
import matplotlib.pyplot as plt

# Параметри
M = 10000  # Реалiзацiї
N = 500  # Кроки
T = 3.0  # Час
dt = T / N  # Крок у часi
level = 0.5  # Заданий рiвень


# Моделювання вiнерiвського процесу
def model_wiener_process(m, n, dt):
    # Реалiзацiї
    w = np.zeros((m, n + 1))
    # Симуляцiя
    for i in range(1, n + 1):
        w[:, i] = w[:, i - 1] + np.sqrt(dt) * np.random.randn(m)
    return w
# Симуляцiя вiнерiвського процесу
wiener_process = model_wiener_process(M, N, dt)
# Вiзуалiзацiя трьох траєкторiй
for i in range(3):
    plt.plot(np.linspace(0, T, N + 1), wiener_process[i])
plt.xlabel('Час')
plt.ylabel('w(t)')
plt.title('Вiзуалiзованi траєкторiї')
plt.legend()
plt.show()
