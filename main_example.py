from fireworks import *

def circle(theta):
    return 1;

def sun(theta):
    return ((theta % 72)/48.0)

def fivepoint(theta):
    return .02 * (math.fabs(((theta + 9) % 72) - 36) + 36)

def spiral(theta):
    return theta/360

def degToRad(theta):
    return theta * math.pi / 180

def heartlike(theta):
    rad = degToRad(theta)
    return -.7*(1 - math.sin(rad))

def heart(theta):
    rad = degToRad(theta)
    return -.6*(
        (math.sin(rad) * math.sqrt(math.fabs(math.cos(rad))))
        /
        (math.sin(rad) + 1.4)
        - 2 * math.sin(rad) + 2
        )

def white(theta):
    return (255, 255, 255)

def red(theta):
    return (255, 0, 0)

def blue(theta):
    return (0, 0, 255)

def yellow(theta):
    return (255, 255, 0)

def green(theta):
    return (0, 255, 0)

# start(circle, white)

shapes = [ circle, sun, fivepoint, spiral, heart ]
colors = [ white, red, blue, yellow, green ]

startMany(shapes, colors)
