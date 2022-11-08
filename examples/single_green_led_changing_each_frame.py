from xled_plus.samples.sample_setup import *

ctr = setup_control()

ctr.show_movie(
    ctr.make_func_movie(
        400,
        lambda frameNumber: ctr.make_layout_pattern(lambda ledPosition, ledIndex: rgb_color(0.0, 1.0, 0.0) if ledIndex == frameNumber else rgb_color(1.0, 0.0, 0.0), None, True)
    ),
    10,
)

