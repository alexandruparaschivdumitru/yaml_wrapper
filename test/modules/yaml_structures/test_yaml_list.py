from unittest import TestCase

class TestYamlList(TestCase):
    pass

# Data structures tested:
# serials:
#   - label    : Chinese_GPS
#     speed    : 9600
#     address  : "/dev/ttyACM0"

#  - label   : Kendau_GPS
#    speed   : 9600
#    address : /dev/ttyUSB0
# Converted in ADT
# ------------------------------
# data = {
#     key: serials
#     value : [
#         [{label: speed},{speed: 9600},{assdress: "h,mfhd"}],
#         [{label: speed},{speed: 9600},{assdress: "h,mfhd"}]
#     ]
# }