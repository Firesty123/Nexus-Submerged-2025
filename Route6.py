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


def Route6():
    laura.Hub_StatusLight(Color.MAGENTA)

    """ Optional - Unregulated motor """
    # laura.Unregulated_AttachMotor(-50,-50,50)
    # while not Button.CENTER in laura.Hub_ButtonPressed():
    #     wait(20)
    
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
    
    laura.MoveStraight_Distance(800,400,275,False,True,Stop.BRAKE,10)
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,300,1000,Stop.COAST,False)
    laura.LockTurn_Degree(True,PORT_RIGHTDRIVE,600,410,Stop.BRAKE,10)
    laura.MoveStraight_Distance(300,300,100,False,True,Stop.BRAKE,10)
    
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,-1000,900,Stop.COAST,True)
    
    laura.MoveStraight_Distance(500,400,270,False,True,Stop.BRAKE,10)

    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,500,500,Stop.BRAKE,True)
    wait(50)
    laura.MoveStraight_Distance(700,700,250,False,True,Stop.BRAKE,20)
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,-500,500,Stop.BRAKE,True)
    
    laura.LockTurn_Degree(True,PORT_RIGHTDRIVE,500,150,Stop.BRAKE,20)
    
    laura.MoveSteering_Degree(True,-800,60,1900,Stop.COAST,10)

    
    laura.SingleMotor_Brake(PORT_RIGHTDRIVE)
    laura.SingleMotor_Brake(PORT_LEFTDRIVE)

    """ Optional - Timer end """
    # print("Time used: ", timer1.time())

######################## Route testing ########################

# For individual route testing only
# Comment it when using Master Program

#Route6()
