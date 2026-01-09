# main.py

# Import device classes
from motor import Motor
from light import Light

# Import controller class
from controller import Controller

# Create Motor object
motor = Motor()

# Create Light object
light = Light()

# Create controller objects
motor_controller = Controller()
light_controller = Controller()

# Operate motor using controller
motor_controller.operate_device(motor)

# Operate light using controller
light_controller.operate_device(light)
