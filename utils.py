import brickpi
import time
from math import pi

class RobotUtility:
  #constructor
  def __init__(self):
    self.WHEEL_RADIUS = 1.5
    self.ROBOT_RADIUS = 5.5
    self.PERC_MOD_WHEEL = 1 #init
    self.PERC_MOD_BOOST = 1 #init 
    self.DEGS = 0

  #set configurations from callibration result 
  def set_drift_callibration (self,mode_wheel,boost,degs):
    self.PERC_MOD_WHEEL = mdoel_wheel 
    self.PERC_MOD_BOOST = boost
    self.DEGS = degs 




# WHEEL_RADIUS = 1.5
# ROBOT_RADIUS = 5.0

# motors = [0,1]

# interface = brickpi.Interface()
# interface.initialize()
# interface.motorEnable(motors[0])
# interface.motorEnable(motors[1])
# motorParam0 = interface.MotorAngleControllerParameters()
# motorParam1 = interface.MotorAngleControllerParameters()  

# motorParam0.maxRotationAcceleration = 7.0
# motorParam0.maxRotationSpeed = 12.0
# motorParam0.feedForwardGain = 255/20.0
# motorParam0.minPWM = 18.0
# motorParam0.pidParameters.minOutput = -255
# motorParam0.pidParameters.maxOutput = 255
# motorParam0.pidParameters.k_p = 20.0
# motorParam0.pidParameters.k_i = 0.0
# motorParam0.pidParameters.k_d = 0.0
  
# motorParam1.maxRotationAcceleration = 7.0 
# motorParam1.maxRotationSpeed = 12.0
# motorParam1.feedForwardGain = 255/20.0
# motorParam1.minPWM = 18.0
# motorParam1.pidParameters.minOutput = -255
# motorParam1.pidParameters.maxOutput = 255 
# motorParam1.pidParameters.k_p = 20.0
# motorParam1.pidParameters.k_i = 0.0 
# motorParam1.pidParameters.k_d = 0.0 




# '''Move distance cm forward'''
# def move(distance):
#   interface.setMotorAngleControllerParameters(motors[0],motorParam0)
#   interface.setMotorAngleControllerParameters(motors[1],motorParam1)

#   interface.increaseMotorAngleReferences(motors,[distance/WHEEL_RADIUS,distance/WHEEL_RADIUS])
  
#   while not interface.motorAngleReferencesReached(motors) :
#     motorAngles = interface.getMotorAngles(motors)
#     if motorAngles :
#       print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]

#My intergration of move forward 
def move (distance)(self,distance,interface ,motorParams,verbose=True):
  motors = [0,1]
  # to control the motor angle correctly ,
  #we need set up motor angle control parameters to each motor , the parametar are pre defined above 
  interface.setMotorAngleControllerParameters(0,motorParam0)
  interface.setMotorAngleControllerParameters(0.motorParam1)

  # set target by using equation (?)
  interface.increaseMotorAngleReferences(motors, [(distance * self.PERC_MOD_BOOST)]/self.WHEEL_RADIUS,self.PERC_MOD_WHEEL * distance * self.PERC_MOD_BOOST/self.WHEEL_RADIUS)

  #start process to approach the target by using While Not 
  while not interface.motorAngleReferencesReached (motors) :
    motorAngles = interface.getMotorAngles([0,1])
    if motorAngles  and verbose :
      print "motor angles :" , motorAngles[0][0],",",motorAngles[1][0]

  while not interface.motorAngleReferencesReached
'''Rotate radians clockwise'''
def rotate(radians):
  motors 0,1
  interface.setMotorAngleControllerParameters(motors[0],motorParam0)
  interface.setMotorAngleControllerParameters(motors[1],motorParam1)
  
  #angle = ROBOT_RADIUS * pi / WHEEL_RADIUS 
  #my implementation of angle 
  radiance = radiance + self.DEGS * pi / 180 #add up two raidicance gives final radiance  <?>then what is self.DEG?
  angle = self.ROBOT_RADIUS * radiance / self.WHEEL_RADIUS #<?> what does this equation comes from? 

  interface.increaseMotorAngleReferences(motors, [angle, -angle])
 
  while not interface.motorAngleReferencesReached(motors) :
    motorAngles = interface.getMotorAngles(motors)
    if motorAngles :
      print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]

