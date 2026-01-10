# main.py

# Import device classes
from motor import Motor
from light import Light

# Import controller class
from controller import Controller

def displayOutput(outputs):
  for message in outputs:
    print(message)

# Create Motor object
motor = Motor()

# Create Light object
light = Light()

# Create controller objects
device_controller = Controller()

# Operate motor using controller
displayOutput(device_controller.operate_device(motor))

# Operate light using controller
displayOutput(device_controller.operate_device(light))

