from modules.BluetoothLightController import BluetoothLightController
import time

if __name__ == '__main__':

    ctrl = BluetoothLightController(
        [
            'C4:BE:84:51:A6:BC',  # Behind TV
            'C4:BE:84:51:CE:6F',  # Desk-Left
            'C4:BE:84:51:DA:D7'   # Behind-Bed
        ]
    )

    while True:
        #print("Turning on Orb Mode")
        #start = time.time()
        #ctrl.orb()
        #end = (time.time() - start)
        #print('Elapsed Time: ', end)
        #print("Turning Off")
        #ctrl.turn_off()
        #print("Turning On")
        #ctrl.turn_on()
        ctrl.orb_night()