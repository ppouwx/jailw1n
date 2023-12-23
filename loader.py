import sys
import time
import usb.core
import struct

kpf = open("bin/nokpf4u.bin", "rb").read()
rdsk = open("bin/noramdisk4u.bin", "rb").read()
overlay = open("bin/nooverlay4u.bin", "rb").read()
dev = usb.core.find(idVendor=0x05ac, idProduct=0x4141)
if dev is None:
    raise ValueError('Device not found')
dev.set_configuration()

dev.ctrl_transfer(0x21, 4, 0, 0, 0)
dev.ctrl_transfer(0x21, 3, 0, 0, "fuse lock\n")
dev.ctrl_transfer(0x21, 4, 0, 0, 0)
dev.ctrl_transfer(0x21, 3, 0, 0, "sep auto\n")

dev.ctrl_transfer(0x21, 2, 0, 0, 0)
dev.ctrl_transfer(0x21, 1, 0, 0, struct.pack('I', len(kpf)))
dev.write(2,kpf,1000000)
dev.ctrl_transfer(0x21, 4, 0, 0, 0)
dev.ctrl_transfer(0x21, 3, 0, 0, "modload\n")

dev.ctrl_transfer(0x21, 4, 0, 0, 0)
dev.ctrl_transfer(0x21, 3, 0, 0, "palera1n_flags 0x4000000\n")

dev.ctrl_transfer(0x21, 2, 0, 0, 0)
dev.ctrl_transfer(0x21, 1, 0, 0, struct.pack('I', len(rdsk)))
dev.write(2,rdsk,1000000)
dev.ctrl_transfer(0x21, 4, 0, 0, 0)
dev.ctrl_transfer(0x21, 3, 0, 0, "ramdisk\n")

dev.ctrl_transfer(0x21, 2, 0, 0, 0)
dev.ctrl_transfer(0x21, 1, 0, 0, struct.pack('I', len(overlay)))
dev.write(2,overlay,1000000)
dev.ctrl_transfer(0x21, 4, 0, 0, 0)
dev.ctrl_transfer(0x21, 3, 0, 0, "overlay\n")

dev.ctrl_transfer(0x21, 4, 0, 0, 0)
dev.ctrl_transfer(0x21, 3, 0, 0, "xargs  rootdev=md0\n")
dev.ctrl_transfer(0x21, 4, 0, 0, 0)
dev.ctrl_transfer(0x21, 3, 0, 0, "bootx\n")