import numpy as np
import matplotlib.pyplot as plt
# Параметри
a = 0.3 # Заданий рiвень
M = 10000 # Реалiзацiї
T = 3 # Час
N = 500 # Кроки
# Модифiкована реалiзацiя вiнерiвського процесу
def wiener_process_exit(a, T, N):
    dt = T / N
    t = np.linspace(0, T, N + 1)
    w = np.zeros(N + 1)
    for i in range(1, N + 1):
        w[i] = w[i - 1] + np.sqrt(dt) * np.random.randn()
        if w[i] >= a:
            return t[i]
    return np.nan
# Масив часових значень першого виходу за рiвень 0,3 для кожної реалiзацiї вiнерiвського процесу
exits = np.array([wiener_process_exit(a, T, N) for _ in range(M)])
exits = exits[~np.isnan(exits)]
# Вiзуалiзацiя результатiв
plt.hist(exits, bins=10, density=True)
plt.xlabel(f'Час першого виходу за рiвень {a}')
plt.ylabel('Щiльнiсть вiрогiдностi')
plt.title(f'Емпiричний закон розподiлу часу першого виходу за рiвень {a}')
plt.show()