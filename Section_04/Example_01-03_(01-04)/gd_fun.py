import numpy as np

def gradient_descent(
    derivative_fun,
    initial_guess,
    multiplier=0.01,
    precision=0.0001,
    max_iter=500
):
    x = initial_guess

    x_list = [x]

    for n in range(1, max_iter):
        x = x - multiplier * derivative_fun(x)
        x_list.append(x)
        if abs(x-x_list[-2]) < precision:
            break

    print(f"Local minimum:\t{x}")
    print(f"Number Steps:\t{len(x_list)}")
    print(f"Slope at x:\t{derivative_fun(x)}")
    # print(f"g(x) cost at x:\t{g(x)}")

    x_list = np.array(x_list)
    return x, x_list, derivative_fun(x_list)