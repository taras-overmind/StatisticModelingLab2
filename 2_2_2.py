import numpy as np
import matplotlib.pyplot as plt
events = 500
lambda_value = 3
inter_arrivals = np.random.exponential(1/lambda_value, events)
arrivals = np.cumsum(inter_arrivals)
plt.hist(arrivals, bins=10, density=True)
plt.xlabel('Час мiж послiдовними подiями')
plt.ylabel('Вiрогiднiсть')
plt.title('Гiстограма iнтервалiв мiж подiями')
plt.show()