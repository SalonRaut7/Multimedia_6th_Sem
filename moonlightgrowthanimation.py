from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

WIDTH, HEIGHT = 400, 400
MOON_RADIUS = 80
CENTER = (WIDTH // 2, HEIGHT // 2)
BG_COLOR = (10, 10, 30)
WHITE = (255, 255, 255)

fig, ax = plt.subplots()
ax.axis('off')
img_display = ax.imshow(np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8))

def draw_moon_phase(phase):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)


    draw.ellipse([CENTER[0] - MOON_RADIUS, CENTER[1] - MOON_RADIUS,
                  CENTER[0] + MOON_RADIUS, CENTER[1] + MOON_RADIUS], fill=WHITE)

    if phase <= 1.0:
        offset = (1.0 - phase) * 2 * MOON_RADIUS
        draw.ellipse([CENTER[0] - MOON_RADIUS + offset, CENTER[1] - MOON_RADIUS,
                      CENTER[0] + MOON_RADIUS + offset, CENTER[1] + MOON_RADIUS], fill=BG_COLOR)
    else:
        offset = (phase - 1.0) * 2 * MOON_RADIUS
        draw.ellipse([CENTER[0] - MOON_RADIUS, CENTER[1] - MOON_RADIUS,
                      CENTER[0] + MOON_RADIUS, CENTER[1] + MOON_RADIUS], fill=BG_COLOR)
        draw.ellipse([CENTER[0] - MOON_RADIUS + offset, CENTER[1] - MOON_RADIUS,
                      CENTER[0] + MOON_RADIUS + offset, CENTER[1] + MOON_RADIUS], fill=BG_COLOR)

    return np.array(img)

def update(frame):
    phase = (frame % 100) / 50  
    img = draw_moon_phase(phase)
    img_display.set_data(img)

ani = FuncAnimation(fig, update, frames=200, interval=50, repeat=True)
plt.show()
