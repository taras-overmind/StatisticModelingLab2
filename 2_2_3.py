import matplotlib.pyplot as plt
from scipy.stats import poisson
lambda_value = 3
T = 2
n = 5
M = 10000
# Створення 10000 реалiзацiй пуассонiвського процесу на момент часу 2
event_counts = poisson.rvs(mu=lambda_value * T, size=M)
# Створення гiстограми для кiлькостi реалiзацiй, де з'явилося рiвно п'ять подiй
plt.hist(event_counts, bins=range(max(event_counts)+1), align='left', alpha=0.75,
density=True)
plt.axvline(n, color='g', linewidth=1)
plt.text(n+0.2, plt.ylim()[1]*0.9, f'n={n}', color = 'green')
plt.xlabel('Кiлькiсть подiй')
plt.ylabel('Частота')
plt.title(f'Гiстограма появи рiвно {n} подiй')
plt.show()