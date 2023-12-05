import numpy as np
import matplotlib.pyplot as plt
events = 500
lambda_value = 3
inter_arrivals = np.random.exponential(1/lambda_value, events)
arrivals = np.cumsum(inter_arrivals)
n = 30
plt.hist(arrivals[:n], bins=n, density=True)
plt.xlabel(f'Час появи {n}-ої подiї')
plt.ylabel('Вiрогiднiсть')
plt.title(f'Гiстограма часу появи {n}-ої подiї')
plt.show()