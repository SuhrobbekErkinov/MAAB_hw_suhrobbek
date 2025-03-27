import numpy as np

def power_of(base, exponent):
    return base ** exponent

if __name__ == "__main__":
    vectorized_power = np.vectorize(power_of)
    bases = np.array([2, 3, 4, 5])
    exponents = np.array([1, 2, 3, 4])
    results = vectorized_power(bases, exponents)

    print(results)