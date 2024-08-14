def sqrt_newton(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if x == 0:
        return 0
    guess = x
    epsilon = 0.00001
    while abs(guess * guess - x) > epsilon:
        guess = (guess + x / guess) / 2
    return guess
