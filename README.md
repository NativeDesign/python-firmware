NTV Firmware Utils
===



### `ntv_firmware.locate_firmware()`
Locate the serial port of a COM device running the specified firmware version

#### Keyword Arguments
Name              |   Type    |   Description
------------------|-----------|-----------------
 baudrate         |    int    |  Baudrate to open serial port on.
 firmware_id      |   string  |  Name/ID of the firmware running on the device.
 firmware_version |   string  |  Version of the firmware running on the device.
 firmware_uid     |   string  |  Unique identifier of the device.
 outstream        |    file   |  Output stream for logging. Defaults to `sys.stdout`.
 silent           |  boolean  |  Don't output anything to outstream.
 delay            |    int    |  Seconds to delay between iterations.
 max_attempts     |    int    |  Number of iterations to search for. Defaults to `0` (infinite).

#### Example
```python
from ntv_firmware import locate_firmware
com_address = locate_firmware(
    baudrate = 57600,
    firmware_uid = "my-unique-name"
    firmware_id = "example-button-driver"
  );
print com_address
>> "/dev/tty.usbmodem1421"
```
