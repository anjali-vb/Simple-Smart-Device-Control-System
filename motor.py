# motor.py

# Import the base Device class
from device import Device

# Motor class inherits from Device
class Motor(Device):

    def start(self):
        # Check if motor is currently OFF
        if not self._is_on:
            # Change internal state to ON
            self._is_on = True
            # Print device-specific message
            return "Motor has started"

    def stop(self):
        # Check if motor is currently ON
        if self._is_on:
            # Change internal state to OFF
            self._is_on = False
            # Print device-specific message
            return "Motor has stopped"
