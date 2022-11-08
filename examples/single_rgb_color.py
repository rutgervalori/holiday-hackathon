from xled_plus.samples.sample_setup import *

ctr = setup_control()
ctr.show_pattern(ctr.make_layout_pattern(
    lambda pos: rgb_color(1.0, 1.0, 0.0)
))

