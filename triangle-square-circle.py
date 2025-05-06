import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def interpolate_shapes(shape1, shape2, t):
    return shape1 * (1 - t) + shape2 * t


def generate_polygon(n_sides, n_points):
    angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
    shape = np.c_[np.cos(np.linspace(0, 2*np.pi, n_sides, endpoint=False)),
                  np.sin(np.linspace(0, 2*np.pi, n_sides, endpoint=False))]
    return np.array([shape[i % n_sides] for i in range(n_points)])


def generate_circle(n_points):
    angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
    return np.c_[np.cos(angles), np.sin(angles)]


N = 100
triangle = generate_polygon(3, N)
square = generate_polygon(4, N)
circle = generate_circle(N)

#  triangle -> square -> circle -> triangle
shapes = [triangle, square, circle, triangle]

transition_frames = 50
pause_frames = 20
total_phases = len(shapes) - 1
frames_per_phase = transition_frames + pause_frames
total_frames = total_phases * frames_per_phase

fig, ax = plt.subplots()
line, = ax.plot([], [], 'o-', lw=2)
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')

def init(): 
    line.set_data([], [])
    return line,

def animate(frame):
    phase = frame // frames_per_phase
    frame_in_phase = frame % frames_per_phase

    current_shape = shapes[phase]
    next_shape = shapes[phase + 1]

    if frame_in_phase < pause_frames:
        shape = current_shape
    else:
        t = (frame_in_phase - pause_frames) / transition_frames
        shape = interpolate_shapes(current_shape, next_shape, t)

    x, y = shape[:, 0], shape[:, 1]
    line.set_data(np.append(x, x[0]), np.append(y, y[0]))  
    return line,

ani = FuncAnimation(fig, animate, frames=total_frames, init_func=init, blit=True, interval=50, repeat=True)
plt.show()
