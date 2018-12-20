#!/usr/bin/env python3

import wpilib
from wpilib import drive
import time
import ctre

from robotpy_ext.autonomous import AutonomousModeSelector

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.motor1 = ctre.WPI_TalonSRX(1)
        self.motor2 = ctre.WPI_TalonSRX(2)
        self.motor3 = ctre.WPI_TalonSRX(3)
        self.motor4 = ctre.WPI_TalonSRX(4)

        self.ultrasonic = wpilib.AnalogInput(0)

        self.playerOne = wpilib.XboxController(0)

        self.robotDrive = wpilib.RobotDrive(self.motor1, self.motor2, self.motor3, self.motor4)

        self.components = {
        'robotDrive': self.robotDrive,
        'ultrasonic': self.ultrasonic
        }
        self.automodes = AutonomousModeSelector('autonomous', self.components)


    def disabledInit(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        self.automodes.run()

    def teleopInit(self):
        pass

    def teleopPeriodic(self):

        self.robotDrive.arcadeDrive(-self.playerOne.getY(0), self.playerOne.getX(0))


        if self.ultrasonic.getVoltage() < 4.9:
            print("Object Detected")
        else:
            print("No Object")

if __name__ == "__main__":
    wpilib.run(MyRobot)
