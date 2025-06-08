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
    # laura.Unregulated_AttachMotor(50,-50,50) 
    # while not Button.CENTER in laura.Hub_ButtonPressed():
    #     wait(20)
    
    """ Route start """
    laura.MoveSteering_Seconds(-150, 0, 300, True, 200)
    
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,-500,800,Stop.BRAKE,False)
    laura.MoveStraight_Distance(400,400,750,False,True,Stop.BRAKE,50)
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,500,600,Stop.BRAKE,False)
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,600,2000,Stop.BRAKE,True)
    
    laura.PointTurn_Degree(True,-310,30,False,500)
    
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,500,600,Stop.BRAKE,True)
    laura.MoveStraight_Distance(400,400,780,False,True,Stop.BRAKE,50)
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,-1000,2000,Stop.BRAKE,True)
    laura.MoveStraight_Distance(400,400,330,False,False,Stop.BRAKE,50)
    wait(100)
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,1000,2000,Stop.BRAKE,True)
    #laura.SingleMotor_BySeconds(PORT_LEFTATTACH,300,500,Stop.BRAKE,False)
    laura.LockTurn_Degree(True,PORT_RIGHTDRIVE,700,180,Stop.BRAKE,50)
    laura.MoveSteering_Degree(True,700,-18,1300,Stop.COAST,20)
    
    laura.SingleMotor_Brake(PORT_LEFTDRIVE)
    laura.SingleMotor_Brake(PORT_RIGHTDRIVE)

    """ Optional - Timer start """
    # timer1 = StopWatch()
    # timer1.reset()

    """ Start your code here """
    # Step 1 - Wall squaring & ...
    laura.MoveStraight_Distance(400,500,700,False,True,Stop.BRAKE,200)
    

    """ Optional - Timer end """
    # print("Time used: ", timer1.time())

######################## Route testing ########################

# For individual route testing only
# Comment it when using Master Program

#Route1()