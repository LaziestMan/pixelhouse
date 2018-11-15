# A working file to test various aspects of the module
import numpy as np
import pixelhouse as ph
from pixelhouse import Canvas, Animation, circle, rectangle

C = Canvas(width=400, height=400, bg="purple")

with C.layer() as CX:
    CX += circle(x=0, color="w")
    for i in range(10):
        CX += ph.filters.gaussian_blur(blur_x=0.25)

    CX += circle(x=0, color="w")

C += circle(x=0, y=2, r=0.7, color="r")
C += circle(x=0, y=-2, r=0.7, color="k")
C += circle(x=0, y=2, r=0.7, color="r")

C.show()
