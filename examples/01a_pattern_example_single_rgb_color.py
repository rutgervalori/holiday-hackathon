from xled_plus.samples.sample_setup import *
import hosts

ctr = HighControlInterface(hosts.default)

'''
make_layout_pattern requires a function as an argument,
and that function needs to accept one argument.
So we're passing it a lamda (anonymous function: https://www.w3schools.com/python/python_lambda.asp)
In the 1b version we're using a method instead of a lambda to achieve the same result'''
pattern = ctr.make_layout_pattern(
    lambda pos: rgb_color(1.0, 1.0, 0.0)
)

ctr.show_pattern(pattern)  # This line uploads the pattern to Twinkly, so comment if you do not want it to

