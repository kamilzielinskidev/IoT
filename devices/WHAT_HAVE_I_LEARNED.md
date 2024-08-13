# What have I learned

- How to create IoT Hub device using IoTHubRegistryManager
- There is no way to connect multiple devices on the same connection string
- There is no easy way of connection between devices using IoT Hub, it is possible via Event Grid (but it costs money per hour)
    - I may not need to connect between devices at all
- Concept of Devices is based on connection between Cloud and Device and vice versa, not between Devices
  - If a punctuator needs to react to a sensor, sensor should send a message to the cloud, cloud (Azure Function preferably) should do the logic and send a message to the punctuator
- If many (really many, 10+, 100+) devices are needed, it is better to manage their existance via cloud, not on the device itself. Devices when fresh created, should receive it's own connection string.