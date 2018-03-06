from modules.BluetoothLightController import BluetoothLightController
import time

if __name__ == '__main__':

    # Bluetooth Light MAC Addresses
    ctrl = BluetoothLightController(
        [
            'C4:BE:84:51:A6:BC',  # Behind TV
            'C4:BE:84:51:CE:6F',  # Desk-Left
            'C4:BE:84:51:DA:D7'   # Behind-Bed
        ]
    )

    while True:
        # Uncomment a mode to enable it.
        #ctrl.orb()
        #ctrl.turn_on()
        #ctrl.turn_off()
        ctrl.orb_night()
