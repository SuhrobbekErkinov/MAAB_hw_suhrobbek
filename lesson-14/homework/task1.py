import numpy as np

def f_to_c(f):
    return (f - 32) * 5 / 9

if __name__ == "__main__":
    vectorized_conversion = np.vectorize(f_to_c)
    f_temps = np.array([47, 45, 65, 27, 38])
    c_temps = vectorized_conversion(f_temps)
    print(c_temps)