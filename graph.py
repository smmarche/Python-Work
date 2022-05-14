import os
import matplotlib.pyplot as drawing

coefficients = input("Enter coefficients: ").split(",")
int_coefficients = [int(i) for i in coefficients]

coefficient_a = int_coefficients[0]
coefficient_b = int_coefficients[1]
coefficient_c = int_coefficients[2]

x_values = list(range(-10, 11))
y_values = [coefficient_a * n + coefficient_b for n in x_values]
drawing.plot(x_values, y_values, color="g", label=f"{coefficient_a}x+{coefficient_b}")


x_values = list(range(-10, 11))
y_values = [coefficient_a * n ** 2 + coefficient_b * n + coefficient_c for n in x_values]
drawing.plot(x_values, y_values, color="r", label=f"{coefficient_a}x^2+{coefficient_b}+{coefficient_c}")

drawing.xlabel("x values")
drawing.ylabel("y values")
drawing.legend()
drawing.grid()
drawing.title("Linear and Quadratic Equations")

os.mkdir('equations') # Make a directory
os.chdir('equations') # Change directory
drawing.savefig('equations.png')

drawing.show()
drawing.close()