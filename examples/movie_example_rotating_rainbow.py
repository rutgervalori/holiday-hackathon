"""
Tips:
Speed should be high when using more colors
For example: 100 for 400 colors
"""

from xled_plus.samples.sample_setup import *
from effects.RotateOnYAxisEffect import RotateOnYAxisEffect
import hosts

ctr = HighControlInterface(hosts.default)


def getListColor(i):
    hueColor = i % 1.0  # min 0.0, max 1.0
    return hsl_color(hueColor, 1.0, 0.3)

def createColorList():
    colorList = [False] * ctr.num_leds
    for i in range(ctr.num_leds):
        colorList[i] = getListColor(i/ctr.num_leds)
    return colorList


speed = 100
fold = 1
colorPattern = createColorList()
RotateOnYAxisEffect(ctr, colorPattern, fold, speed).launch_movie()
# if you do not want to upload the movie to Twinkly, use -> RotateOnYAxisEffect(ctr, cols, fold, speed).doNotLaunchMovie()
