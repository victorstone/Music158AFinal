from base import *
import csv, sys, numpy as np
import serial, pdb

ser = serial.Serial('/dev/tty.usbmodem1421', 9600, timeout=10)
NUM_CAPS_AND_POTS = 4

class SequenceSource:
    def __init__(self):
        self.saved_pitch_data = {}
        self.saved_mod_data = {}

    def get_cap_data(self, cap_num):
        assert cap_num in range(NUM_CAPS_AND_POTS)
        return int(ser.readline().split('+')[0].split(',')[cap_num])

    def get_pitch_data(self, pot_num):
        assert pot_num in range(NUM_CAPS_AND_POTS)
        return int(ser.readline().split('+')[1].split(',')[pot_num])

    def get_duration_data(self):
        return int(ser.readline().split('+')[2])

    def get_mod_data(self):
        return int(ser.readline().split('+')[3])

if __name__ == '__main__':
    length = 100
    seq = SequenceSource()
    while True:
        pm = PacketManager(length)
        pm.add_data_source(seq)
        pm.send_to_max()
    ser.close()
