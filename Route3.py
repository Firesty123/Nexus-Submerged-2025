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


def Route3():
    laura.Hub_StatusLight(Color.MAGENTA)

    """ Optional - Unregulated motor """
    laura.Unregulated_AttachMotor(50,50,50)
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
    # Step 1 - Wall squaring & Move to Ship
    laura.MoveSteering_Seconds(-150, 0, 300, True, 100) # wall squaring
    laura.MoveStraight_Distance(610,550,600,False,True,Stop.BRAKE,50)
    laura.PointTurn_Angle(True,400,300,90,True,Stop.BRAKE,50)
    
    #Step 2 - Collect the Chest & Lift Ship Up
    
    laura.MoveStraight_Distance(500,400,100,False,True,Stop.BRAKE,50)
    laura.MoveSteering_Seconds(100,0,1095 ,Stop.COAST,50)
    
    #Step 3 - Move to Shark and Coral
    
    laura.MoveStraight_Distance(400,200,-156,False,True,Stop.BRAKE,100)
    laura.PointTurn_Angle(True,-600,550,90,True,Stop.BRAKE,50)
    laura.MoveSteering_Seconds(-400,0,1500,Stop.COAST,50)
    
    wait(50)
    
    #Step 4 - Press Shark Down and Put 
    
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,-700,700,Stop.COAST,False)
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,-1000,1000,Stop.COAST,True)
    
    wait(50)
    
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,800,500,Stop.BRAKE,False)
    laura.MoveSteering_Seconds(300,0,250,Stop.BRAKE,True)
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,100,1000,Stop.BRAKE,True)
    
    #Step 5 - Return to Base
    
    laura.MoveSteering_Seconds(50,0,2000,Stop.BRAKE,True)
    laura.MoveSteering_Degree(True,900,8,1550,Stop.COAST,50)
    
    laura.SingleMotor_Brake(PORT_LEFTDRIVE)
    laura.SingleMotor_Brake(PORT_RIGHTDRIVE)
    
    """ Optional - Timer end """
    # print("Time used: ", timer1.time())

######################## Route testing ########################

# For individual route testing only
# Comment it when using Master Program

Route3()
