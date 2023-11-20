def gradient_descent(starting_point, learning_rate, num_iterations):
    x = starting_point

    def function_to_minimize(x):
        return (x + 3)**2

    for _ in range(num_iterations):
        gradient = 2 * (x + 3)  # Derivative of the function

        x = x - learning_rate * gradient

    return x, function_to_minimize(x)

initial_point = 2
learning_rate = 0.1
iterations = 100

minimum_point, minimum_value = gradient_descent(initial_point, learning_rate, iterations)

print("Local minimum point:", minimum_point)
print("Minimum value of the function:", minimum_value)
