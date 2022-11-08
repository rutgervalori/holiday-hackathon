"""
Tips:
Speed should be high when using more colors

"""

from xled_plus.samples.sample_setup import *

class WheelEffect(Effect):
    def __init__(self, ctr, cols, folds, speed):
        super(WheelEffect, self).__init__(ctr)
        self.cols = cols ## List of colors to be used for leds
        self.folds = folds
        self.ncols = len(cols) * folds
        self.speedfactor = float(speed) / self.preferred_fps
        self.preferred_frames = int(len(cols) * self.preferred_fps / speed)
        self.white = hsl_color(0.0, 0.0, 1.0)

    def getcolor(self, pos):
        angleInRadians = m.atan2(pos[2], pos[0])
        angleInDegrees = m.degrees(angleInRadians)
        # r = m.sqrt(pos[0]**2 + pos[1]**2)
        n = round(angleInRadians * self.ncols / (2 * m.pi) + self.tm * self.speedfactor)
        colorIndex = int(n) % len(self.cols)
        col = self.cols[colorIndex]
        # if r < 0.0: ## set center radius. 0.0 is no center color
        #     return self.white
        # else:
            #return col
        return col

    def reset(self, numframes):
        self.tm = 0

    def getnext(self):
        pat = self.ctr.make_layout_pattern(self.getcolor)
        self.tm += 1
        return pat

ctr = setup_control()

def getColor(i):
    return rgb_color(0.0, 1.0, 0.0) if i == 0 else rgb_color(0.0, 0.0, 0.0)

def createColorList():
    listLength = int(ctr.num_leds/16)
    pat = [False] * listLength
    for i in range(listLength):
        pat[i] = getColor(i)
    return pat


cols = createColorList()
WheelEffect(ctr, cols, 1, 10).launch_movie()
