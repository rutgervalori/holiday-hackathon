"""
Tips:
Speed should be high when using more colors

"""

from xled_plus.samples.sample_setup import *

import colours
from effects.RotateOnYAxisEffect import RotateOnYAxisEffect
import hosts

ctr = HighControlInterface(hosts.default)


def getListColor(i):
    return colours.green if i == 0 else colours.black

def createColorList():
    listLength = int(ctr.num_leds/16)
    colorList = [False] * listLength
    for i in range(listLength):
        colorList[i] = getListColor(i)
    return colorList


speed = 10
fold = 1
cols = createColorList()
RotateOnYAxisEffect(ctr, cols, fold, speed).launch_movie()
# if you do not want to upload the movie to Twinkly, use -> RotateOnYAxisEffect(ctr, cols, fold, speed).doNotLaunchMovie()
