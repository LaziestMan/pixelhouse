import random
import numpy as np
import pixelhouse as ph


# Inspired by
# https://dev.to/agathacco/how-to-create-pure-css-illustrations-and-animate-them---part-1-1j1k

# Setup our canvas! Make it 400 by 400 pixels,
canvas = ph.Canvas(400, 400, bg="#FEEE9D")

# Face shadow
canvas += ph.circle(0.1, -0.1, r=3, color="#EFBB42")

# Face
canvas += ph.circle(0, 0, r=3, color="#FBD671")

# Eyes, 400 px = 8
x = 0.9
canvas += ph.ellipse(x, x, a=x * (3 / 10), b=x * (5 / 10), color="#20184E")
canvas += ph.ellipse(-x, x, a=x * (3 / 10), b=x * (5 / 10), color="#20184E")

# Pupils
canvas += ph.ellipse(x - x / 15, x + x / 10, a=x / 6, b=x / 4, color="#FBD671")
canvas += ph.ellipse(-x - x / 15, x + x / 10, a=x / 6, b=x / 4, color="#FBD671")

# Mouth
canvas += ph.ellipse(
    0,
    -x * 0.75,
    a=1.5 * x,
    b=1.25 * x,
    angle_start=np.pi,
    angle_end=2 * np.pi,
    color="#20184E",
)

# Tounge color #F15962; 100/80
# Display the image. It'll stay open until you press a key.
canvas.show()