from xled_plus.samples.sample_setup import *

import colours
import hosts

ctr = HighControlInterface(hosts.default)
ctr.fetch_layout()  # fetch layout so we can ask for led coordinates
centerX = ctr.layout_bounds['center'][0]
centerY = ctr.layout_bounds['center'][1]
centerZ = ctr.layout_bounds['center'][2]
useIndex = True
specificLayoutShape = None


patternList = []

patterGreen = ctr.make_layout_pattern(
    lambda ledPosition: colours.teal if ledPosition[0] <= centerX else colours.pink
)
patternRed = ctr.make_layout_pattern(
    lambda ledPosition: colours.red if ledPosition[1] <= centerY else colours.blue
)
patternBlue = ctr.make_layout_pattern(
    lambda ledPosition: colours.hot_pink if ledPosition[2] <= centerZ else colours.white
)

patternList.append(patterGreen)
patternList.append(patternRed)
patternList.append(patternBlue)

movie = ctr.to_movie(patternList)
framesPerSecond = 1

ctr.show_movie(movie, framesPerSecond) # This line uploads the movie to Twinkly, so comment if you do not want it to

