#!/usr/bin/env python3

import wpilib
from wpilib import drive
import time
import ctre

from robotpy_ext.autonomous import AutonomousModeSelector

from robotpy_ext.common_drivers import units, navx

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.motor1 = ctre.WPI_TalonSRX(1)
        self.motor2 = ctre.WPI_TalonSRX(2)
        self.motor3 = ctre.WPI_TalonSRX(3)
        self.motor4 = ctre.WPI_TalonSRX(4)

        self.ultrasonic = wpilib.AnalogInput(0)
        self.distanceSensor = navx.AHRS.create_i2c()

        self.playerOne = wpilib.XboxController(0)

        self.robotDrive = wpilib.RobotDrive(self.motor1, self.motor2, self.motor3, self.motor4)

        self.components = {
        'robotDrive': self.robotDrive,
        'ultrasonic': self.ultrasonic
        }
        self.automodes = AutonomousModeSelector('autonomous', self.components)

        self.navx = navx.AHRS.create_spi()

    def disabledInit(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        self.automodes.run()

    def teleopInit(self):
        self.navx.reset()

    def teleopPeriodic(self):

        print(self.motor4.getPulseWidthAll())

        if self.ultrasonic.getVoltage() < 4.9:
            print("Close Range - Object Detected")
#        elif self.distanceSensor.getVolatage() < 4.9:
#            print("Long Range - Object Detected")
        else:
            print("No Object")


        if self.playerOne.getAButton():
            self.autoAlign()
        elif self.playerOne.getBButton():
            self.navx.reset()
        else:
            self.robotDrive.arcadeDrive(-self.playerOne.getY(0), self.playerOne.getX(0))

    def autoAlign(self):
        speed = 0.5
        if self.navx.getYaw() > 0 and not self.navx.getYaw() < -170 or self.navx.getYaw() > 170:
            self.robotDrive.arcadeDrive(-self.playerOne.getY(0), speed)
        elif self.navx.getYaw() < 0 and not self.navx.getYaw() < -170 or self.navx.getYaw() > 170:
            self.robotDrive.arcadeDrive(-self.playerOne.getY(0), -speed)
        elif self.navx.getYaw() < -170 or self.navx.getYaw() > 170:
            self.robotDrive.arcadeDrive(-self.playerOne.getY(0), 0)

if __name__ == "__main__":
    wpilib.run(MyRobot)
