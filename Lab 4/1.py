import matplotlib.pyplot as plt

def midpoint_ellipse(xc, yc, rx, ry):
    x_points = []
    y_points = []

    x = 0
    y = ry

    
    rx2 = rx * rx
    ry2 = ry * ry
    two_rx2 = 2 * rx2
    two_ry2 = 2 * ry2

    # Region 1
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)
    dx = two_ry2 * x
    dy = two_rx2 * y

    while dx < dy:
        
        x_points.extend([xc + x, xc - x, xc + x, xc - x])
        y_points.extend([yc + y, yc + y, yc - y, yc - y])

        x += 1
        dx += two_ry2
        if p1 < 0:
            p1 += ry2 + dx
        else:
            y -= 1
            dy -= two_rx2
            p1 += ry2 + dx - dy

    # Region 2
    p2 = ry2 * ((x + 0.5)**2) + rx2 * ((y - 1)**2) - rx2 * ry2
    while y >= 0:
        x_points.extend([xc + x, xc - x, xc + x, xc - x])
        y_points.extend([yc + y, yc + y, yc - y, yc - y])

        y -= 1
        dy -= two_rx2
        if p2 > 0:
            p2 += rx2 - dy
        else:
            x += 1
            dx += two_ry2
            p2 += rx2 - dy + dx

    return x_points, y_points


def plot_ellipse(xc, yc, rx, ry):
    x, y = midpoint_ellipse(xc, yc, rx, ry)
    plt.figure(figsize=(6,6))
    plt.plot(x, y, 'o', color='purple')
    plt.title(f"Midpoint Ellipse Algorithm (rx={rx}, ry={ry})")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

plot_ellipse(0, 0, 10, 5)