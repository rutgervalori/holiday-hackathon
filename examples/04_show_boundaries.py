from xled_plus.samples.sample_setup import *
import hosts

ctr = HighControlInterface(hosts.default)

ctr.fetch_layout()

fullFrameNumber = 35
framerate = 1

centerX = ctr.layout_bounds['center'][0]
centerY = ctr.layout_bounds['center'][1]
centerZ = ctr.layout_bounds['center'][2]

minXLayoutBoundry = ctr.layout_bounds['bounds'][0][0]
maxXLayoutBoundry = ctr.layout_bounds['bounds'][0][1]
minYLayoutBoundry = ctr.layout_bounds['bounds'][1][0]
maxYLayoutBoundry = ctr.layout_bounds['bounds'][1][1]
minZLayoutBoundry = ctr.layout_bounds['bounds'][2][0]
maxZLayoutBoundry = ctr.layout_bounds['bounds'][2][1]

def ledMinXBoundAdjecent(ledPosition, margin=0.0):
    xBool = ledPosition[0] >= minXLayoutBoundry and ledPosition[0] <= minXLayoutBoundry+margin
    return xBool

def ledMaxXBoundAdjecent(ledPosition, margin=0.0):
    xBool = ledPosition[0] >= maxXLayoutBoundry-margin and ledPosition[0] <= maxXLayoutBoundry
    return xBool

def ledMinYBoundAdjecent(ledPosition, margin=0.0):
    yBool = ledPosition[1] >= minYLayoutBoundry and ledPosition[1] <= minYLayoutBoundry+margin
    return yBool

def ledMaxYBoundAdjecent(ledPosition, margin=0.0):
    yBool = ledPosition[1] >= maxYLayoutBoundry-margin and ledPosition[1] <= maxYLayoutBoundry
    return yBool

def ledMinZBoundAdjecent(ledPosition, margin=0.0):
    zBool = ledPosition[2] >= minZLayoutBoundry and ledPosition[2] <= minZLayoutBoundry+margin
    return zBool

def ledMaxZBoundAdjecent(ledPosition, margin=0.1):
    zBool = ledPosition[2] >= maxZLayoutBoundry-margin and ledPosition[2] <= maxZLayoutBoundry
    return zBool


def returnColorForLedByBound(frameNumber, ledPosition):
    ledColor = rgb_color(0.2, 0.0, 0.0)  # red
    print("Pos is: "+"X:"+ str(ledPosition[0])+", Y:"+ str(ledPosition[1])+", Z:"+ str(ledPosition[2]))
    if frameNumber <= 5:
        if ledMinXBoundAdjecent(ledPosition, 0.2):
            ledColor = rgb_color(0.0, 0.2, 0.0)  # green
    if frameNumber > 5 and frameNumber <= 10:
        if ledMaxXBoundAdjecent(ledPosition, 0.2):
            ledColor = rgb_color(0.0, 0.0, 0.2)  # blue
    if frameNumber > 10 and frameNumber <= 15:
        if ledMaxYBoundAdjecent(ledPosition, 0.2):
            ledColor = rgb_color(255/255, 136/255, 0) # orange
    if frameNumber > 15 and frameNumber <= 20:
        if ledMinYBoundAdjecent(ledPosition, 0.2):
            ledColor = rgb_color(0.2, 0.9, 1.0) # turqoise
    if frameNumber > 20 and frameNumber <= 25:
        if ledMaxZBoundAdjecent(ledPosition, 0.4):
            ledColor = rgb_color(255/255, 0, 166/255)  # pink
    if frameNumber > 25 and frameNumber <= 30:
        if ledMinZBoundAdjecent(ledPosition, 0.2):
            ledColor = rgb_color(187/255, 0, 255/255) # purple?
    return ledColor

style = None #'square', 'rect', 'centered', 'cylinder', 'sphere'
movie_fps = 1
movie = ctr.make_func_movie(
        fullFrameNumber,
        lambda currentFrameNumber: ctr.make_layout_pattern(lambda ledPosition, ledIndex: returnColorForLedByBound(currentFrameNumber, ledPosition), style, True)
    )

ctr.show_movie(movie,movie_fps) # This line uploads the movie to Twinkly, so comment if you do not want it to




