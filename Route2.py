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


def Route2():
    laura.Hub_StatusLight(Color.MAGENTA)

    """ Optional - Unregulated motor """
    laura.Unregulated_AttachMotor(40,40,30) 
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
    # Step 1 - Wall squaring & ...
    
    laura.MoveSteering_Seconds(-150, 0, 300, True, 200) # wall squaring
    
    laura.MoveStraight_Distance(800,600,719,True,True,Stop.BRAKE,10)

    laura.PointTurn_Degree(True,-700,180,True,10)
    

    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,-800,700,Stop.COAST,False)
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,-800,900,Stop.COAST,True)
    
    laura.MoveSteering_Seconds(200,3,500,True,10)

    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,200,900,Stop.COAST,False)
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,800,900,Stop.COAST,True)
    
    laura.MoveStraight_Distance(800,600,-100,True,True,Stop.BRAKE,0)
    
    laura.PointTurn_Degree(True,-700,60,True,0)
    
    laura.MoveSteering_Seconds(1000,-10,1500,True,0)
    

    """ Optional - Timer end """
    # print("Time used: ", timer1.time())

######################## Route testing ########################

# For individual route testing only
# Comment it when using Master Program

Route2()
