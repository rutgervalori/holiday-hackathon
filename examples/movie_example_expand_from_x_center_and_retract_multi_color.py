from xled_plus.samples.sample_setup import *
import hosts

ctr = HighControlInterface(hosts.default)

ctr.fetch_layout()

movie_frames_total = 60
movie_fps = 20

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

def expandAndRetractLedColors(currentFrameNumber, ledPosition):
    halfwayPointMovie = movie_frames_total / 2

    hueColor = (ledPosition[1] - currentFrameNumber / movie_frames_total) % 1.0 #min 0.0, max 1.0

    if currentFrameNumber <= halfwayPointMovie:
        if ledIsInCenter(ledPosition, currentFrameNumber/halfwayPointMovie):
            ledColor = hsl_color(hueColor, 1.0, 0.3)
        else:
            ledColor = rgb_color(0.0, 0.0, 0.0)
    else:
        if ledIsInCenter(ledPosition, 1-((currentFrameNumber-halfwayPointMovie)/halfwayPointMovie)):
            ledColor = hsl_color(hueColor, 1.0, 0.3)
        else:
            ledColor = rgb_color(0.0, 0.0, 0.0)
    return ledColor


movie = ctr.make_func_movie(
        movie_frames_total,
        lambda currentFrameNumber: ctr.make_layout_pattern(lambda ledPosition, ledIndex: expandAndRetractLedColors(currentFrameNumber, ledPosition), None, True)
    )


ctr.show_movie(movie,movie_fps) # This line uploads the movie to Twinkly, so comment if you do not want it to
