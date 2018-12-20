from robotpy_ext.autonomous import StatefulAutonomous, timed_state, state

class DriveForward(StatefulAutonomous):

    DEFAULT = True
    MODE_NAME = 'Drive Forward'

    def initialize(self):
        self.robotDrive.arcadeDrive(0, 0)

    @timed_state(duration=0.5, next_state='drive_forward', first=True)
    def drive_wait(self):
        self.robotDrive.arcadeDrive(0, 0)

    @timed_state(duration=5, next_state='stop')
    def drive_forward(self):
        if self.ultrasonic.getVoltage() < 4.9:
            self.robotDrive.arcadeDrive(0, 0)
            print("stopped - Object Found")
            self.next_state('stop')
        else:
            self.robotDrive.arcadeDrive(0.4, 0)

    @state()
    def stop(self):
         self.robotDrive.arcadeDrive(0, 0)
