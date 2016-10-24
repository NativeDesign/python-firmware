from ntv_firmware import locate_firmware


serial = locate_firmware(
    baudrate = 57600,
    firmware_uid = "uid.202",
    firmware_id = "foo.example.com",
    firmware_version = "1.0"
)

print serial
