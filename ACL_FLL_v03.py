"""  

---- Disclaimer ----

Filename - ACL_FLL_v03.py
Pybricks firmware - v3.5.0 (Pybricks Code v2.5.1)
Tested on - Laura 3

1 - This code library is developed for Assassins Robotics students & coaches usage only.
2 - This code library was tested on and to be paired with Laura.
3 - Any modifications to the robot base & code library are not encouraged and the results will not be optimsed.
4 - Should you found any bugs or ideas for improvement, feel free to consult respective Assassins Robotics coaches.

Think Like Champion, Work Like Champion, Play Like Champion

© 2024 Assassins Mecha Sdn Bhd.

"""

######################## Pyricks library ########################

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


######################## Define variable ########################

pi = 3.1415926535897

WHEEL_SIZE = 61 # Measuerement in milimeter
WHEEL_SPACING = 145 #160

STR_SPEED = 400
STR_ACCEL = 400
TURN_SPEED = 300
TURN_ACCEL = 300
ARM_SPEED = 300

PORT_LEFTDRIVE = "LD"
PORT_RIGHTDRIVE = "RD"
PORT_LEFTATTACH = "LA"
PORT_RIGHTATTACH = "RA"
PORT_LEFTCOLOUR = "LC"
PORT_RIGHTCOLOUR = "RC"

BLACK = 5
WHITE = 40
THRESHOLD = (WHITE - BLACK) / 2

######################## Hub & Port setup ########################

# Robot type - Laura 3
hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
left_colour = ColorSensor(Port.A)
right_colour = ColorSensor(Port.B)
left_attach = Motor(port=Port.C, positive_direction=Direction.CLOCKWISE, gears=[12,20])
right_attach = Motor(port=Port.D, positive_direction=Direction.CLOCKWISE, gears=[12,20])
left_drive = Motor(port=Port.E, positive_direction=Direction.COUNTERCLOCKWISE)
right_drive = Motor(port=Port.F, positive_direction=Direction.CLOCKWISE)
drive_base = DriveBase(left_drive, right_drive, WHEEL_SIZE, WHEEL_SPACING)
hub.system.set_stop_button([Button.BLUETOOTH])
left_drive.control.limits(speed=1000, acceleration=600, torque=500)
right_drive.control.limits(speed=1000, acceleration=600, torque=500)
left_drive.settings(max_voltage=9000)
right_drive.settings(max_voltage=9000)

######################## Hub Display ########################

