from xled_plus.samples.sample_setup import *
import colours
import hosts

ctr = HighControlInterface(hosts.default)

ctr.fetch_layout()  # fetch layout so we can ask for led coordinates
centerX = ctr.layout_bounds['center'][0] # see 04_show_boundaries file for example of other bounds
useIndex = False
specificLayoutShape = None

pattern = ctr.make_layout_pattern(
    lambda ledPosition: colours.teal if ledPosition[0]<=centerX else colours.pink, specificLayoutShape, useIndex)

ctr.show_pattern(pattern)  # This line uploads the pattern to Twinkly, so comment if you do not want it to

