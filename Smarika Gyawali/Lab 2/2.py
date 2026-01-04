import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    x_points = []
    y_points = []

    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1

    for i in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc

    return x_points, y_points


def plot_dda(x1, y1, x2, y2):
    x, y = dda_line(x1, y1, x2, y2)

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    plt.title("DDA Line Drawing Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

plot_dda(2, 3, 10, 8)