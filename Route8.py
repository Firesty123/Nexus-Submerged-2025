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


def Route8():
    laura.Hub_StatusLight(Color.MAGENTA)

    """ Optional - Unregulated motor """
    # laura.Unregulated_AttachMotor(50,-50,50)
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
    # wall squaring
   
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,-100,1200,Stop.BRAKE,False)
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,200,2500,Stop.BRAKE,True)
    
    laura.MoveStraight_Distance(500,500,-680,True,True,Stop.BRAKE,10)
    laura.LockTurn_Degree(True,PORT_LEFTDRIVE,500,125,True,10)
    laura.MoveSteering_Seconds(-200,0,2000,Stop.COAST,10)
    laura.MoveStraight_Distance(500,500,100,True,True,Stop.BRAKE,10)
    laura.LockTurn_Degree(True,PORT_LEFTDRIVE,300,250,True,10)
    laura.MoveStraight_Distance(500,500,420,True,True,Stop.BRAKE,10)
    laura.LockTurn_Degree(True,PORT_RIGHTDRIVE,-400,200,True,10)
    laura.MoveSteering_Seconds(300,0,2000,True,10)
    laura.SingleMotor_BySeconds(PORT_RIGHTATTACH,400,1500,Stop.BRAKE,False)
    laura.SingleMotor_BySeconds(PORT_LEFTATTACH,-400,1500,Stop.BRAKE,True)
    laura.MoveSteering_Degree(True,-400,200,True,10)
    laura.LockTurn_Degree(True,PORT_LEFTDRIVE,400,30,True,10)
    laura.MoveStraight_Distance(600,300,-200,False,True)
    
    laura.MoveStraight_Distance(500,500,-200,False,True,Stop.BRAKE,50)
    laura.SingleMotor_Brake(PORT_LEFTDRIVE)
   
    """ Optional - Timer end """
    # print("Time used: ", timer1.time())


######################## Route testing ########################

# For individual route testing only
# Comment it when using Master Program

Route8()