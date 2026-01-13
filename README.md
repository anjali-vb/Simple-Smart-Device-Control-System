# Simple Smart Device Control System

A minimal Python project that demonstrates a controller coordinating simple smart devices (motor and light). The project includes device classes, a controller, a simple runner, and unit tests.

## Features

- Small, clear object-oriented design for devices and controller
- Example usage via `main.py`
- Unit tests with Python's `unittest` in `test_devices.py`

## Files

- [controller.py](controller.py): Controller logic to operate devices
- [device.py](device.py): Base `Device` class shared by devices
- [motor.py](motor.py): `Motor` device implementation
- [light.py](light.py): `Light` device implementation
- [main.py](main.py): Simple runner / demo showing usage
- [test_devices.py](test_devices.py): Unit tests (uses `unittest`)

## Requirements

- Python 3.8+

## Usage

Run the demo:

```bash
python main.py
```

Run the unit tests:

```bash
python -m unittest test_devices.py
```

or

```bash
python test_devices.py
```

## Contributing

Feel free to open issues or send pull requests. Keep changes small and focused.

## License

This project has no license specified. Add a `LICENSE` file if you wish to make terms explicit.
