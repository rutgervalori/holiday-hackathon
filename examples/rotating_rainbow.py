"""
Tips:
Speed should be high when using more colors
For example: 100 for 400 colors
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
        a = m.atan2(pos[2], pos[0])
        r = m.sqrt(pos[0]**2 + pos[2]**2)
        n = round(a * self.ncols / (2 * m.pi) + self.tm * self.speedfactor)
        colorIndex = int(n) % len(self.cols)
        col = self.cols[colorIndex]
        if r < 0.0: ## set center radius. 0.0 is no center color
            return self.white
        else:
            return col
    def reset(self, numframes):
        self.tm = 0
    def getnext(self):
        pat = self.ctr.make_layout_pattern(self.getcolor, "centered")
        self.tm += 1
        return pat

ctr = setup_control()

def getColor(i):
    hueColor = i % 1.0  # min 0.0, max 1.0
    return hsl_color(hueColor, 1.0, 0.3)

def createColorList():
    pat = [False] * ctr.num_leds
    for i in range(ctr.num_leds):
        pat[i] = getColor(i/ctr.num_leds)
    return pat


cols = createColorList()
WheelEffect(ctr, cols, 1, 100).launch_movie()
