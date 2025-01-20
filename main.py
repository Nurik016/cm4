from methods import *

# 1 (newton_forward_interpolation)
x_values = [1, 1.4, 1.8, 2.2]
y_values = [3.49, 4.82, 5.96, 6.5]

x_to_interpolate = 1.6
y_interpolated = newton_forward_interpolation(x_values, y_values, x_to_interpolate)
print(f"The interpolated value of f(1.6) is {y_interpolated:.4f}  (newton_forward_interpolation)")
line()


# 2 (lagrange_interpolation)
x2_points = [5, 6, 9, 11]
y2_points = [12, 13, 14, 16]

x2_to_interpolate = 10
interpolated_value = lagrange_interpolation(x2_points, y2_points, x2_to_interpolate)
print(f"The interpolated value of y at x = {x2_to_interpolate} is {interpolated_value:.2f} (lagrange_interpolation)")
line()


# 3 (newton_divided_difference)
x3_points = [1, 2, 4, 6]
y3_points = [-26, 12, 256, 844]

x3_to_interpolate = 3
interpolated_value = newton_divided_difference(x3_points, y3_points, x3_to_interpolate)
print(f"The interpolated value of u(3) is {interpolated_value:.2f} (newton_divided_difference)")