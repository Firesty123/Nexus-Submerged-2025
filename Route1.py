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


def Route1v2():
    laura.Hub_StatusLight(Color.MAGENTA)

    """ Optional - Unregulated motor """
    laura.Unregulated_AttachMotor(50,50,40) 
    while not Button.CENTER in laura.Hub_ButtonPressed():
        wait(20)
    
    """ Route start """

    """ Optional - Timer start """
    # timer1 = StopWatch()
    # timer1.reset()

    """ Start your code here """
    
    laura.SingleMotor_Brake(PORT_LEFTATTACH)
    laura.SingleMotor_Brake(PORT_RIGHTATTACH)
    
    # Step 1 - Wall squaring & ...

    laura.MoveSteering_Seconds(-150, 0, 300, True, 200)
    
    # Step 2 - Move Foward to collect 2 shrimp and 1 coral
    
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,-300,500,Stop.COAST,False)
    laura.MoveStraight_Distance(800,500,700,True,True,Stop.BRAKE,0)
    
    # laura.SingleMotor_BySeconds(PORT_LEFTATTACH,-300,500,Stop.COAST,False)
    
    laura.MoveStraight_Distance(800,500,70,False,False,Stop.BRAKE,50)
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,200,500,Stop.COAST,False)
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,-1000,1600,Stop.COAST,True)
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,1000,1600,Stop.COAST,False)
    wait(200)
    laura.PointTurn_Degree(True,-300,200,Stop.BRAKE,50)
    
    laura.MoveStraight_Distance(600,600,250,True,True,Stop.COAST,10)
    
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,-1000,540,Stop.COAST,False)
    laura.MoveSteering_Degree(True,600,10,330,Stop.BRAKE,20)

    laura.LineFollow_P_ByDegree(True,PORT_RIGHTCOLOUR,40,350,-0.4,Stop.BRAKE,20)

    laura.MoveStraight_Distance(600,600,100,False,True,Stop.BRAKE,10)
    
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,-1000,1500,Stop.COAST,True)
    
    laura.MoveStraight_Distance(800,600,110,True,True,Stop.BRAKE,10)
    
    
    
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,1000,1500,Stop.COAST,False)

    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,200,500,Stop.BRAKE,False)
    
    laura.MoveStraight_Distance(600,600,180,False,True,Stop.BRAKE,10)
    
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,-200,500,Stop.BRAKE,True)
    
    laura.MoveSteering_Degree(True,700,-60,1100,True,10)
    laura.MoveSteering_Degree(True,700,90,300,True,10)
    
    laura.SingleMotor_Brake(PORT_LEFTDRIVE)
    laura.SingleMotor_Brake(PORT_RIGHTDRIVE)

    """ Optional - Timer end """
    # print("Time used: ", timer1.time())

######################## Route testing ########################

# For individual route testing only
# Comment it when using Master Program

Route1v2()