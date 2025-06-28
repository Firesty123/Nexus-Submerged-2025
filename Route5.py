######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from ACL_FLL_v03 import *
laura = Laura() # create object

######################## Route parallel program ########################

# Example action
# def __Route1_Arm1():
    # laura.SingleMotor_BySeconds(PORT_LEFTATTACH, 200, 1000, Stop.BRAKE, False)
    
######################## Route program ########################

### Starting position ###
# Blue base - Align left wheel left side to 2nd Bold line from left


def Route5():
    laura.Hub_StatusLight(Color.MAGENTA)

    """ Optional - Unregulated motor """
    laura.Unregulated_AttachMotor(-60,-30, 50)
    while not Button.CENTER in laura.Hub_ButtonPressed():
        wait(20)
    
    """ Route start """
    laura.SingleMotor_Brake(PORT_LEFTATTACH)
    laura.SingleMotor_Brake(PORT_RIGHTATTACH)
    laura.Hub_SpeakerBeep(500, 200) # wait 0.2s before start

    """ Optional - Timer start """
    # timer1 = StopWatch()
    # timer1.reset()

    """ Start your code here """

    laura.MoveSteering_Degree(True,150,3,800,False,0)    
    laura.MoveSteering_Degree(True,600,3,900,True,10)
    
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,200,1000,Stop.COAST,True)
    
    laura.MoveStraight_Distance(200,200,-200,True,True,Stop.BRAKE,10)
    
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,-1000,600,Stop.BRAKE,True)
    
    laura.MoveSteering_Degree(True,-1000,5,500,True,0)
    
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,1000,600,Stop.COAST,True)
    
    laura.MoveStraight_Distance(700,600,-115,True,True,Stop.BRAKE,10)
    
    laura.LockTurn_Degree(True,PORT_RIGHTDRIVE,900,350,True,10)
    # laura.MoveSteering_Degree(True,-200,0,100,True,0)
    laura.LockTurn_Degree(True,PORT_LEFTDRIVE,900,350,True,10)
    
    laura.MoveStraight_Distance(800,600,1060,True,True,Stop.BRAKE,0)
    
    laura.LockTurn_Degree(True,PORT_RIGHTDRIVE,-900,210,True,10)
    
    laura.MoveStraight_Distance(500,400,-300,True,True,Stop.COAST,0)
    laura.MoveSteering_Degree(True,1000,0,700,True,0)
    
   
    

    """ Optional - Timer end """
    # print("Time used: ", timer1.time())

######################## Route testing ########################

# For individual route testing only
# Comment it when using Master Program

Route5()
