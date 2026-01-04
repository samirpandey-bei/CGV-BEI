def dda_operations(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    additions = 0
    multiplications = 0

    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps
    multiplications += 2

    x, y = x1, y1
    for i in range(steps):
        x += x_inc
        y += y_inc
        additions += 2

    return additions, multiplications


def bresenham_operations(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    additions = 3
    multiplications = 0

    while dx > 0 or dy > 0:
        additions += 2
        dx -= 1

    return additions, multiplications



dda_add, dda_mul = dda_operations(2, 3, 10, 8)
br_add, br_mul = bresenham_operations(2, 3, 10, 8)

print("DDA Algorithm:")
print("Additions =", dda_add)
print("Multiplications =", dda_mul)

print("\nBresenham Algorithm:")
print("Additions =", br_add)
print("Multiplications =", br_mul)