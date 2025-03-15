"""  

---- Disclaimer ----

Filename - ACL_FLL_v02.py
Pybricks firmware - v3.5 stable
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

WHEEL_SIZE = 62
WHEEL_SPACING = 145 #160

STR_SPEED = 600
STR_ACCEL = 800
TURN_SPEED = 300
TURN_ACCEL = 500
ATT_SPEED = 250

PORT_LEFTDRIVE = "LD"
PORT_RIGHTDRIVE = "RD"
PORT_LEFTATTACH = "LA"
PORT_RIGHTATTACH = "RA"
PORT_LEFTCOLOUR = "LC"
PORT_RIGHTCOLOUR = "RC"

BLACK = 5
WHITE = 40
THRESHOLD = (WHITE - BLACK) / 2

KP = 0.4
# KI = -0.01
KD = 0.15

######################## Hub & Port setup ########################

# Robot type - Laura 2S
hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
left_colour = ColorSensor(Port.C)
right_colour = ColorSensor(Port.D)
left_attach = Motor(port=Port.A, positive_direction=Direction.CLOCKWISE)
right_attach = Motor(port=Port.B, positive_direction=Direction.CLOCKWISE)
left_drive = Motor(port=Port.E, positive_direction=Direction.COUNTERCLOCKWISE)
right_drive = Motor(port=Port.F, positive_direction=Direction.CLOCKWISE)
drive_base = DriveBase(left_drive, right_drive, WHEEL_SIZE, WHEEL_SPACING)
hub.system.set_stop_button([Button.BLUETOOTH])

######################## Hub Display ########################

class Laura():

    ######################## Hub display / controls ########################

    def Hub_StatusLight(self, colour):
        """
        Sets the SPIKE Prime button light to the specified colour.

        :param colour: The colour to set the light to.

        :type colour: Color
        """
        hub.light.on(colour)

    def Hub_StatusBlink(self, colour, duration):
        """
        Sets the SPIKE Prime button light to blink at the specified colour.

        :param colour: The colour to set the light to.
        :param duration: The duration of the blink in milliseconds.
        
        :type colour: Color
        :type duration: int
        """
        hub.light.blink(colour, duration)

    def Hub_DisplayNum(self, num):
        """
        Sets the SPIKE Prime display to show the specified number.

        :param num: The number to display.
        
        :type num: int
        """
        hub.display.number(num)

    def Hub_DisplayIcon(self, icon):
        """
        Sets the SPIKE Prime display to show the specified icon.

        :param icon: The icon to display.

        :type icon: Icon
        """
        hub.display.icon(icon)

    def Hub_DisplayPixel(self, row, column, brightness):
        """
        Sets the SPIKE Prime display to show the specified pixel.
        
        :param row: The row of the pixel.
        :param column: The column of the pixel.
        :param brightness: The brightness of the pixel.
        
        :type row: int
        :type column: int
        :type brightness: int
        """
        hub.display.off()
        hub.display.pixel(row, column, brightness)

    def Hub_SpeakerBeep(self, frequency, duration):
        """
        Plays a beep sound on the SPIKE Prime speaker.
        
        :param frequency: The frequency of the beep in Hertz.
        :param duration: The duration of the beep in milliseconds.
        
        :type frequency: int
        :type duration: int
        """
        hub.speaker.beep(frequency, duration)

    def Hub_Shutdown(self):
        """
        Shuts down the SPIKE Prime.
        """
        hub.display.icon(Icon.CIRCLE)
        wait(100)
        hub.speaker.play_notes(["C4/16", "C3/16", "C2/16"])
        hub.system.shutdown()

    def Hub_ButtonPressed(self):
        """
        Returns a list of buttons that are currently pressed on the SPIKE Prime.
        
        :return: A list of buttons that are currently pressed.
        :rtype: list
        """
        return hub.buttons.pressed()

    ######################## Port view / check tools ########################

    def PortView_ReflectedLight(self, interval):
        """
        Print the reflected light intensity of the colour sensor in the console.
        
        :param interval: The interval in milliseconds between each reading.
        
        :type interval: int
        """
        print("---- Reflected Value ----")
        while True: 
            normalised_left = ((left_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            normalised_right = ((right_colour.reflection() - BLACK) / (WHITE - BLACK)) * 100
            print("Reflected(left): ", left_colour.reflection(), "| Reflected(right): ", right_colour.reflection(), "| Normalised(left): ", normalised_left , "| Normalised(right): ", normalised_right)
            wait(interval)

    def PortView_HSV(self, interval):
        """
        Print the HSV value of the colour sensor in the console.
        
        :param interval: The interval in milliseconds between each reading.
        
        :type interval: int
        """
        print("---- HSV Value ----")
        while True:
            print("HSV(left): ", left_colour.hsv(), "| HSV(right): ", right_colour.hsv())
            wait(interval)

    def PortView_Battery(self):
        """
        Print the battery information of the hub in the console.
        """
        print("---- Hub battery info ----")
        print("Hub battery voltage: ", hub.battery.voltage(), "mV")
        print("Hub battery current: ", hub.battery.current(), "mA")
        print(" ")

    def PortView_MotorAngle(self, interval):
        """
        Print the angle of the motors in the console.
        
        :param interval: The interval in milliseconds between each reading.
        
        :type interval: int
        """
        print("---- Motor angle ----")
        while True:
            print("LeftDrive: ", left_drive.angle(), "| RightDrive: ", right_drive.angle(), "| Arm1: ", left_attach.angle(), "| Arm2: ", right_attach.angle())
            wait(interval)

    def PortView_MotorLoad(self, motorPower, interval):
        """
        Print the load of the motors in the console.
        
        :param motorPower: The power of the motors in percentage.
        :param interval: The interval in milliseconds between each reading.
        
        :type motorPower: int
        :type interval: int
        """
        print("---- Motor load ----")
        while True:
            left_drive.dc(motorPower)
            right_drive.dc(motorPower)
            left_attach.dc(motorPower)
            right_attach.dc(motorPower)
            print("LeftDrive: ", left_drive.load(), "| RightDrive: ", right_drive.load(), "| Arm1: ", left_attach.load(), "| Arm2: ", right_attach.load())
            wait(interval)

    def PortView_MotorSpeed(self, motorSpeed, interval):
        """
        Print the speed of the motors in the console.
        
        :param motorSpeed: The speed of the motors in degrees per second.
        :param interval: The interval in milliseconds between each reading.
        
        :type motorSpeed: int
        :type interval: int
        """
        print("---- Motor speed ----")
        while True:
            left_drive.run(motorSpeed)
            right_drive.run(motorSpeed)
            left_attach.run(motorSpeed)
            right_attach.run(motorSpeed)
            print("LeftDrive: ", left_drive.speed(), "| RightDrive: ", right_drive.speed(), "| Arm1: ", left_attach.speed(), "| Arm2: ", right_attach.speed())
            wait(interval)        

    ######################## Single Motor control ########################

    def SingleMotor_On(self, port, speed):
        """
        Run the motor at the specified speed.
        
        :param port: The port of the motor.
        :param speed: The speed of the motor in degrees per second.
        
        :type port: str
        :type speed: int
        
        :raises TypeError: If the port is invalid.
        """
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

    def SingleMotor_BySeconds(self, port, speed, duration, stopMethod=Stop.BRAKE, waitForComplete=True):
        """
        Run the motor at the specified speed for the specified duration.
        
        :param port: The port of the motor.
        :param speed: The speed of the motor in degrees per second.
        :param duration: The duration of the motor run in milliseconds.
        :param stopMethod: The method to stop the motor.
        :param waitForComplete: The method to wait for the motor to complete.
        
        :type port: str
        :type speed: int
        :type duration: int
        :type stopMethod: Stop
        :type waitForComplete: bool
        
        :raises TypeError: If the port is invalid.
        """
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

    def SingleMotor_ByDegree(self, port, speed, degree, stopMethod=Stop.BRAKE, waitForComplete=True):
        """
        Run the motor at the specified speed for the specified degree.
        
        :param port: The port of the motor.
        :param speed: The speed of the motor in degrees per second.
        :param degree: The degree of the motor run.
        :param stopMethod: The method to stop the motor.
        :param waitForComplete: The method to wait for the motor to complete.
        
        :type port: str
        :type speed: int
        :type degree: int
        :type stopMethod: Stop
        :type waitForComplete: bool
        
        :raises TypeError: If the port is invalid.
        """
        if port == "LA":
            left_attach.run_angle(speed, degree, stopMethod, waitForComplete)
        elif port == "RA":
            right_attach.run_angle(speed, degree, stopMethod, waitForComplete)
        elif port == "LD":
            left_drive.run_angle(speed, degree, stopMethod, waitForComplete)
        elif port == "RD":
            right_drive.run_angle(speed, degree, stopMethod, waitForComplete)
        else:
            raise TypeError("Invalid Port")

    def SingleMotor_Brake(self, port):
        """
        Brake the motor.
        
        :param port: The port of the motor.
        
        :type port: str
        
        :raises TypeError: If the port is invalid.
        """
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

    ######################## FLL custom feature ########################
    
    def Unregulated_AttachMotor(self, leftPower, rightPower):
        """
        Run the unregulated motor at the specified power.
        
        :param leftPower: The power of the left motor in percentage.
        :param rightPower: The power of the right motor in percentage.
        
        :type leftPower: int
        :type rightPower: int
        """
        if abs(left_attach.load()) > 30:
            # left_attach.dc(0)
            left_attach.stop()
            wait(20)
        elif abs(right_attach.load()) > 30:
            # right_attach.dc(0)
            right_attach.stop()
            wait(20)
        else:
            left_attach.dc(leftPower)
            right_attach.dc(rightPower)
            wait(20)

    def Calibrate_ColorSensor(self):
        """
        Calibrate the colour sensor to get the maximum (white) and minimum (black) reflected value.
        The value will then be stored in the SPIKE Hub and used again and again as the user wish.

        The robot should move from one white edge to the other to get the maximum white reflected value.
        And vice versa, move from one white edge to the other to get the minimum black reflected value.

        The value will be stored in the SPIKE Hub as follows:
        - White colour value for left sensor: byte number 1
        - White colour value for right sensor: byte number 2
        - Black colour value for left sensor: byte number 3
        - Black colour value for right sensor: byte number 4

        The value will be stored in the SPIKE Hub as bytes.
        """
        # Get the white color value for sensor
        max_threshold_left = []
        min_threshold_left = []

        max_threshold_right = []
        min_threshold_right = []

        white_threshold_left = 0
        black_threshold_left = 0

        white_threshold_right = 0
        black_threshold_right = 0

        print("Calibrating white color value...")
        # Move from one white edge to the other to get the maximum white color value
        while(not drive_base.distance() >= 60):
            drive_base.drive(100, 0)
            max_threshold_left.append(left_colour.reflection())
            max_threshold_right.append(right_colour.reflection())
            wait(20)
        drive_base.brake()
        white_threshold_left = max(max_threshold_left)
        white_threshold_right = max(max_threshold_right)
        hub.speaker.beep(700, 200)
        wait(1000)
        # Store data onto brick
        hub.system.storage(offset=1, write=white_threshold_left.to_bytes(1, "big"))
        hub.system.storage(offset=2, write=white_threshold_right.to_bytes(1, "big"))
        print(
            "Left white color value: ", int.from_bytes(hub.system.storage(offset=1, read=1), "big"),
            "\nRight white color value: ", int.from_bytes(hub.system.storage(offset=2, read=1), "big")
        )
        hub.speaker.beep(600, 200)
        wait(1000)

        # Move to from one white edge to the other to get the minimum black color value
        drive_base.reset()
        while(not drive_base.distance() <= -50):
            drive_base.drive(-100, 0)
            min_threshold_left.append(left_colour.reflection())
            min_threshold_right.append(right_colour.reflection())
            wait(20)
        drive_base.brake()
        black_threshold_left = min(min_threshold_left)
        black_threshold_right = min(min_threshold_right)
        hub.speaker.beep(700, 200)
        wait(1000)
        # Store data onto brick
        hub.system.storage(offset=3, write=black_threshold_left.to_bytes(1, "big"))
        hub.system.storage(offset=4, write=black_threshold_right.to_bytes(1, "big"))
        print(
            "Black color value: ", int.from_bytes(hub.system.storage(offset=3, read=1), "big"),
            "\nRight black color value: ", int.from_bytes(hub.system.storage(offset=4, read=1), "big")
        )
        hub.speaker.beep(600, 200)

    ######################## Drive base movements ########################

    def MoveSteering_Seconds(self, speed, steering, duration, stop=True, settlingTime=200):
        """
        Drive the robot at the specified speed and steering for the specified duration.
        
        :param speed: The speed of the robot in millimeters per second.
        :param steering: The steering of the robot in percentage.
        :param duration: The duration of the robot drive in milliseconds.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type speed: int
        :type steering: int
        :type duration: int
        :type stop: Stop
        :type settlingTime: int
        """
        drive_base.drive(speed, steering)
        wait(duration)
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def MoveSteering_Distance(self, speed, steering, distance, stop=True, settlingTime=200):
        """
        Drive the robot at the specified speed and steering for the specified distance.
        
        :param speed: The speed of the robot in millimeters per second.
        :param steering: The steering of the robot in percentage.
        :param distance: The distance of the robot drive in millimeters.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type speed: int
        :type steering: int
        :type distance: int
        :type stop: Stop
        :type settlingTime: int
        """
        distance_driven = 0
        while distance_driven < distance:
            distance_driven = (abs(left_drive.angle()) + abs(right_drive.angle())) / 2
            drive_base.drive(speed, steering)

            # # Get power limits for left motor
            # left_limits = left_drive.control.limits()
            # print(f"Left Motor - Speed: {left_limits[0]}°/s, Acceleration: {left_limits[1]}°/s², Voltage: {left_limits[2]}mV")

            # # Get power limits for right motor 
            # right_limits = right_drive.control.limits()
            # print(f"Right Motor - Speed: {right_limits[0]}°/s, Acceleration: {right_limits[1]}°/s², Voltage: {right_limits[2]}mV")
            
            # print(f"""
            # Left Motor:
            # Speed: {left_drive.speed()} °/s
            # Load: {left_drive.load()} mNm
            
            # Right Motor:
            # Speed: {right_drive.speed()} °/s
            # Load: {right_drive.load()} mNm
            # """)

        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def MoveSteering_DistanceNew(self, target_speed, steering, distance, acceleration, stop=True, settlingTime=100):
        
        distance_driven = 0
        current_speed = 0  # Start from a standstill
        deadband = 4

        # Calculate total time to travel the distance at target speed
        # total_time = distance / target_speed if target_speed > 0 else 0

        # Determine acceleration and deceleration rates
        # max_acceleration = target_speed / (total_time / 2) if total_time > 0 else 0
        # max_deceleration = target_speed / (total_time / 2) if total_time > 0 else 0
        
        max_acceleration = acceleration
        max_deceleration = acceleration

        
        while distance_driven < distance:
            distance_driven = (abs(left_drive.angle()) + abs(right_drive.angle())) / 2
            # drive_base.drive(speed, steering)

            # Adjust current speed towards target speed based on acceleration/deceleration
            if distance_driven < distance / 2:  # Accelerate until halfway
                current_speed += max_acceleration * (1 / 50)  # Adjust speed incrementally
                if current_speed > target_speed:
                    current_speed = target_speed  # Cap to target speed
            else:  # Decelerate after halfway
                current_speed -= max_deceleration * (1 / 50)  # Adjust speed incrementally
                if current_speed < 0:
                    current_speed = 0  # Ensure speed does not go negative

            # Get current speeds of both motors
            left_speed = left_drive.speed()
            right_speed = right_drive.speed()

            # Calculate the speed difference
            # speed_difference = left_speed - right_speed
            speed_difference = right_speed - left_speed

            # Apply deadband
            deadband = 10
            if abs(speed_difference) > deadband:
                # Adjust steering based on speed difference (tune this factor)
                steering_adjustment = speed_difference * 0.2  # Reduced factor (0.02)
                # Limit maximum adjustment
                steering_adjustment = max(min(steering_adjustment, 50), -50)  # Limit to ±50°

                # Update drive command with adjusted steering
                drive_base.drive(current_speed, steering)
            else:
                # If within deadband, drive straight
                drive_base.drive(current_speed, 0)         
                
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def MoveStraight_Distance(self, speed, accel, distance, useGyro=True, waitForComplete=True, stopMethod=Stop.BRAKE, settlingTime=200):
        """
        Drive the robot straight at the specified speed for the specified distance.
        
        :param speed: The speed of the robot in millimeters per second.
        :param accel: The acceleration of the robot in millimeters per second squared.
        :param distance: The distance of the robot drive in millimeters.
        :param useGyro: The method to use the gyro sensor.
        :param waitForComplete: The method to wait for the robot to complete.
        :param stopMethod: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type speed: int
        :type accel: int
        :type distance: int
        :type useGyro: bool
        :type waitForComplete: bool
        :type stopMethod: Stop
        :type settlingTime: int
        """
        drive_base.reset()
        drive_base.use_gyro(useGyro)
        drive_base.settings(speed, accel, TURN_SPEED, TURN_ACCEL)
        drive_base.straight(distance, stopMethod, waitForComplete)
        hub.speaker.beep(500, settlingTime)

    def MoveCurve_Distance(self, speed, accel, radius, angle, waitForComplete=True, stopMethod=Stop.BRAKE, settlingTime=200):
        """
        Drive the robot in a curve at the specified speed for the specified distance.
        
        :param speed: The speed of the robot in millimeters per second.
        :param accel: The acceleration of the robot in millimeters per second squared.
        :param radius: The radius of the robot curve in millimeters.
        :param angle: The angle of the robot curve in degrees.
        :param waitForComplete: The method to wait for the robot to complete.
        :param stopMethod: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type speed: int
        :type accel: int
        :type radius: int
        :type angle: int
        :type waitForComplete: bool
        :type stopMethod: Stop
        :type settlingTime: int
        """
        drive_base.reset()
        drive_base.use_gyro(True)
        drive_base.settings(speed, accel, TURN_SPEED, TURN_ACCEL)
        drive_base.curve(radius, angle, stopMethod, waitForComplete)
        hub.speaker.beep(500, settlingTime)
    
    def LockTurn_Seconds(self, port, speed, duration, stop=True, settlingTime=200):
        """
        Drive the robot in a lock turn at the specified speed for the specified duration.
        
        :param port: The port of the motor.
        :param speed: The speed of the robot in millimeters per second.
        :param duration: The duration of the robot drive in milliseconds.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type port: str
        :type speed: int
        :type duration: int
        :type stop: Stop
        :type settlingTime: int
        """
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
    
    def LockTurn_Degree(self, port, speed, degree, stop=True, settlingTime=200):
        """
        Drive the robot in a lock turn at the specified speed for the specified degree.
        
        :param port: The port of the motor.
        :param speed: The speed of the robot in millimeters per second.
        :param degree: The degree of the robot drive.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type port: str
        :type speed: int
        :type degree: int
        :type stop: Stop
        :type settlingTime: int
        """
        distance_driven = 0
        left_drive.reset_angle(0)
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

    def PointTurn_Seconds(self, speed, duration, stop=True, settlingTime=200):
        """
        Drive the robot in a point turn at the specified speed for the specified duration.
        
        :param speed: The speed of the robot in millimeters per second.
        :param duration: The duration of the robot drive in milliseconds.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type speed: int
        :type duration: int
        :type stop: Stop
        :type settlingTime: int
        """
        timerPT = StopWatch()
        timerPT.reset()
        while timerPT.time() < duration:
            left_drive.run(speed)
            right_drive.run(-speed)
            wait(10)
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def PointTurn_Degree(self, speed, degree, stop=True, settlingTime=200):
        """
        Drive the robot in a point turn at the specified speed for the specified degree.
        
        :param speed: The speed of the robot in millimeters per second.
        :param degree: The degree of the robot drive.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type speed: int
        :type degree: int
        :type stop: Stop
        :type settlingTime: int
        """
        left_drive.reset_angle(0)
        right_drive.reset_angle(0)
        distance_driven = 0
        while distance_driven < degree:
            distance_driven = (abs(left_drive.angle()) + abs(right_drive.angle())) / 2
            left_drive.run(speed)
            right_drive.run(-speed)
            wait(10)
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def PointTurn_Angle(self, turn_speed, turn_accel, angle, waitForComplete=True, stopMethod=Stop.BRAKE, settlingTime=200):
        """
        Drive the robot in a point turn at the specified speed for the specified angle.
        
        :param turn_speed: The speed of the robot in millimeters per second.
        :param turn_accel: The acceleration of the robot in millimeters per second squared.
        :param angle: The angle of the robot drive.
        :param waitForComplete: The method to wait for the robot to complete.
        :param stopMethod: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type turn_speed: int
        :type turn_accel: int
        :type angle: int
        :type waitForComplete: bool
        :type stopMethod: Stop
        :type settlingTime: int
        """
        drive_base.reset()
        drive_base.use_gyro(True)
        drive_base.settings(STR_SPEED, STR_ACCEL, turn_speed, turn_accel)
        drive_base.turn(angle, stopMethod, waitForComplete)
        hub.speaker.beep(500, settlingTime)

    ######################## Colour Sensing ########################

    def ColourDetection_Steering(self, sensorPort, speed, colour, steering, stop=True, settlingTime=200):
        """
        Drive the robot at the specified speed and steering until the specified colour is detected.

        :param sensorPort: The port of the colour sensor.
        :param speed: The speed of the robot in millimeters per second.
        :param colour: The colour to detect.
        :param steering: The steering of the robot in percentage.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.

        :type sensorPort: str
        :type speed: int
        :type colour: Color
        :type steering: int
        :type stop: Stop
        :type settlingTime: int

        :raises TypeError: If the port is invalid.
        """
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

    def LineDetection_Dark_Steering(self, sensorPort, speed, steering, threshold=BLACK, stop=True, settlingTime=200):
        """
        Drive the robot at the specified speed and steering until the specified dark line is detected.
        
        :param sensorPort: The port of the colour sensor.
        :param speed: The speed of the robot in millimeters per second.
        :param steering: The steering of the robot in percentage.
        :param threshold: The threshold of the dark line.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type sensorPort: str
        :type speed: int
        :type steering: int
        :type threshold: int
        :type stop: Stop
        :type settlingTime: int
        
        :raises TypeError: If the port is invalid.
        """
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

    def LineDetection_Bright_Steering(self, sensorPort, speed, steering, threshold=WHITE, stop=True, settlingTime=200):
        """
        Drive the robot at the specified speed and steering until the specified bright line is detected.
        
        :param sensorPort: The port of the colour sensor.
        :param speed: The speed of the robot in millimeters per second.
        :param steering: The steering of the robot in percentage.
        :param threshold: The threshold of the bright line.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type sensorPort: str
        :type speed: int
        :type steering: int
        :type threshold: int
        :type stop: Stop
        :type settlingTime: int
        
        :raises TypeError: If the port is invalid.
        """
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
    
    def LineDetection_Dark_LockTurn(self, sensorPort, motorPort, speed, threshold=BLACK, stop=True, settlingTime=200):
        """
        Drive the robot in a lock turn at the specified speed until the specified dark line is detected.
        
        :param sensorPort: The port of the colour sensor.
        :param motorPort: The port of the motor.
        :param speed: The speed of the robot in millimeters per second.
        :param threshold: The threshold of the dark line.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type sensorPort: str
        :type motorPort: str
        :type speed: int
        :type threshold: int
        :type stop: Stop
        :type settlingTime: int
        
        :raises TypeError: If the port is invalid.
        """
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

    def LineDetection_Bright_LockTurn(self, sensorPort, motorPort, speed, threshold=WHITE, stop=True, settlingTime=200):
        """
        Drive the robot in a lock turn at the specified speed until the specified bright line is detected.
        
        :param sensorPort: The port of the colour sensor.
        :param motorPort: The port of the motor.
        :param speed: The speed of the robot in millimeters per second.
        :param threshold: The threshold of the bright line.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type sensorPort: str
        :type motorPort: str
        :type speed: int
        :type threshold: int
        :type stop: Stop
        :type settlingTime: int
        
        :raises TypeError: If the port is invalid.
        """
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

    def LineDetection_Dark_PointTurn(self, sensorPort, speed, threshold=BLACK, stop=True, settlingTime=200):
        """
        Drive the robot in a point turn at the specified speed until the specified dark line is detected.
        
        :param sensorPort: The port of the colour sensor.
        :param speed: The speed of the robot in millimeters per second.
        :param threshold: The threshold of the dark line.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type sensorPort: str
        :type speed: int
        :type threshold: int
        :type stop: Stop
        :type settlingTime: int
        """
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
    
    def LineDetection_Bright_PointTurn(self, sensorPort, speed, threshold=WHITE, stop=True, settlingTime=200):
        """
        Drive the robot in a point turn at the specified speed until the specified bright line is detected.
        
        :param sensorPort: The port of the colour sensor.
        :param speed: The speed of the robot in millimeters per second.
        :param threshold: The threshold of the bright line.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type sensorPort: str
        :type speed: int
        :type threshold: int
        :type stop: Stop
        :type settlingTime: int
        """
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

    def LineSquaring(self, duration, Kp=KP, settling_time=200):
        """
        Drive the robot to square up to a line for the specified duration.
        
        :param duration: The duration of the squaring in milliseconds.
        :param Kp: The proportional gain of the squaring.
        :param settling_time: The settling time of the robot in milliseconds.
        
        :type duration: int
        :type Kp: float
        :type settling_time: int
        """
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
        hub.speaker.beep(500, settling_time)

    ######################## Line follow (Proportional) ########################

    def LineFollow_UntilSeconds(self, sensorPort, power, duration, Kp=KP, stop=True, settlingTime=200):
        """
        A proportional line follower for the specified duration.
        
        :param sensorPort: The port of the colour sensor.
        :param power: The power of the robot in percentage.
        :param duration: The duration of the line follow in milliseconds.
        :param Kp: The proportional gain of the line follow.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type sensorPort: str
        :type power: int
        :type duration: int
        :type Kp: float
        :type stop: bool
        :type settlingTime: int
        
        :raises TypeError: If the port is invalid.
        """
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

    def LineFollow_UntilDegree(self, sensorPort, power, degree, Kp=KP, stop=True, settlingTime=200):
        """
        A proportional line follower for the specified degree.
        
        :param sensorPort: The port of the colour sensor.
        :param power: The power of the robot in percentage.
        :param degree: The degree of the line follow.
        :param Kp: The proportional gain of the line follow.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type sensorPort: str
        :type power: int
        :type degree: int
        :type Kp: float
        :type stop: bool
        :type settlingTime: int
        
        :raises TypeError: If the port is invalid.
        """
        error = 0
        normalised = 50
        distance_driven = 0
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

    def LineFollow_UntilDark(self, sensorPort, detectPort, power, threshold=BLACK, Kp=KP, stop=True, settlingTime=200):
        """
        A proportional line follower until the specified dark line is detected.

        :param sensorPort: The port of the colour sensor.
        :param detectPort: The port of the colour sensor to detect the line.
        :param power: The power of the robot in percentage.
        :param threshold: The threshold of the dark line.
        :param Kp: The proportional gain of the line follow.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.

        :type sensorPort: str
        :type detectPort: str
        :type power: int
        :type threshold: int
        :type Kp: float
        :type stop: bool
        :type settlingTime: int
        """
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

    def LineFollow_UntilBright(self, sensorPort, detectPort, power, threshold=WHITE, Kp=KP, stop=True, settlingTime=200):
        """
        A proportional line follower until the specified bright line is detected.
        
        :param sensorPort: The port of the colour sensor.
        :param detectPort: The port of the colour sensor to detect the line.
        :param power: The power of the robot in percentage.
        :param threshold: The threshold of the bright line.
        :param Kp: The proportional gain of the line follow.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type sensorPort: str
        :type detectPort: str
        :type power: int
        :type threshold: int
        :type Kp: float
        :type stop: bool
        :type settlingTime: int
        """
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

    ######################## Line Follow (Proportional & Derivative) ########################

    def LineFollow_PD_UntilSeconds(self, sensorPort, power, duration, Kp=KP, Kd=KD, stop=True, settlingTime=200):
        """
        A proportional and derivative line follower for the specified duration.
        
        :param sensorPort: The port of the colour sensor.
        :param power: The power of the robot in percentage.
        :param duration: The duration of the line follow in milliseconds.
        :param Kp: The proportional gain of the line follow.
        :param Kd: The derivative gain of the line follow.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type sensorPort: str
        :type power: int
        :type duration: int
        :type Kp: float
        :type Kd: float
        :type stop: bool
        :type settlingTime: int
        
        :raises TypeError: If the port is invalid.
        """
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

    def LineFollow_PD_UntilDegree(self, sensorPort, power, degree, Kp=KP, Kd=KD, stop=True, settlingTime=200):
        """
        A proportional and derivative line follower for the specified degree.
        
        :param sensorPort: The port of the colour sensor.
        :param power: The power of the robot in percentage.
        :param degree: The degree of the line follow.
        :param Kp: The proportional gain of the line follow.
        :param Kd: The derivative gain of the line follow.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type sensorPort: str
        :type power: int
        :type degree: int
        :type Kp: float
        :type Kd: float
        :type stop: bool
        :type settlingTime: int
        
        :raises TypeError: If the port is invalid.
        """
        error = lastError = 0
        normalised = 50
        distance_driven = 0
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
            error = normalised - 50
            pd = (error * Kp) + ((error - lastError) * Kd)
            left_drive.dc(power + pd)
            right_drive.dc(power - pd)
            lastError = error
        if stop == True:
            drive_base.brake()
            hub.speaker.beep(500, settlingTime)

    def LineFollow_PD_UntilDark(self, sensorPort, detectPort, power, threshold=BLACK, Kp=KP, Kd=KD, stop=True, settlingTime=200):
        """
        A proportional and derivative line follower until the specified dark line is detected.
        
        :param sensorPort: The port of the colour sensor.
        :param detectPort: The port of the colour sensor to detect the line.
        :param power: The power of the robot in percentage.
        :param threshold: The threshold of the dark line.
        :param Kp: The proportional gain of the line follow.
        :param Kd: The derivative gain of the line follow.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type sensorPort: str
        :type detectPort: str
        :type power: int
        :type threshold: int
        :type Kp: float
        :type Kd: float
        :type stop: bool
        :type settlingTime: int
        """
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

    def LineFollow_PD_UntilBright(self, sensorPort, detectPort, power, threshold=WHITE, Kp=KP, Kd=KD, stop=True, settlingTime=200):
        """
        A proportional and derivative line follower until the specified bright line is detected.
        
        :param sensorPort: The port of the colour sensor.
        :param detectPort: The port of the colour sensor to detect the line.
        :param power: The power of the robot in percentage.
        :param threshold: The threshold of the bright line.
        :param Kp: The proportional gain of the line follow.
        :param Kd: The derivative gain of the line follow.
        :param stop: The method to stop the robot.
        :param settlingTime: The settling time of the robot in milliseconds.
        
        :type sensorPort: str
        :type detectPort: str
        :type power: int
        :type threshold: int
        :type Kp: float
        :type Kd: float
        :type stop: bool
        :type settlingTime: int
        """
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