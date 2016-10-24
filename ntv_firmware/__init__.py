import sys
import serial
import glob
from time import sleep

def locate_firmware(
    baudrate = 57600,
    firmware_uid = None,
    firmware_id = None,
    firmware_version = None
    ):
    """

    """
    ## Platform-dependant port enumeration
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/ttyACM[0-9]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.usbmodem[0-9]*')
    else:
        raise EnvironmentError('Unsupported platform')

    for port in ports:
        try:
            with serial.Serial(port, baudrate, timeout=1) as sp:
                sleep(1)
                sp.read(9999)
                sp.write("IDENTIFY\n")
                id = sp.readline()
                _,f_uid,f_id,f_version = id.strip().split(":")

                if firmware_id is not None and firmware_id != f_id:
                    continue
                if firmware_uid is not None and firmware_uid != f_uid:
                    continue
                if firmware_version is not None and firmware_version != f_version:
                    continue

                return port

        except Exception as e:
            print e
            pass
