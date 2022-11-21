from xled_plus.samples.sample_setup import *
import hosts

ctr = HighControlInterface(hosts.default)

numberOfLeds = ctr.num_leds
middleIndex = (numberOfLeds-1) / 2
useIndex = True
specificLayoutShape = None

pattern = ctr.make_layout_pattern(
    lambda ledPosition, ledIndex: rgb_color(0.0, 1.0, 1.0) if ledIndex<=middleIndex else rgb_color(1.0, 0.0, 1.0), specificLayoutShape, useIndex)

ctr.show_pattern(pattern)  # This line uploads the pattern to Twinkly, so comment if you do not want it to