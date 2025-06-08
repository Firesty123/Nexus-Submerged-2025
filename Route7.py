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


def Route7():
    laura.Hub_StatusLight(Color.MAGENTA)

    """ Optional - Unregulated motor """
    laura.Unregulated_AttachMotor(50,-50,50)
    while not Button.CENTER in laura.Hub_ButtonPressed():
        wait(20)
    
    """ Route start """
    laura.SingleMotor_Brake(PORT_LEFTATTACH)
    laura.SingleMotor_Brake(PORT_RIGHTATTACH)
    laura.Hub_SpeakerBeep(500, 400) # wait 0.2s before start

    """ Optional - Timer start """
    # timer1 = StopWatch()
    # timer1.reset()

    """ Start your code here """ 
    #
    # Step 1 - Wall squaring 
    laura.MoveSteering_Seconds(-150, 0, 1000, True, 20)
    
    #Step 2 - Complete Change Shipping Lanes
    laura.MoveStraight_Distance(600,400,350,False,True,Stop.BRAKE,50)
    laura.LockTurn_Degree(True,PORT_LEFTDRIVE,1000,200,Stop.BRAKE,50)
    laura.MoveStraight_Distance(200,600,50,False,True,Stop.BRAKE,50)
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,1000,1500,Stop.BRAKE,True)
    
    #Note: May be inconsistent
    laura.MoveStraight_Distance(600,100,-311,False,True,Stop.BRAKE,20)
    laura.LockTurn_Degree(True,PORT_LEFTDRIVE,600,600,Stop.BRAKE,50)
    #Close Note
    
    laura.SingleMotor_BySeconds(PORT_LEFTDRIVE,1000,200,Stop.BRAKE,50)
    
    #Step 3 - Complete Sonar Discovery
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,-100,200,Stop.BRAKE,True)
    laura.MoveStraight_Distance(400,250,-550,False,True,Stop.BRAKE,200)
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,-1000,800,Stop.BRAKE,50)
    laura.MoveStraight_Distance(400,300,-250,False,True,Stop.BRAKE,200)
    laura.MoveStraight_Distance(200,100,-100,False,True,Stop.BRAKE,50)
    laura.MoveStraight_Distance(300,200,60,False,True,Stop.BRAKE,50)
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,300,1200,Stop.BRAKE,True)
    laura.MoveStraight_Distance(300,200,100,False,True,Stop.BRAKE,50)
    laura.LockTurn_Degree(True,PORT_RIGHTDRIVE,1000,80,True,50)

    #Step 4 - Go Back To Blue Base
    laura.MoveStraight_Distance(1000,900,770,False,True,Stop.BRAKE,50)
    
    """ Optional - Timer end """
    # print("Time used: ", timer1.time())

######################## Route testing ########################

# For individual route testing only
# Comment it when using Master Program

# Route7()
