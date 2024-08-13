# This script creates a new device in the IoT Hub using the provided connection string and device ID.

from azure.iot.hub import IoTHubRegistryManager
import base64
import argparse
import uuid

parser = argparse.ArgumentParser()
parser.add_argument("--connection-string", help="Connection string to use", required=True)
parser.add_argument("--device-id", help="Device ID to create", required=True)
args = parser.parse_args()

connection_string = args.connection_string
device_id = args.device_id

def main ():
    iothub_registry_manager = IoTHubRegistryManager.from_connection_string(connection_string)
    primary_key = base64.b64encode(uuid.uuid4().bytes).decode('utf8')
    secondary_key = base64.b64encode(uuid.uuid4().bytes).decode('utf8')
    device_state = "enabled"

    new_device = iothub_registry_manager.create_device_with_sas(device_id, primary_key, secondary_key, device_state)
    print(new_device)


if __name__ == '__main__':
    main()