NTV Firmware Utils
===



### `ntv_firmware.locate_firmware()`
Locate the serial port of a COM device running the specified firmware version

#### Keyword Arguments
Name              |   Type    |   Description
------------------|-----------|-----------------
 baudrate         |    int    |  Baudrate to open serial port on
 firmware_uid     |   string  |  Unique identifier of the device
 firmware_id      |   string  |  Name/ID of the firmware running on the device
 firmware_version |   string  |  Version of the firmware running on the device
 
#### Example
```python
from ntv_firmware import locate_firmware
com_address = locate_firmware(
    baudrate = 57600,
    firmware_ui = "my-unique-name"
    firmware_id = "example-button-driver"
    firmware_version = "1.0.12"
  );
print com_address
>> "/dev/tty.usbmodem1421"
```
