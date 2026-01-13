
import unittest
from motor import Motor
from light import Light
from controller import Controller

class TestSmartDevices(unittest.TestCase):

    def setUp(self):
        # Runs before every test
        self.motor = Motor()
        self.light = Light()
        self.controller = Controller()

    def test_device_initial_state(self):
        # Test initial OFF state
        self.assertFalse(self.motor.is_on())
        self.assertFalse(self.light.is_on())

    def test_motor_start_stop(self):
        # Test Motor behavior
        output = self.controller.operate_device(self.motor)

        self.assertEqual(output[0], "Motor has started")
        self.assertEqual(output[1], "Motor has stopped")
        self.assertFalse(self.motor.is_on())

    def test_light_start_stop(self):
        # Test Light behavior
        output = self.controller.operate_device(self.light)
        self.assertEqual(output[0], "Light switched on")
        self.assertEqual(output[1], "Light switched off")
        self.assertFalse(self.light.is_on())

#Tests run only when this file is executed directly

if __name__ == "__main__":
    unittest.main()

