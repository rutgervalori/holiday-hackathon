from xled_plus.samples.sample_setup import *

import colours
import hosts

ctr = HighControlInterface(hosts.default)
ctr.fetch_layout()  # this method fetches the led layout coordinates we need in the ledIsInCenter method.


## centerSizeIncrease should be max 1.0
def ledIsInCenter(ledPosition, centerSizeIncrease=0.0):
    centerX = ctr.layout_bounds['center'][0]
    centerY = ctr.layout_bounds['center'][1]

    minXLayoutBoundry = ctr.layout_bounds['bounds'][0][0]
    maxXLayoutBoundry = ctr.layout_bounds['bounds'][0][1]
    minYLayoutBoundry = ctr.layout_bounds['bounds'][1][0]
    maxYLayoutBoundry = ctr.layout_bounds['bounds'][1][1]

    minXOffSet = ((minXLayoutBoundry-centerX)*centerSizeIncrease)
    maxXOffset = ((maxXLayoutBoundry-centerX)*centerSizeIncrease)
    minYOffset = ((minYLayoutBoundry-centerY)*centerSizeIncrease)
    maxYOffset = ((maxYLayoutBoundry-centerY)*centerSizeIncrease)
    minXBoundry = centerX + minXOffSet
    maxXBoundry = centerX + maxXOffset
    minYBoundry = centerY + minYOffset
    maxYBoundry = centerY + maxYOffset

    xBool = ledPosition[0] >= minXBoundry and ledPosition[0] <= maxXBoundry
    yBool = ledPosition[1] >= minYBoundry and ledPosition[1] <= maxYBoundry

    return xBool and yBool


movie_frames_total = 60
movie_fps = 20

'''
This method creates a movie with 60 frames, displayed at 20 frames per second (that means the movies will be 3seconds in length).
The led at the center coordinate is set to green. Then for each following frame the size of what is considered the 'center' 
is increased until the whole layout is considered the center (and every led is colored green).
'''
movie = ctr.make_func_movie(
        movie_frames_total,
        lambda currentFrameNumber: ctr.make_layout_pattern(
            lambda ledPosition, ledIndex: colours.green if ledIsInCenter(ledPosition, currentFrameNumber/movie_frames_total) else rgb_color(0.2, 0.0, 0.0), None, True)
    )

ctr.show_movie(movie,movie_fps) # This line uploads the movie to Twinkly, so comment if you do not want it to
