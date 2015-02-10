from utils import *

SQUARE_LOG_FILE_NAME = "square"

interface.startLogging("/home/pi/BrickPi/Logfiles/" + SQUARE_LOG_FILE_NAME)

# Move 10cm forward
move(5)

# Rotate pi radians clockwise
rotate(pi)

interface.stopLogging()

interface.terminate()
