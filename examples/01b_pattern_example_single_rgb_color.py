from xled_plus.samples.sample_setup import *
import hosts

ctr = HighControlInterface(hosts.default)


def provideColor(position):
    return rgb_color(1.0, 1.0, 1.0)

'''
make_layout_pattern requires a function as an argument,
and that function needs to accept one argument
So we're passing it the provideColor method
In this example we're passing a specific method
in the 1a version we're using a lamda to achieve the same result'''
pattern = ctr.make_layout_pattern(
    provideColor
)

ctr.show_pattern(pattern)  # This line uploads the pattern to Twinkly, so comment if you do not want it to

