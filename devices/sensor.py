# This script reads from a counterfit sensor and sends the value to the IoT Hub.
# To read real sensor data, you can remove the counterfit connection and replace counterfit_shims_grove with the appropriate sensor library.

from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)

from time import sleep
from counterfit_shims_grove.adc import ADC
import argparse
from azure.iot.device import IoTHubDeviceClient, Message
import json

parser = argparse.ArgumentParser()
parser.add_argument("--pin", help="Pin number to read from", type=int, required=True)
parser.add_argument("--connection-string", help="Connection string to use", required=True)
args = parser.parse_args()

pin = args.pin
connection_string = args.connection_string

adc = ADC()

device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)

device_client.connect()

while True:
    sensor_value = adc.read(pin)
    msg = Message(json.dumps({"value": sensor_value}))
    device_client.send_message(msg)
    print(f"Sent message: {sensor_value}")
    sleep(5)