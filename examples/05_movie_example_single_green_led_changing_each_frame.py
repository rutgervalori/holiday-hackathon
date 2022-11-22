from xled_plus.samples.sample_setup import *

import colours
import hosts

ctr = HighControlInterface(hosts.default)

class ChangingLedColorByIndex:
    def __init__(self, ctr):
        self.ctr = ctr
        self.currentFrameNumber = 0

    def decideLedColorBasedOnIndex(self, ledPosition, ledIndex):
        return colours.green if ledIndex == self.currentFrameNumber else colours.pink

    def createPatternForFrame(self, frameNumber):
        useIndex = True
        style = None
        self.currentFrameNumber = frameNumber
        return ctr.make_layout_pattern(
            self.decideLedColorBasedOnIndex, style,
            useIndex)


totalNumberOfFrames = ctr.num_leds # make sure this movie works for all amount of leds, as it will create a frame for each led
framesPerSecond = 10

#ChangingLedColorByIndex(ctr)

movie = ctr.make_func_movie(
        totalNumberOfFrames, ChangingLedColorByIndex(ctr).createPatternForFrame
    )

ctr.show_movie(movie,framesPerSecond) # This line uploads the movie to Twinkly, so comment if you do not want it to
