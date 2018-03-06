import os
import subprocess


class BluetoothLight(object):

    def __init__(self, address):
        self.address = address
        self.rgb_handle = '0x002e'
        self.bt_packet_head = '78'
        self.bt_packet_tail = '0000ee'
        self.red = '00'
        self.green = '00'
        self.blue = '00'

    def set_color(self, red, green, blue):

        self.red = hex(int(red))[2:4].zfill(2)
        self.green = hex(int(green))[2:4].zfill(2)
        self.blue = hex(int(blue))[2:4].zfill(2)

        msg = [
            'gatttool',
            '-i', 'hci0',
            '-b', self.address,
            '--char-write-req',
            '-a', self.rgb_handle,
            '-n', self.bt_packet_head + self.red + self.green + self.blue + self.bt_packet_tail
        ]

        nullfile = open(os.devnull, 'w')
        subprocess.Popen(msg, stdout=nullfile, stderr=nullfile)
