 ######################## Pyricks library ########################

from pybricks.parameters import Color, Direction, Stop, Icon
from pybricks.tools import wait, StopWatch, Matrix

######################## Custom program ########################

from Laura_Lib import *
from Route_0 import *
from Route_1 import *

laura = Laura() #create object

######################## Total route ########################

CURRENT_ROUTE = 1
MAX_ROUTE = 1 # modify accordingly

######################## Main program ########################

while True:
    laura.Hub_DisplayNum(CURRENT_ROUTE)
    laura.Hub_StatusLight(Color.CYAN)

    if Button.LEFT in laura.Hub_ButtonPressed():
        if CURRENT_ROUTE > 0:
            CURRENT_ROUTE -= 1
        elif CURRENT_ROUTE == 0:
            CURRENT_ROUTE = MAX_ROUTE
        wait(200)

    elif Button.RIGHT in laura.Hub_ButtonPressed():
        if CURRENT_ROUTE < MAX_ROUTE:
            CURRENT_ROUTE += 1
        elif CURRENT_ROUTE == MAX_ROUTE:
            CURRENT_ROUTE = 0
        wait(200)

    elif Button.CENTER in laura.Hub_ButtonPressed():
        # add your route here
        if CURRENT_ROUTE == 0:
            Route0()
        elif CURRENT_ROUTE == 1:
            # Route1()
            pass


        # auto-run next route
        if CURRENT_ROUTE < MAX_ROUTE:
            CURRENT_ROUTE += 1

    # Unregulated motor power = 100 to -100
    else:
        if CURRENT_ROUTE == 0:
            laura.Unregulated_AttachMotor(0, 30)
        elif CURRENT_ROUTE == 1:
            laura.Unregulated_AttachMotor(-80, 30)
        elif CURRENT_ROUTE == 2:
            laura.Unregulated_AttachMotor(20, 70)

    # test push