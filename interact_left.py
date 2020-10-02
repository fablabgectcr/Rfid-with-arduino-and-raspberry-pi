import gpiozero

import sys

robot = gpiozero.Robot(left=(26,16), right=(5,6))

lefts = gpiozero.DigitalInputDevice(17)
rights = gpiozero.DigitalInputDevice(27)
leftend = gpiozero.DigitalInputDevice(22)
rightend = gpiozero.DigitalInputDevice(23)

robot.left()
while True:
    if (lefts.is_active == True) and (rights.is_active == True):
        robot.stop()
        break
    else:
        continue

sys.exit()