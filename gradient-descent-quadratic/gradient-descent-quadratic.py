def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    x = x0
    for _ in range(0,steps):
        x_next = x - lr*(2*a*x + b)
        x = x_next
    return x_next
    pass