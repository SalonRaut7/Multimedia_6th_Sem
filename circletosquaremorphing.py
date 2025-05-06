import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

WIDTH, HEIGHT = 600, 600
RADIUS = 150
NUM_POINTS = 120
DURATION = 4.0  
FPS = 60
TOTAL_FRAMES = int(DURATION * FPS)

CENTER = np.array([WIDTH // 2, HEIGHT // 2])

def generate_circle_points(center, radius, num_points):
    angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return np.column_stack((x, y))

def generate_square_points(center, radius, num_points):
    points = []
    for i in range(num_points):
        t = i / num_points
        angle = 2 * np.pi * t
        x = np.cos(angle)
        y = np.sin(angle)
        max_component = max(abs(x), abs(y))
        x = (x / max_component) * radius
        y = (y / max_component) * radius
        points.append(center + np.array([x, y]))
    return np.array(points)

def interpolate_points(p1, p2, t):
    return p1 + (p2 - p1) * t


circle = generate_circle_points(CENTER, RADIUS, NUM_POINTS)
square = generate_square_points(CENTER, RADIUS, NUM_POINTS)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.axis('off')
polygon, = ax.plot([], [], color='cornflowerblue', lw=2)

direction = [1]  

def update(frame):
    t = frame / TOTAL_FRAMES
    t = min(t, 1)
    if direction[0] == 1:
        shape = interpolate_points(circle, square, t)
    else:
        shape = interpolate_points(square, circle, t)

    if frame == TOTAL_FRAMES - 1:
        direction[0] *= -1 
        ani.event_source.stop()  
        plt.pause(0.2)
        ani.event_source.start()

    polygon.set_data(np.append(shape[:, 0], shape[0, 0]), np.append(shape[:, 1], shape[0, 1]))
    return polygon,

ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000/FPS, blit=True, repeat=True)
plt.show()
