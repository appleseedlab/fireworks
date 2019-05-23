from fireworks import *

shapes = {
'circle' : lambda theta, rad, t: 1,
'circle' : lambda theta, rad, t: 1,
'circle' : lambda theta, rad, t: 1,
'circle' : lambda theta, rad, t: 1,
'heart1' : lambda theta, rad, t: -.7*(1 - math.sin(rad)),
'heart2' : lambda theta, rad, t: -.6*(
    (math.sin(rad) * math.sqrt(math.fabs(math.cos(rad))))
    /
    (math.sin(rad) + 1.4)
    - 2 * math.sin(rad) + 2
    ),
'fivepoint1' : lambda theta, rad, t: .02 * (math.fabs(((theta+9) % 72) - (72/2)) + 36),
'spiral' : lambda theta, rad, t: .5 * (rad/(math.pi/15)) / (2*math.pi),
'sun' : lambda theta, rad, t: ((theta % 72)/48.0),

'weird1' : lambda theta, rad, t: ((theta % 24)/48 + .5),
'weird2' : lambda theta, rad, t: ((theta % 72) / 2 - 72)*.025,
'fourpoint1' : lambda theta, rad, t: .025 * ((theta % 90) - (90/2)),
'twopoint' : lambda theta, rad, t: .01 * (math.fabs((theta % 180) - (180/2))),
'threepoint' : lambda theta, rad, t: .02 * (math.fabs((theta % 120) - (120/2))),
'fourpoint2' : lambda theta, rad, t: .02 * (math.fabs((theta % 90) - (90/2))),
'fivepoint2' : lambda theta, rad, t: .02 * (math.fabs((theta % 72) - (72/2))),
'fivepoint3' : lambda theta, rad, t: .02 * (math.fabs((theta % 72) - (72/2)) + 10),
}

colors = {
'random' : [],
'random_flicker' : [],
'flicker' : lambda theta, rad, t: t % 2 == 0 and (255, 255, 255) or (0, 0, 0),
'red' : lambda theta, rad, t: (255, 0, 0),
'green' : lambda theta, rad, t: (0, 255, 0),
'blue' : lambda theta, rad, t: (0, 0, 255),
'patriotic' : lambda theta, rad, t: theta >= 0 and theta < 360 / 3 and pygame.color.THECOLORS['red'] or theta >= 360 / 3 and theta < 2 * 360 / 3 and pygame.color.THECOLORS['white'] or theta >= 2 * 360 / 3 and theta < 3 * 360 / 3 and pygame.color.THECOLORS['blue']
}

def circle(theta):
    return 1;

def sun(theta):
    return ((theta % 72)/48.0)

def fivepoint(theta):
    return .02 * (math.fabs(((theta + 9) % 72) - 36) + 36)

def spiral(theta):
    return 2*theta/360

def heartlike(theta):
    rad = theta * math.pi / 180
    return -.7*(1 - math.sin(rad))

def heart(theta):
    rad = theta * math.pi / 180
    return -.6*(
        (math.sin(rad) * math.sqrt(math.fabs(math.cos(rad))))
        /
        (math.sin(rad) + 1.4)
        - 2 * math.sin(rad) + 2
        )

def white(theta):
    return 255, 255, 255

def red(theta):
    return 255, 0, 0

def blue(theta):
    return 0, 0, 255

# start(circle, white)

shapes = [ heartlike ]
colors = [ white, red, blue ]

startMany(shapes, colors)
