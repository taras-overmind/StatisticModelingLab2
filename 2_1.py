import numpy as np
import matplotlib.pyplot as plt
events = 500
lambda_value = 3
inter_arrivals = np.random.exponential(1/lambda_value, events)
arrivals = np.cumsum(inter_arrivals)
plt.step(arrivals, range(1, events + 1), where='post')
plt.xlabel('Час')
plt.ylabel('Кiлькiсть випадкових подiй')
plt.title('Демонстрацiя пуассонiвського процесу')
plt.show()