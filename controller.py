# controller.py

# Controller class does not depend on any specific device
class Controller:

    def operate_device(self, device):
        # Accepts ANY device object
        # Calls start method of the device
        device.start()

        # Calls stop method of the device
        device.stop()
