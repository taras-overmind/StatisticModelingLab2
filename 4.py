import numpy as np


class MarkovChain:
    def __init__(self, size):
        self.size = size
        # Генерацiя стохастичної матрицi переходiв
        self.transition_matrix = self.generate_stochastic_matrix(size)

    @staticmethod
    def generate_stochastic_matrix(size):
        # Створення матрицi iз випадковими значеннями
        matrix = np.random.rand(size, size)
        # Нормалiзацiя рядкiв матрицi
        matrix /= matrix.sum(axis=1)[:, None]
        return matrix

    def simulate_absorbing_chain(self, initial_state):
        state = initial_state
        steps = 0
        while True:
            steps += 1
            # Вибiр наступного стану
            state = np.random.choice(self.size, p=self.transition_matrix[state])
            # Перевiрка на досягнення поглинаючого стану
            if self.transition_matrix[state].sum() == 1:
                break
        return steps

    def theoretical_absorbing_chain(self):
        Q = self.transition_matrix[:-1, :-1]
        R = self.transition_matrix[:-1, -1]
        # Обчислення фундаментальної матрицi
        N = np.linalg.inv(np.eye(len(Q)) - Q)
        # Обчислення ймовiрностей поглинання
        B = N.dot(R)
        return N, B

    @staticmethod
    def calculate_state_durations(chains, size):
        durations = np.zeros((len(chains), size))

        for i, chain in enumerate(chains):
            for state in range(size):
                # Розрахунок тривалостi перебування в станах
                durations[i, state] = np.sum(np.array(chain) == state)
        return durations

    def find_stationary_distribution(self):
        # Знаходження власних значень i власних векторiв
        eigvals, eigvecs = np.linalg.eig(self.transition_matrix.T)
        # Визначення стацiонарного розподiлу
        stationary_distribution = np.abs(eigvecs[:, np.isclose(eigvals, 1)]).flatten()
        stationary_distribution /= stationary_distribution.sum()
        return stationary_distribution


# Приклад використання
size = 4
initial_state = 0
num_simulations = 200
chain_lengths = 10
# Створення ланцюга Маркова з одним поглинаючим станом
absorbing_markov_chain = MarkovChain(size)
# Встановлення останнього стану як поглинаючого
absorbing_markov_chain.transition_matrix[-1] = np.eye(1, size)[-1]
# Моделювання реалiзацiй поглинаючого ланцюга Маркова
absorption_times = [absorbing_markov_chain.simulate_absorbing_chain(initial_state)
                    for _ in range(num_simulations)]
# Розрахунок теоретичних характеристик
N, B = absorbing_markov_chain.theoretical_absorbing_chain()
# Розрахунок середнього часу до поглинання
average_absorption_time = np.mean(absorption_times)
# Створення регулярного ланцюга Маркова
regular_markov_chain = MarkovChain(size)

# Моделювання реалiзацiй регулярного ланцюга Маркова
regular_chains = [list(np.random.choice(size,
                                        chain_lengths, p=regular_markov_chain.transition_matrix[initial_state]))
                  for _ in range(num_simulations)]

# Розрахунок тривалостi перебування в станах
state_durations = MarkovChain.calculate_state_durations(regular_chains, size)

# Визначення теоретичного стацiонарного розподiлу
stationary_distribution = regular_markov_chain.find_stationary_distribution()

# Визначення експериментального стацiонарного розподiлу
total_state_time = np.sum(state_durations, axis=0)
experimental_stationary_distribution = total_state_time / np.sum(total_state_time)

# Вiдображення результатiв
print(f"Матриця перехiдних ймовiрностей для поглинаючого ланцюга Маркова:\n{absorbing_markov_chain.transition_matrix}")
print(f"Середнiй час до поглинання: {average_absorption_time}")
print(f"Фундаментальна матриця:\n{N}")
print(f"Теоретичнi ймовiрностi поглинання: {B}")
print(f"Матриця перехiдних ймовiрностей для регулярного ланцюга Маркова:\n{regular_markov_chain.transition_matrix}")
print(f"Теоретичний стацiонарний розподiл: {stationary_distribution}")
print(f"Експериментальний стацiонарний розподiл:{experimental_stationary_distribution}")
