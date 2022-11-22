from xled_plus.samples.sample_setup import *

import colours
import hosts

ctr = HighControlInterface(hosts.default)

numberOfLeds = ctr.num_leds
middleIndex = (numberOfLeds-1) / 2
useIndex = True
specificLayoutShape = None

pattern = ctr.make_layout_pattern(
    lambda ledPosition, ledIndex: colours.teal if ledIndex<=middleIndex else colours.pink, specificLayoutShape, useIndex)

ctr.show_pattern(pattern)  # This line uploads the pattern to Twinkly, so comment if you do not want it to