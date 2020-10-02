import gpiozero
import sys

robot = gpiozero.Robot(left=(26,16), right=(5,6))

lefts = gpiozero.DigitalInputDevice(17)
rights = gpiozero.DigitalInputDevice(27)
leftend = gpiozero.DigitalInputDevice(22)
rightend = gpiozero.DigitalInputDevice(23)



while True:
    if (lefts.is_active == True) and (rights.is_active == True) and (leftend.is_active == True) and (rightend.is_active == True):
        robot.stop()
        break
    elif (lefts.is_active == True) and (rights.is_active == True):
        robot.forward()
    elif (lefts.is_active == False) and (rights.is_active == True):
        robot.right()
    elif (lefts.is_active == True) and (rights.is_active == False):
        robot.left()
    elif (rightend.is_active == True):
        robot.right()
    elif (leftend.is_active == True):
        robot.left()

sys.exit()

    