# farm-iot

This is a project to monitor the farm environment and control the irrigation system using IoT devices.

There are two parts to this project:
    - The IoT devices, their connections and the data they send and receive
    - Cloud functions that contain the logic to process the data and send commands to the actuators

There are two types of devices: sensors and actuators.

Sensor devices are connected to Azure IoT Hub and send data to it. Actuator devices are connected to Azure IoT Hub and receive and execute commands from it.



<!-- ## Getting Started

The project uses mocked sensors and actuators from Counterfit so python3 is required to gather the data and see the results.

```bash
# Install Counterfit and the required packages
pip install -r requirements.txt

# Run the Counterfit environment
counterfit
```

The sensors app uses pins 0 and 1 -->
