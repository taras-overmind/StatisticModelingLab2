import numpy as np
import matplotlib.pyplot as plt
a = 0.3 # Заданий рiвень
T = 3 # Час
N = 500 # Кроки
# Реалiзацiя вiнерiвського процесу
def wiener_process(N, T, a):
    dt = T/N
    t = np.linspace(0, T, N+1)
    dW = np.random.normal(0, np.sqrt(dt), N)
    W = np.cumsum(dW)
    W = np.insert(W, 0, 0)
    exit = np.nan
    for i in range(1, len(W)):
        if W[i] >= a:
            exit = t[i]
            break
    return t, W, exit
# Отримання однiєї реалiзацiї вiнерiвського процесу
t, W, exit = wiener_process(N, T, a)
# Вiзуалiзацiя траєкторiї
plt.plot(t, W, label='w(t)')
plt.title(f'Вихiд вiнерiвського процесу за заданий рiвень a = {a}')
plt.xlabel('t')
plt.ylabel('w(t)')
# Позначення часу першого виходу за рiвень a
if not np.isnan(exit):
    plt.text(exit, a, f'({exit}, {a})', fontsize=13, verticalalignment='bottom')
    plt.axvline(x=exit, color='r', linestyle='--')
    plt.axhline(y=a, color='r', linestyle='--')
    plt.xlabel('Час')
plt.legend()
plt.show()