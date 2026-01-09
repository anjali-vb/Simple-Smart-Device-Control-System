# device.py

# Base class for all devices
class Device:
    def __init__(self):
        # Protected variable to store ON/OFF state
        
        self._is_on = False
        #device is in off state

    def start(self):
        # This method is meant to be overridden by child classes
        # If a child class does not implement it, an error is raised
        raise NotImplementedError("Start method must be implemented")

    def stop(self):
        # This method is also meant to be overridden
        raise NotImplementedError("Stop method must be implemented")

    def is_on(self):
        # Public method to allow external code to CHECK the state
        # This maintains encapsulation (read-only access)
        return self._is_on
