import brickpi
import time

interface=brickpi.Interface()
interface.initialize()

motors = [0,1]

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

motorParams = [];

# set params for motor 0
motorParams.append(interface.MotorAngleControllerParameters())
motorParams[0].maxRotationAcceleration = 6.0
motorParams[0].maxRotationSpeed = 12.0
motorParams[0].feedForwardGain = 255/20.0
motorParams[0].minPWM = 18.0
motorParams[0].pidParameters.minOutput = -255
motorParams[0].pidParameters.maxOutput = 255
motorParams[0].pidParameters.k_p = 20.0
motorParams[0].pidParameters.k_i = 0.0
motorParams[0].pidParameters.k_d = 0.0

# set params for motor 1
motorParams.append(interface.MotorAngleControllerParameters())
motorParams[1].maxRotationAcceleration = 6.0
motorParams[1].maxRotationSpeed = 12.0
motorParams[1].feedForwardGain = 255/20.0
motorParams[1].minPWM = 18.0
motorParams[1].pidParameters.minOutput = -255
motorParams[1].pidParameters.maxOutput = 255
motorParams[1].pidParameters.k_p = 220.0
motorParams[1].pidParameters.k_i = 0.0
motorParams[1].pidParameters.k_d = 0.0

interface.setMotorAngleControllerParameters(motors[0],motorParams[0])
interface.setMotorAngleControllerParameters(motors[1],motorParams[1])

logfile = raw_input("Specify logfile: ")
#f = open("/home/pi/BrickPi/Logfiles/log0.txt");
interface.startLogging("/home/pi/BrickPi/Logfiles/" + logfile)

while True:
	angle = float(input("Enter a angle to rotate (in radians): "))

	interface.increaseMotorAngleReferences(motors,[angle,angle])

	while not interface.motorAngleReferencesReached(motors) :
		print "Refrences: ", interface.getMotorAngleReferences(motors)
		motorAngles = interface.getMotorAngles(motors)
		if motorAngles :
			print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
		time.sleep(0.1)

	print "Destination reached!"

interface.stopLogging()
	

interface.terminate()
