import numpy as np

def func(x):
    return -0.2 + x[0]**2 + x[1]**2 - (np.cos(6*np.pi*x[0]) + np.cos(6*np.pi*x[1]))/10

def hill_climbing(func, x_init, step_size=0.01, max_iter=1000):
    x = x_init
    for _ in range(max_iter):
        grad = np.gradient(x)
        x_next = x + step_size * grad
        if func(x_next) <= func(x):
            break
        x = x_next
    return x

x_init = np.array([0.0, 0.0])
x_max = hill_climbing(func, x_init)
y_max = func(x_max)

print(f"Giá trị cực đại của hàm số là {y_max} tại điểm {x_max}")
