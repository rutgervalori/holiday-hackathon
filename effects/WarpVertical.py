from xled_plus.samples.sample_setup import *

class WarpVertical(Effect):
    def __init__(self, ctr, colorList, folds, speed):
        super(WarpVertical, self).__init__(ctr)
        self.colorList = colorList ## List of colors to be used for leds
        self.ncols = len(colorList) * folds
        self.speedfactor = float(speed) / self.preferred_fps
        self.preferred_frames = int(len(colorList) * self.preferred_fps / speed)
    def getLedColor(self, pos):
        yPos = pos[1]
        n = round(yPos * self.ncols / (2 * m.pi) + self.tm * self.speedfactor)
        colorIndex = int(n) % len(self.colorList)
        color = self.colorList[colorIndex]
        return color
    def reset(self, numframes):
        self.tm = 0
    def getnext(self):
        pattern = self.ctr.make_layout_pattern(self.getLedColor, None)
        self.tm += 1
        return pattern
    def doNotLaunchMovie(self):
        self.make_movie(self.preferred_frames)
