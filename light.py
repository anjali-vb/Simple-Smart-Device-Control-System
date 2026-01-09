# light.py

# Import base Device class
from device import Device

# Light class inherits from Device
class Light(Device):

    def start(self):
        # Check if light is OFF
        if not self._is_on:
            # Turn the light ON
            self._is_on = True
            # Print device-specific message
            print("Light switched on")

    def stop(self):
        # Check if light is ON
        if self._is_on:
            # Turn the light OFF
            self._is_on = False
            # Print device-specific message
            print("Light switched off")
