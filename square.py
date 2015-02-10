from utils import *

def main():
	SQUARE_LOG_FILE_NAME = "square"

	#initialized brickpi interface 
	interface = brickpi.Interface()
	interface.initialize() 

	#define motor instances 
	motors = [0,1]
	
	#using motorEnable to activate motor 
	interface.motorEnable(motors[0])
	interface.motorEnable(motors[1])

	#set up  motorparameter from the value of interface <?> what is brickpi interface ? 
	motorParams = setup(interface)
	robot_until = RobotUtility() #where does this method comes from?

	#manully set drift callibration for test 
	if len(sys.argv) == 4:
    	robot_util.set_drift_callibration(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    else :
    	print "no drift calibration values set "

	#square move script  
	#verbose : switch on/off debug information
	robot_util.move (15,interface,motorParams,verbose = True)
	robot_util.rotate(pi/2, interface, motorParams, verbose=True)
	robot_util.move (15,interface,motorParams,verbose = True)
	robot_util.rotate(pi/2, interface, motorParams, verbose=True)
	robot_util.move (15,interface,motorParams,verbose = True)
	robot_util.rotate(pi/2, interface, motorParams, verbose=True)
	robot_util.move (15,interface,motorParams,verbose = True)
	robot_util.rotate(pi/2, interface, motorParams, verbose=True)
	
	#termination
	interface.terminate()

	#<?> what is this ?
	if __name__ == "__main__":
		main()