def newton_forward_interpolation(x_values, y_values, x_to_interpolate):
    """
    Computes the interpolated value of a function at a given x_to_interpolate
    using Newton's Forward Interpolation formula.

    :param x_values: List of x values (equally spaced interpolation nodes)
    :param y_values: List of corresponding y values
    :param x_to_interpolate: The x value at which to find the interpolated y value
    :return: Interpolated y value
    """
    n = len(x_values)
    h = x_values[1] - x_values[0]  # Height between values
    diff_table = [[0] * n for _ in range(n)] # Creates n by n table full of 0

    # Filling the first column Δ f(x)
    for i in range(n):
        diff_table[i][0] = y_values[i]

    # Calculate forward differences Δ2 f(x), Δ2 f(x) ....
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1] # Δ2 f(x1) = Δ f(x2) - Δ f(x)

    # Calculate p
    p = (x_to_interpolate - x_values[0]) / h    # p = (x-x0)/height

    # Newton's formula
    y_interpolated = y_values[0]
    p_term = 1  # The current p term in the formula: p(p-1)(p-2).../(n!)
    for j in range(1, n):
        p_term *= (p - (j - 1)) / j
        y_interpolated += p_term * diff_table[0][j]

    return y_interpolated


def lagrange_interpolation(x_points, y_points, x):
    """
    Computes the Lagrange Interpolation for a given value of x.

    Parameters:
    - x_points: List of x-coordinates of the data points.
    - y_points: List of corresponding y-coordinates of the data points.
    - x: The x-value at which to estimate the interpolated value.

    Returns:
    - Interpolated value of y at the given x.
    """
    if len(x_points) != len(y_points):
        raise ValueError("x_points and y_points must have the same length.")

    n = len(x_points)
    y = 0

    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (x - x_points[j]) / (x_points[i] - x_points[j])

        # Add contribution of this term to the result
        y += y_points[i] * L

    return y

def newton_divided_difference(x_points, y_points, x):
    """"
    Computes the Newton Divided Difference Interpolation for a given value of x.

    Parameters:
    - x_points: List of x-coordinates of the data points.
    - y_points: List of corresponding y-coordinates of the data points.
    - x: The x-value at which to estimate the interpolated value.

    Returns:
    - Interpolated value of y at the given x.
    """
    if len(x_points) != len(y_points):
        raise ValueError("x_points and y_points must have the same length.")

    n = len(x_points) # matrix n x n len

    divided_diff = [[0] * n for _ in range(n)] #filling matrix n by n zero

    # Populate the first column with y_points
    for i in range(n):
        divided_diff[i][0] = y_points[i]

    # Compute the divided differences
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i][j] = (divided_diff[i + 1][j - 1] - divided_diff[i][j - 1]) / (
                        x_points[i + j] - x_points[i])

    # Perform interpolation
    result = divided_diff[0][0]
    product = 1
    for i in range(1, n):
        product *= (x - x_points[i - 1])
        result += product * divided_diff[0][i]

    return result


def line():
    print(50 * "//")
