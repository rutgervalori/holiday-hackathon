from xled_plus.samples.sample_setup import *

class RotateOnYAxisEffect(Effect):
    def __init__(self, ctr, colorList, folds, speed):
        super(RotateOnYAxisEffect, self).__init__(ctr)
        self.colorList = colorList ## List of colors to be used for leds
        self.ncols = len(colorList) * folds
        self.speedfactor = float(speed) / self.preferred_fps
        self.preferred_frames = int(len(colorList) * self.preferred_fps / speed)
    def getLedColor(self, pos):
        a = m.atan2(pos[2], pos[0]) # calculate angle with Z and X coordinates
        n = round(a * self.ncols / (2 * m.pi) + self.tm * self.speedfactor)
        colorIndex = int(n) % len(self.colorList)
        color = self.colorList[colorIndex]
        return color
    def reset(self, numframes):
        self.tm = 0
    def getnext(self):
        pattern = self.ctr.make_layout_pattern(self.getLedColor, "centered")
        self.tm += 1
        return pattern
    def doNotLaunchMovie(self):
        self.make_movie(self.preferred_frames)