class Laura():

    """ Hub display / controls """

    def Hub_StatusLight(self, colour):
        '''
        Set hub button LED colour\n
        - [Colour] Set the button colour (eg Color.RED)\n
        '''
        hub.light.on(colour)

    def Hub_StatusBlink(self, colour, duration):
        '''
        Set hub button LED to start blinking\n
        - [Colour] Set the button colour (eg Color.RED)\n
        - [Duration:list] Set the blinking interval (eg [200, 200] in ms)\n
        '''
        hub.light.blink(colour, duration)

    def Hub_DisplayNum(self, number):
        '''
        Display number on hub\n
        - [Number:int] Set the number (0 to 99)\n
        '''
        hub.display.number(number)

    def Hub_DisplayIcon(self, icon):
        '''
        Display icon on hub\n
        - [Icon] Set the icon (eg ICON.CIRCLE)\n
        '''
        hub.display.icon(icon)

    def Hub_DisplayPixel(self, row, column, brightness):
        '''
        Turn on specific hub LED\n
        - [Row:int] Set the LED row (0 to 4)\n
        - [Column:int] Set the LED column (0 to 4)\n
        - [Brightness:int] Set the LED brightness (0% to 100%)\n
        '''
        hub.display.off()
        hub.display.pixel(row, column, brightness)

    def Hub_SpeakerBeep(self, frequency, duration):
        '''
        Play a beep/tone\n
        - [Frequency:int] Set the beep/tone (64 to 24000 Hz)\n
        - [Duration:int] How long the beep/tone last (ms)\n
        '''
        hub.speaker.beep(frequency, duration)

    def Hub_Shutdown(self):
        '''
        Turn off the hub
        '''
        hub.display.icon(Icon.CIRCLE)
        wait(100)
        hub.speaker.play_notes(["C4/16", "C3/16", "C2/16"])
        hub.system.shutdown()

    def Hub_ButtonPressed(self):
        '''
        Return button pressed
        '''
        return hub.buttons.pressed()

    """ Port view / check tools """

    def PortView_ReflectedLight(self, interval):
        '''
        Measure reflected light value\n
        - [Interval:int] Duration between each reading updates (ms)\n
        '''
        print("---- Reflected Value ----")
        while True: 
            normalised_left = ((left_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            normalised_right = ((right_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            print("Reflected(left): ", left_colour.reflection(), "| Reflected(right): ", right_colour.reflection(), "| Normalised(left): ", normalised_left , "| Normalised(right): ", normalised_right)
            wait(interval)

    def PortView_HSV(self, interval):
        '''
        Measure HSV value\n
        - [Interval:int] Duration between each reading updates (ms)\n
        '''
        print("---- HSV Value ----")
        while True:
            print("HSV(left): ", left_colour.hsv(), "| HSV(right): ", right_colour.hsv())
            wait(interval)

    def PortView_Battery(self):
        '''
        Measure battery left on hub\n
        '''
        print("---- Hub battery info ----")
        print("Hub battery voltage: ", hub.battery.voltage(), "mV")
        print("Hub battery current: ", hub.battery.current(), "mA")
        print(" ")

    def PortView_MotorAngle(self, interval):
        '''
        Measure motor degree\n
        - [Interval:int] Duration between each reading updates (ms)\n
        '''
        print("---- Motor angle ----")
        while True:
            print("LeftDrive: ", left_drive.angle(), "| RightDrive: ", right_drive.angle(), "| Arm1: ", left_attach.angle(), "| Arm2: ", right_attach.angle())
            wait(interval)

    def PortView_MotorLoad(self, motorPower, interval):
        '''
        Measure motor load\n
        - [MotorPower:int] Set the testing motor power (-100 to 100)\n
        - [Interval:int] Duration between each reading updates (ms)\n
        '''
        print("---- Motor load ----")
        while True:
            left_drive.dc(motorPower)
            right_drive.dc(motorPower)
            left_attach.dc(motorPower)
            right_attach.dc(motorPower)
            print("LeftDrive: ", left_drive.load(), "| RightDrive: ", right_drive.load(), "| Arm1: ", left_attach.load(), "| Arm2: ", right_attach.load())
            wait(interval)

    def PortView_MotorSpeed(self, motorSpeed, interval):
        '''
        Measure motor speed\n
        - [MotorSpeed:int] Set the testing motor speed (-1000 to 1000)\n
        - [Interval:int] Duration between each reading updates (ms)\n
        '''
        print("---- Motor speed ----")
        while True:
            left_drive.run(motorSpeed)
            right_drive.run(motorSpeed)
            left_attach.run(motorSpeed)
            right_attach.run(motorSpeed)
            print("LeftDrive: ", left_drive.speed(), "| RightDrive: ", right_drive.speed(), "| Arm1: ", left_attach.speed(), "| Arm2: ", right_attach.speed())
            wait(interval)        

    """ Single motor """

    def SingleMotor_On(self, port, speed):
        '''
        Single motor run forever\n
        - [Port] Set the motor port (eg PORT_LEFTDRIVE)\n
        - [Speed:int] Set the motor speed (-1000 to 1000)\n
        '''
        if port == "LA":
            left_attach.run(speed)
        elif port == "RA":
            right_attach.run(speed)
        elif port == "LD":
            left_drive.run(speed)
        elif port == "RD":
            right_drive.run(speed)
        else:
            raise TypeError("Invalid Port")

    def SingleMotor_BySeconds(self, port, speed, duration, stopMethod, waitForComplete):
        '''
        Single motor run by seconds\n
        - [Port] Set the motor port (eg PORT_LEFTDRIVE)\n
        - [Speed:int] Set the motor speed (-1000 to 1000)\n
        - [Duration:int] How long the motor run (ms)\n
        - [StopMethod] How the motor stop after complete (eg Stop.BRAKE)\n
        - [WaitForComplete:bool] Wait for this command to complete before next step (True/False)\n
        '''
        if port == "LA":
            left_attach.run_time(speed, duration, stopMethod, waitForComplete)
        elif port == "RA":
            right_attach.run_time(speed, duration, stopMethod, waitForComplete)
        elif port == "LD":
            left_drive.run_time(speed, duration, stopMethod, waitForComplete)
        elif port == "RD":
            right_drive.run_time(speed, duration, stopMethod, waitForComplete)
        else:
            raise TypeError("Invalid Port")

    def SingleMotor_ByDegree(self, port, resetDegree, speed, degree, stopMethod, waitForComplete):
        '''
        Single motor run by seconds\n
        - [Port] Set the motor port (eg PORT_LEFTDRIVE)\n
        - [ResetDegree:bool] Reset accumulated motor degree (True/False)\n
        - [Speed:int] Set the motor speed (-1000 to 1000)\n
        - [Duration:int] How long the motor run (ms)\n
        - [StopMethod] How the motor stop after complete (eg Stop.BRAKE)\n
        - [WaitForComplete:int] Complete this action before next step (True/False)\n
        '''
        if port == "LA":
            if resetDegree == True:
                left_attach.reset_angle(0)
            left_attach.run_angle(speed, degree, stopMethod, waitForComplete)
        elif port == "RA":
            if resetDegree == True:
                right_attach.reset_angle(0)
            right_attach.run_angle(speed, degree, stopMethod, waitForComplete)
        elif port == "LD":
            if resetDegree == True:
                left_drive.reset_angle(0)
            left_drive.run_angle(speed, degree, stopMethod, waitForComplete)
        elif port == "RD":
            if resetDegree == True:
                right_drive.reset_angle(0)
            right_drive.run_angle(speed, degree, stopMethod, waitForComplete)
        else:
            raise TypeError("Invalid Port")

    def SingleMotor_Brake(self, port):
        '''
        Single motor stop running\n
        [Port] Set the motor port (eg PORT_LEFTDRIVE)\n
        '''
        if port == "LA":
            left_attach.brake()
        elif port == "RA":
            right_attach.brake()
        elif port == "LD":
            left_drive.brake()
        elif port == "RD":
            right_drive.brake()
        else:
            raise TypeError("Invalid Port")

    """ FLL custom feature """
    
    def Unregulated_AttachMotor(self, leftPower, rightPower, loadLimit):
        '''
        Unregulated motor running for installing attachment\n
        - [LeftPower:int] Set the power for left attach motor (-100 to 100)\n
        - [RightPower:int] Set the power for right attach motor (-100 to 100)\n
        - [LoadLimit:int] Motor load limit to stop motor rotate (0 to 100)
        '''
        if abs(left_attach.load()) > loadLimit:
            left_attach.stop()
            wait(20)
        elif abs(right_attach.load()) > loadLimit:
            right_attach.stop()
            wait(20)
        else:
            left_attach.dc(leftPower)
            right_attach.dc(rightPower)
            wait(20)
    
    def PortView_MotorPairing(self, speed, power, useSpeed, duration, interval, cycle):
        '''
        Measure & compare both motors for pairing\n
        - [Speed:int] Set motor speed (-1000 to 1000)\n
        - [Power:int] Set motor power (-100 to 100)\n
        - [UseSpeed:bool] Start motor with speed or power (True/False)\n
        - [Duration:int] How long for the motors run (ms)\n
        - [Interval:int] Duration between each reading updates (ms)\n
        - [Cycle: int] How many times for the sampling cycle\n
        '''
        # Release motor limits to max value
        left_drive.settings(max_voltage=9000)
        right_drive.settings(max_voltage=9000)
        left_drive.control.limits(speed=1000, acceleration=2000, torque=560)
        right_drive.control.limits(speed=1000, acceleration=2000, torque=560)
        leftLimits = left_drive.control.limits()
        rightLimits = right_drive.control.limits()
        leftVoltage = left_drive.settings()
        rightVoltage = right_drive.settings()

        print("--- Motor settings for maximum speed, acceleration, torque & voltage ---")
        print(f"Left Motor - Speed: {leftLimits[0]}deg/s, Acceleration: {leftLimits[1]}deg/s², Torque: {leftLimits[2]}mNm, Voltage: {leftVoltage[0]}mV")
        print(f"Right Motor - Speed: {rightLimits[0]}deg/s, Acceleration: {rightLimits[1]}deg/s², Torque: {rightLimits[2]}mNm, Voltage: {rightVoltage[0]}mV")
        print("")

        # Choose motor run mode (speed / power) and get values
        leftAverageSpeed = rightAverageSpeed = 0
        leftAverageTorque = rightAverageTorque = 0
        loop = 0
        print("--- Motor value ---")
        for x in range (cycle):
            if useSpeed == True:
                left_drive.run(speed)
                right_drive.run(speed)
            else:
                left_drive.dc(power)
                right_drive.dc(power)
            timerMP = StopWatch()
            timerMP.reset()
            while timerMP.time() < duration:
                loop += 1
                leftMotorStatus = left_drive.model.state()
                rightMotorStatus = right_drive.model.state()
                print(f"Left Motor - Speed: {leftMotorStatus[1]}deg/s, Torque: {left_drive.load()} mNm, Current: {leftMotorStatus[2]}mA")
                print(f"Right Motor - Speed: {rightMotorStatus[1]}deg/s, Torque: {right_drive.load()} mNm, Current: {rightMotorStatus[2]}mA")
                print("")
                leftAverageSpeed += leftMotorStatus[1]
                rightAverageSpeed += rightMotorStatus[1]
                leftAverageTorque = leftAverageTorque + left_drive.load()
                rightAverageTorque = rightAverageTorque + right_drive.load()
                wait(interval)
                
            left_drive.stop()
            right_drive.stop()
            wait(500)

        print("--- Motor average value ---")
        leftAverageSpeed = leftAverageSpeed / loop
        rightAverageSpeed = rightAverageSpeed / loop
        leftAverageTorque = leftAverageTorque / loop
        rightAverageTorque = rightAverageTorque / loop
        print(f"Left Motor - Average Speed: {leftAverageSpeed}deg/s, Average load: {leftAverageTorque}mMm")
        print(f"Right Motor - Average Speed: {rightAverageSpeed}deg/s, Average load: {rightAverageTorque}mMm")

        # Handicap motor settings to optimum value
        left_drive.control.limits(speed=1000, acceleration=600, torque=500)
        right_drive.control.limits(speed=1000, acceleration=600, torque=500)

    """ Drive base movements """

    def MoveSteering_Seconds(self, speed, steering, duration, stop, settlingTime):
        '''
        Robot move steering by seconds\n
        - [Speed:int] Set robot FW/BW speed (-1000 to 1000)\n
        - [Steering:int] Set robot turn rate (-100 to 100)\n
        - [Duration:int] How much seconds to move (ms)\n
        - [Stop:bool] Stop after reaching duration (True/False)\n
        - [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        drive_base.drive(speed, steering)
        wait(duration)
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def MoveSteering_Degree(self, resetDegree, speed, steering, degree, stop, settlingTime):
        '''
        Robot move steering by degree\n
        - [ResetDegree:bool] Reset accumulated degree (True/False)\n
        - [Speed:int] Set robot FW/BW speed (-1000 to 1000)\n
        - [Steering:int] Set robot turn rate (-100 to 100)\n
        - [Degree:int] How much degree to move (+ve)\n
        - [Stop:bool] Stop after reaching degree (True/False)\n
        - [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        distance_driven = 0
        if resetDegree == True:
            left_drive.reset_angle(0)
            right_drive.reset_angle(0)
        while distance_driven < degree:
            distance_driven = (abs(left_drive.angle()) + abs(right_drive.angle())) / 2
            drive_base.drive(speed, steering)
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def MoveStraight_Distance(self, speed, accel, distance, useGyro, waitForComplete, stopMethod, settlingTime):
        '''
        Robot move straight by distance\n
        - [Speed:int] Set robot FW/BW speed (0 to 1000)\n
        - [Accel:int] Set robot acceleration rate (0 to 600)\n
        - [Distance:int] How much distance to move (+ve/-ve mm)\n
        - [UseGyro:bool] Use gyro to assist straight (True/False)\n
        - [WaitForComplete:bool] Complete this action before next step (True/False)\n
        - [StopMethod] How to stop robot (eg Stop.BRAKE)\n
        - [SettlingTime:int] Wait interval before next step (ms)
        '''
        drive_base.reset()
        drive_base.use_gyro(useGyro)
        drive_base.settings(speed, accel, TURN_SPEED, TURN_ACCEL)
        drive_base.straight(distance, stopMethod, waitForComplete)
        hub.speaker.beep(500, settlingTime)

    def MoveCurve_Angle(self, speed, accel, radius, angle, waitForComplete, stopMethod, settlingTime):
        '''
        Robot move along curve arc by angle\n
        - [Speed:int] Set robot FW/BW speed (0 to 1000)\n
        - [Accel:int] Set robot acceleration rate (0 to 600)\n
        - [Radius:int] Set the turning arc radius (+ve mm)\n
        - [Angle:int] Moving angle based on arc radius (+ve/-ve)\n
        - [WaitForComplete:bool] Complete this action before next step (True/False)\n
        - [StopMethod] How to stop robot (eg Stop.BRAKE)\n
        - [SettlingTime:int] Wait interval before next step (ms)
        '''
        drive_base.reset()
        drive_base.use_gyro(True)
        drive_base.settings(speed, accel, TURN_SPEED, TURN_ACCEL)
        drive_base.curve(radius, angle, stopMethod, waitForComplete)
        hub.speaker.beep(500, settlingTime)
    
    def LockTurn_Seconds(self, port, speed, duration, stop, settlingTime):
        '''
        Lock Turn by seconds\n
        - [Port] Set the motor port (eg PORT_LEFTDRIVE)\n
        - [Speed:int] Set the turning speed (-1000 to 1000)\n
        - [Duration:int] How long the motor run (ms)\n
        - [Stop:bool] Stop the motor after complete (True/False)\n
        - [SettlingTime:int] Wait interval before next step (ms)
        '''
        timerLT = StopWatch()
        timerLT.reset()
        while timerLT.time() < duration:
            if port == 'LD':
                right_drive.brake()
                left_drive.run(speed)
            elif port == 'RD':
                left_drive.brake()
                right_drive.run(speed)
            else:
                raise TypeError("Invalid Port") 
        if stop == True:
            drive_base.brake()  
            hub.speaker.beep(500, settlingTime)
    
    def LockTurn_Degree(self, resetDegree, port, speed, degree, stop, settlingTime):
        '''
        Lock Turn by degree\n
        [ResetDegree:bool] Reset accumulated degree (True/False)\n
        [Port] Set the motor port (eg PORT_LEFTDRIVE)\n
        [Speed:int] Set the turning speed (-1000 to 1000)\n
        [Degree:int] How much degree to move (+ve)\n
        [Stop:bool] Stop the motor after complete (True/False)\n
        [SettlingTime:int] Wait interval before next step (ms)
        '''
        distance_driven = 0
        if resetDegree == True:
            if port == 'LD':
                left_drive.reset_angle(0)
            elif port == 'RD':
                right_drive.reset_angle(0)
        while distance_driven < degree:
            if port == 'LD':
                distance_driven = abs(left_drive.angle())
                right_drive.brake()
                left_drive.run(speed)
            elif port == 'RD':
                distance_driven = abs(right_drive.angle())
                left_drive.brake()
                right_drive.run(speed)
            else:
                raise TypeError("Invalid Port") 
        if stop == True:
            drive_base.brake()  
            hub.speaker.beep(500, settlingTime)

    def LockTurn_Angle(self, resetAngle:bool, port, speed:int, angle:int, stop:bool, settlingTime:int):
        '''
        Lock Turn by gyro angle\n
        - [ResetAngle:bool] Reset accumulated angle (True/False)\n
        - [Port] Set the motor port (eg PORT_LEFTDRIVE)\n
        - [Speed:int] Set the turning speed (-1000 to 1000)\n
        - [Angle:int] How much turning angle (+ve)\n
        - [Stop:bool] Stop the motor after complete (True/False)\n
        - [SettlingTime:int] Wait interval before next step (ms)
        '''
        robot_angle = 0
        if resetAngle == True:
            hub.imu.reset_heading(0)
        while robot_angle < angle:
            robot_angle = abs(hub.imu.heading())
            print("Angle = ", robot_angle)
            if port == 'LD':
                right_drive.brake()
                left_drive.run(speed)
            elif port == 'RD':
                left_drive.brake()
                right_drive.run(speed)
            else:
                raise TypeError("Invalid Port") 
        if stop == True:
            drive_base.brake()  
            hub.speaker.beep(500, settlingTime)

    def PointTurn_Seconds(self, speed, duration, stop, settlingTime):
        '''
        Point Turn by seconds\n
        - [Speed:int] Set the turning speed (-600 to 600)\n
        - [Duration:int] How long the motor run (ms)\n
        - [Stop:bool] Stop the motor after complete (True/False)\n
        - [SettlingTimeLint] Wait interval before next step (ms)
        '''
        timerPT = StopWatch()
        timerPT.reset()
        while timerPT.time() < duration:
            left_drive.run(speed)
            right_drive.run(-speed)
            wait(10)
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def PointTurn_Degree(self, resetDegree, speed, degree, stop, settlingTime):
        '''
        Point Turn by degree\n
        - [ResetDegree:bool] Reset accumulated degree (True/False)\n
        - [Speed:int] Set the turning speed (-600 to 600)\n
        - [Degree:int] How much degree to move (+ve)\n
        - [Stop:int] Stop the motor after complete (True/False)\n
        - [SettlingTime:int] Wait interval before next step (ms)
        '''
        distance_driven = 0
        if resetDegree == True:
            left_drive.reset_angle(0)
            right_drive.reset_angle(0)
        while distance_driven < degree:
            distance_driven = (abs(left_drive.angle()) + abs(right_drive.angle())) / 2
            left_drive.run(speed)
            right_drive.run(-speed)
            wait(10)
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def PointTurn_Angle(self, resetAngle, turnSpeed:int, turnAccel:int, angle:int, waitForComplete:bool, stopMethod, settlingTime:int):
        '''
        Point Turn by gyro angle\n
        - [ResetAngle:bool] Reset accumulated angle (True/False)\n
        - [TurnSpeed:int] Set the motor speed (-600 to 600)\n
        - [TurnAccel:int] Set the motor acceleration rate (0 to 600)\n
        - [Angle:int] How much turning angle (+ve)\n
        - [WaitForComplete:bool] Complete this action before next step (True/False)\n
        - [Stop:bool] Stop the motor after complete (True/False)\n
        - [StopMethod] How to stop robot (eg Stop.BRAKE)\n
        - [SettlingTime:int] Wait interval before next step (ms)
        '''
        if resetAngle == True:
            hub.imu.reset_heading(0)
        drive_base.reset()
        drive_base.use_gyro(True)
        drive_base.settings(STR_SPEED, STR_ACCEL, turnSpeed, turnAccel)
        drive_base.turn(angle, stopMethod, waitForComplete)
        hub.speaker.beep(500, settlingTime)

    """ Colour Sensing """

    def LineDetection_Colour_Steering(self, sensorPort, speed, steering, colour, stop, settlingTime):
        '''
        Line detection by colour \n
        - [SensorPort] Set the sensor port (eg PORT_LEFTCOLOUR)\n
        - [Speed:int] Set robot FW/BW speed (-1000 to 1000)\n
        - [Steering:int] Set robot turn rate (-100 to 100)\n
        - [Colour] Set the button colour (eg Color.RED)\n
        - [Stop:bool] Stop after reaching degree (True/False)\n
        - [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        if sensorPort == "LC":
            while not left_colour.color() == colour:
                drive_base.drive(speed, steering)
                wait(10)
        elif sensorPort == "RC":
            while not right_colour.color() == colour:
                drive_base.drive(speed, steering)
                wait(10)
        else:
            raise TypeError("Invalid Port")
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def LineDetection_Dark_Steering(self, sensorPort, speed, steering, threshold, stop, settlingTime):
        '''
        Line detection by reflected light dark \n
        [SensorPort] Set the sensor port (eg PORT_LEFTCOLOUR)\n
        [Speed:int] Set robot FW/BW speed (-1000 to 1000)\n
        [Steering:int] Set robot turn rate (-100 to 100)\n
        [Threshold:int] Set the threshold value (0 to 100)\n
        [Stop:bool] Stop after reaching degree (True/False)\n
        [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        normalised = 50
        reflected = 100
        drive_base.reset()
        while normalised > threshold:
            if sensorPort == "LC":
                reflected = left_colour.reflection()  
                normalised = ((reflected - BLACK) / (WHITE - BLACK)) * 100
            elif sensorPort == "RC":
                reflected = right_colour.reflection()
                normalised = ((reflected - BLACK) / (WHITE - BLACK)) * 100
            else:
                raise TypeError("Invalid Port")
            drive_base.drive(speed, steering)
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def LineDetection_Bright_Steering(self, sensorPort, speed, steering, threshold, stop, settlingTime):
        '''
        Line detection by reflected light bright \n
        - [SensorPort] Set the sensor port (eg PORT_LEFTCOLOUR)\n
        - [Speed:int] Set robot FW/BW speed (-1000 to 1000)\n
        - [Steering:int] Set robot turn rate (-100 to 100)\n
        - [Threshold:int] Set the threshold value (0 to 100)\n
        - [Stop:bool] Stop after reaching degree (True/False)\n
        - [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        normalised = 50
        reflected = 0
        drive_base.reset()
        while normalised < threshold:
            if sensorPort == "LC":
                reflected = left_colour.reflection()
                normalised = ((reflected - BLACK) / (WHITE - BLACK)) * 100 
            elif sensorPort == "RC":
                reflected = right_colour.reflection()
                normalised = ((reflected - BLACK) / (WHITE - BLACK)) * 100
            else:
                raise TypeError("Invalid Port")
            drive_base.drive(speed, steering)
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)
    
    def LineDetection_Dark_LockTurn(self, sensorPort, motorPort, speed, threshold, stop, settlingTime):
        '''
        Line detection by reflected light dark (Lock Turn) \n
        - [SensorPort] Set the sensor port (eg PORT_LEFTCOLOUR)\n
        - [MotorPort] Set the motor port (eg PORT_LEFTDRIVE)\n
        - [Speed:int] Set robot FW/BW speed (-1000 to 1000)\n
        - [Threshold:int] Set the threshold value (0 to 100)\n
        - [Stop:int] Stop after reaching degree (True/False)\n
        - [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        normalised = 50
        reflected = 100
        while normalised > threshold:
            if sensorPort == "LC":
                reflected = left_colour.reflection()
            elif sensorPort == "RC":
                reflected = right_colour.reflection()
            normalised = ((reflected - BLACK) / (WHITE - BLACK)) * 100
            if motorPort == "LD":
                right_drive.brake()
                left_drive.run(speed)
                wait(10)
            elif motorPort == "RD":
                left_drive.brake()
                right_drive.run(speed)
                wait(10)
            else:
                raise TypeError("Invalid Port")
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def LineDetection_Bright_LockTurn(self, sensorPort, motorPort, speed, threshold, stop, settlingTime):
        '''
        Line detection by reflected light bright (Lock Turn) \n
        - [SensorPort] Set the sensor port (eg PORT_LEFTCOLOUR)\n
        - [MotorPort] Set the motor port (eg PORT_LEFTDRIVE)\n
        - [Speed:int] Set robot FW/BW speed (-1000 to 1000)\n
        - [Threshold:int] Set the threshold value (0 to 100)\n
        - [Stop:bool] Stop after reaching degree (True/False)\n
        - [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        normalised = 50
        reflected = 0
        while normalised > threshold:
            if sensorPort == "LC":
                reflected = left_colour.reflection()
            elif sensorPort == "RC":
                reflected = right_colour.reflection()
            normalised = ((reflected - BLACK) / (WHITE - BLACK)) * 100
            if motorPort == "LD":
                right_drive.brake()
                left_drive.run(speed)
                wait(10)
            elif motorPort == "RD":
                left_drive.brake()
                right_drive.run(speed)
                wait(10)
            else:
                raise TypeError("Invalid Port")
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def LineDetection_Dark_PointTurn(self, sensorPort, speed, threshold, stop, settlingTime):
        '''
        Line detection by reflected light dark (Point Turn) \n
        - [SensorPort] Set the sensor port (eg PORT_LEFTCOLOUR)\n
        - [Speed:int] Set robot turning speed (-600 to 600)\n
        - [Threshold:int] Set the threshold value (0 to 100)\n
        - [Stop:bool] Stop after reaching degree (True/False)\n
        - [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        normalised = 50
        reflected = 100
        while normalised > threshold:
            if sensorPort == "LC":
                reflected = left_colour.reflection()
            elif sensorPort == "RC":
                reflected = right_colour.reflection()
            normalised = ((reflected - BLACK) / (WHITE - BLACK)) * 100
            left_drive.run(speed)
            right_drive.run(-speed)
            wait(10)
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)
    
    def LineDetection_Bright_PointTurn(self, sensorPort, speed, threshold, stop, settlingTime):
        '''
        Line detection by reflected light bright (Point Turn) \n
        - [SensorPort] Set the sensor port (eg PORT_LEFTCOLOUR)\n
        - [Speed:int] Set robot turning speed (-600 to 600)\n
        - [Threshold:int] Set the threshold value (0 to 100)\n
        - [Stop:bool] Stop after reaching degree (True/False)\n
        - [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        normalised = 50
        reflected = 0
        while normalised < threshold:
            if sensorPort == "LC":
                reflected = left_colour.reflection()
            elif sensorPort == "RC":
                reflected = right_colour.reflection()
            normalised = ((reflected - BLACK) / (WHITE - BLACK)) * 100
            left_drive.run(speed)
            right_drive.run(-speed)
            wait(10)
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def LineSquaring(self, Kp, duration, settlingTime):
        '''
        Robot squares itself to a line with both sensors\n
        [Kp:float] Set the proportional constant value (0.2 to 0.5)\n
        [Duration:int] How long for line squaring (ms)\n
        [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        normalised = 50
        timerLS = StopWatch()
        timerLS.reset()
        while timerLS.time() < duration:
            normalised_left = ((left_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            normalised_right = ((right_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            left_squaring_speed = (normalised_left - 50) * Kp * 20
            right_squaring_speed = (normalised_right - 50) * Kp * 20
            left_drive.run(left_squaring_speed)
            right_drive.run(right_squaring_speed)
            wait(10)
        drive_base.brake()
        hub.speaker.beep(500, settlingTime)

    """ Line follow (Proportional)"""

    def LineFollow_P_BySeconds(self, sensorPort, power, duration, Kp, stop, settlingTime):
        '''
        Proportional line following and stops by seconds\n
        - [SensorPort] Set the sensor port (eg PORT_LEFTCOLOUR)\n
        - [Power:int] Set robot FW/BW power (-90 to 90)\n
        - [Duration:int] How long for line follow (ms)\n
        - [Kp:float] Set the proportional constant value (-0.5 to 0.5)\n
        - [Stop:bool] Stop after reaching degree (True/False)\n
        - [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        error = 0
        normalised = 50
        timerLF = StopWatch()
        timerLF.reset()
        while timerLF.time() < duration:
            if sensorPort == "LC":
                reflected = left_colour.reflection()
            elif sensorPort == "RC":
                reflected = right_colour.reflection()
            else:
                raise TypeError("Invalid Port")
            normalised = ((reflected - BLACK) / (WHITE - BLACK)) * 100
            error = (normalised - 50) * Kp
            left_drive.dc(power + error)
            right_drive.dc(power - error)
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def LineFollow_P_ByDegree(self, resetDegree, sensorPort, power, degree, Kp, stop, settlingTime):
        '''
        Proportional line following and stops by degree\n
        - [ResetDegree:bool] Reset accumulated degree (True/False)\n
        - [SensorPort] Set the sensor port (eg PORT_LEFTCOLOUR)\n
        - [Power:int] Set robot FW/BW power (-90 to 90)\n
        - [Degree:int] How much degree to move (+ve)\n
        - [Kp:float] Set the proportional constant value (-0.5 to 0.5)\n
        - [Stop:bool] Stop after reaching degree (True/False)\n
        - [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        error = 0
        normalised = 50
        distance_driven = 0
        if resetDegree == True:
            left_drive.reset_angle(0)
            right_drive.reset_angle(0)
        while distance_driven < degree:
            distance_driven = (abs(left_drive.angle()) + abs(right_drive.angle())) / 2
            if sensorPort == "LC":
                reflected = left_colour.reflection()
            elif sensorPort == "RC":
                reflected = right_colour.reflection()
            else:
                raise TypeError("Invalid Port")
            normalised = ((reflected - BLACK) / (WHITE - BLACK)) * 100
            error = (normalised - 50) * Kp
            left_drive.dc(power + error)
            right_drive.dc(power - error)
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def LineFollow_P_ByDark(self, sensorPort, detectPort, power, threshold, Kp, stop, settlingTime):
        '''
        Proportional line following and stops by detecting Dark\n
        - [SensorPort] Set the sensor port for line follow (eg PORT_LEFTCOLOUR)\n
        - [DetectPort] Set the sensor port for detection (eg PORT_RIGHTCOLOUR)\n
        - [Power:int] Set robot FW/BW power (-90 to 90)\n
        - [Threshold:int] Set the threshold value (0 to 100)\n
        - [Kp:float] Set the proportional constant value (-0.5 to 0.5)\n
        - [Stop:bool] Stop after reaching degree (True/False)\n
        - [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        error = 0
        normalised = normalised_left = normalised_right = 50
        while normalised > threshold:
            if sensorPort == "LC" and detectPort == "LC":
                normalised_left = ((left_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            elif sensorPort == "RC" and detectPort == "RC":
                normalised_right = ((right_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            else:
                normalised_left = ((left_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
                normalised_right = ((right_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            if detectPort == "LC":
                normalised = normalised_left
            elif detectPort == "RC":
                normalised = normalised_right
            if sensorPort == "LC":
                error = (normalised_left - 50) * Kp
            elif sensorPort == "RC":
                error = (normalised_right - 50) * Kp
            left_drive.dc(power + error)
            right_drive.dc(power - error)
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def LineFollow_Proportional_ByBright(self, sensorPort, detectPort, power, threshold, Kp, stop, settlingTime):
        '''
        Two steps line following and stops by detecting Bright\n
        - [SensorPort] Set the sensor port for line follow (eg PORT_LEFTCOLOUR)\n
        - [DetectPort] Set the sensor port for detection (eg PORT_RIGHTCOLOUR)\n
        - [Power:int] Set robot power (-90 to 90)\n
        - [Threshold:int] Set the threshold value (0 to 100)\n
        - [Kp:float] Set the proportional constant value (-0.5 to 0.5)\n
        - [Stop:bool] Stop after reaching degree (True/False)\n
        - [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        error = 0
        normalised = normalised_left = normalised_right = 50
        while normalised < threshold:
            if sensorPort == "LC" and detectPort == "LC":
                normalised_left = ((left_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            elif sensorPort == "RC" and detectPort == "RC":
                normalised_right = ((right_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            else:
                normalised_left = ((left_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
                normalised_right = ((right_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            if detectPort == "LC":
                normalised = normalised_left
            elif detectPort == "RC":
                normalised = normalised_right
            if sensorPort == "LC":
                error = (normalised_left - 50) * Kp
            elif sensorPort == "RC":
                error = (normalised_right - 50) * Kp
            left_drive.dc(power + error)
            right_drive.dc(power - error)
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    """ Line Follow (Proportional & Derivative) """

    def LineFollow_PD_BySeconds(self, sensorPort, power, duration, Kp, Kd, stop, settlingTime):
        '''
        PD line following and stops by seconds\n
        - [SensorPort] Set the sensor port (eg PORT_LEFTCOLOUR)\n
        - [Power:int] Set robot power (-90 to 90)\n
        - [Duration:int] How long for line follow (ms)\n
        - [Kp:float] Set the proportional constant value (-0.5 to 0.5)\n
        - [Kd:float] Set the derivative constant value (0.01 to 0.5)\n
        - [Stop:bool] Stop after reaching degree (True/False)\n
        - [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        error = lastError = 0
        normalised = 50
        timerLF = StopWatch()
        timerLF.reset()
        while timerLF.time() < duration:
            if sensorPort == "LC":
                reflected = left_colour.reflection()
            elif sensorPort == "RC":
                reflected = right_colour.reflection()
            else:
                raise TypeError("Invalid Port")
            normalised = ((reflected - BLACK) / (WHITE - BLACK)) * 100
            error = normalised - 50
            pd = (error * Kp) + ((error - lastError) * Kd)
            left_drive.dc(power + pd)
            right_drive.dc(power - pd)
            lastError = error
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def LineFollow_PD_ByDegree(self, resetDegree, sensorPort, power, degree, Kp, Kd, stop, settlingTime):
        '''
        PD line following and stops by degree\n
        - [ResetDegree] Reset accumulated degree (True/False)\n
        - [SensorPort] Set the sensor port (eg PORT_LEFTCOLOUR)\n
        - [Power:int] Set robot power (-90 to 90)\n
        - [Degree:int] How much degree to move (+ve)\n
        - [Kp:float] Set the proportional constant value (-0.5 to 0.5)\n
        - [Kd:float] Set the derivative constant value (0.01 to 0.5)\n
        - [Stop:bool] Stop after reaching degree (True/False)\n
        - [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        error = lastError = 0
        normalised = 50
        distance_driven = 0
        while distance_driven < degree:
            distance_driven = (abs(left_drive.angle()) + abs(right_drive.angle())) / 2
            if sensorPort == "LC":
                reflected = left_colour.reflection()
            elif sensorPort == "RC":
                reflected = right_colour.reflection()
            else:
                raise TypeError("Invalid Port")
            normalised = ((reflected - BLACK) / (WHITE - BLACK)) * 100
            error = normalised - 50
            pd = (error * Kp) + ((error - lastError) * Kd)
            left_drive.dc(power + pd)
            right_drive.dc(power - pd)
            lastError = error
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def LineFollow_PD_ByDark(self, sensorPort, detectPort, power, threshold, Kp, Kd, stop, settlingTime):
        '''
        PD line following and stops by detecting Dark\n
        - [SensorPort] Set the sensor port for line follow (eg PORT_LEFTCOLOUR)\n
        - [DetectPort] Set the sensor port for detection (eg PORT_RIGHTCOLOUR)\n
        - [Power:int] Set robot power (-90 to 90)\n
        - [Threshold:int] Set the threshold value (0 to 100)\n
        - [Kp:float] Set the proportional constant value (-0.5 to 0.5)\n
        - [Kd:float] Set the derivative constant value (0.01 to 0.5)\n
        - [Stop:bool] Stop after reaching degree (True/False)\n
        - [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        error = lastError = 0
        normalised = normalised_left = normalised_right = 50
        while normalised > threshold:
            if sensorPort == "LC" and detectPort == "LC":
                normalised_left = ((left_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            elif sensorPort == "RC" and detectPort == "RC":
                normalised_right = ((right_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            else:
                normalised_left = ((left_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
                normalised_right = ((right_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            if detectPort == "LC":
                normalised = normalised_left
            elif detectPort == "RC":
                normalised = normalised_right
            if sensorPort == "LC":
                error = normalised_left - 50
            elif sensorPort == "RC":
                error = normalised_right - 50
            pd = (error * Kp) + ((error - lastError) * Kd)
            left_drive.dc(power + pd)
            right_drive.dc(power - pd)
            lastError = error
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def LineFollow_PD_ByBright(self, sensorPort, detectPort, power, threshold, Kp, Kd, stop, settlingTime):
        '''
        PD line following and stops by detect Bright\n
        - [SensorPort] Set the sensor port for line follow (eg PORT_LEFTCOLOUR)\n
        - [DetectPort] Set the sensor port for detection (eg PORT_RIGHTCOLOUR)\n
        - [Power:int] Set robot power (-90 to 90)\n
        - [Threshold:int] Set the threshold value (0 to 100)\n
        - [Kp:float] Set the proportional constant value (-0.5 to 0.5)\n
        - [Kd:float] Set the derivative constant value (0.01 to 0.5)\n
        - [Stop:bool] Stop after reaching degree (True/False)\n
        - [SettlingTime:int] Wait duration after complete (ms)\n
        '''
        error = lastError = 0
        normalised = normalised_left = normalised_right = 50
        while normalised < threshold:
            if sensorPort == "LC" and detectPort == "LC":
                normalised_left = ((left_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            elif sensorPort == "RC" and detectPort == "RC":
                normalised_right = ((right_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            else:
                normalised_left = ((left_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
                normalised_right = ((right_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            if detectPort == "LC":
                normalised = normalised_left
            elif detectPort == "RC":
                normalised = normalised_right
            if sensorPort == "LC":
                error = normalised_left - 50
            elif sensorPort == "RC":
                error = normalised_right - 50
            pd = (error * Kp) + ((error - lastError) * Kd)
            left_drive.dc(power + pd)
            right_drive.dc(power - pd)
            lastError = error
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)