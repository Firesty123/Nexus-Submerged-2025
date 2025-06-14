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


def Route1():
    laura.Hub_StatusLight(Color.MAGENTA)

    """ Optional - Unregulated motor """
    laura.Unregulated_AttachMotor(50,-50,50) 
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
    
    # Step 1 - Wall Squaring
    
    laura.MoveStraight_Distance(300,600,-80,False,True,Stop.BRAKE,50)
    
    # Step 2 - Move to Kelp Forest 
    
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,-300,600,Stop.BRAKE,False)
    laura.MoveStraight_Distance(400,600,755,False,True,Stop.BRAKE,0)
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,300,600,Stop.BRAKE,False)
                                
    # Step 3 - Collect Plankton Sample
    
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,800,2000,Stop.BRAKE,True)
    
    # Step 4 - Move to Seabed
    
    laura.PointTurn_Degree(True,-110,215,True,50)
    laura.MoveStraight_Distance(400,600,300,False,True,Stop.BRAKE,0)

    # Step 5 - Collect Seabed Sample
    
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,-300,600,Stop.BRAKE,False)
    laura.MoveStraight_Distance(400,600,450,False,True,Stop.BRAKE,0)
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,-500,600,Stop.BRAKE,False)
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,-700,2000,Stop.BRAKE,True)
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,700,2000,Stop.BRAKE,False)
    laura.MoveStraight_Distance(300,600,400,False,True,Stop.BRAKE,0)
    
    # Step 6 - Move to Collect Coral
    
    laura.LockTurn_Degree(True,PORT_RIGHTDRIVE,400,290,True,30)
    laura.MoveStraight_Distance(1000,600,550,False,True,Stop.BRAKE,0)

    """ Optional - Timer end """
    # print("Time used: ", timer1.time())

######################## Route testing ########################

# For individual route testing only
# Comment it when using Master Program

Route1()
