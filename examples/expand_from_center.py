from xled_plus.samples.sample_setup import *

ctr = setup_control()
ctr.fetch_layout()

## centerSizeIncrease should be max 1.0
def ledIsInCenter(ledPosition, centerSizeIncrease=0.0):
    centerX = ctr.layout_bounds['center'][0]
    centerY = ctr.layout_bounds['center'][1]
    centerZ = ctr.layout_bounds['center'][2]

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
    # xBool = pos[0] > -0.10 and pos[0] < -0.02
    # yBool = pos[1] < 0.5 and pos[1] > 0.3
    zBool = True
    return xBool and yBool and zBool


## green spot in center
# ctr.show_pattern(ctr.make_layout_pattern(
#     lambda ledPosition, ledIndex: rgb_color(0.0, 1.0, 0.0) if ledIsInCenter(ledPosition, 0.3) else rgb_color(1.0, 0.0, 0.0), None, True)
# )
#

fullFrameNumber = 60
framerate = 1

def expandAndRetractLedColors(currentFrameNumber, ledPosition, ledIndex):
    halfwayPointMovie = fullFrameNumber / 2

    hueColor =  (ledPosition[1] - currentFrameNumber / fullFrameNumber) % 1.0 #min 0.0, max 1.0

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

def expandLedColors(currentFrameNumber, ledPosition, ledIndex):
    if ledIsInCenter(ledPosition, currentFrameNumber/fullFrameNumber):
        ledColor = rgb_color(0.0, 0.2, 0.0)
    else:
        ledColor = rgb_color(0.2, 0.0, 0.0)
    return ledColor

# ctr.show_movie(
#     ctr.make_func_movie(
#         fullFrameNumber,
#         lambda currentFrameNumber: ctr.make_layout_pattern(lambda ledPosition, ledIndex: expandAndRetractLedColors(currentFrameNumber, ledPosition, ledIndex), None, True)
#     ),
#     framerate,
# )

ctr.show_movie(
    ctr.make_func_movie(
        fullFrameNumber,
        lambda currentFrameNumber: ctr.make_layout_pattern(lambda ledPosition, ledIndex: rgb_color(0.0, 0.2, 0.0) if ledIsInCenter(ledPosition, currentFrameNumber/fullFrameNumber) else rgb_color(0.2, 0.0, 0.0), None, True)
    ),
    20,
)