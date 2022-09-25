import pyshark
import argparse
import hexdump
import hashlib
import binascii
import os
from functools import reduce

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="Filename to process")
args = parser.parse_args()

caps = pyshark.FileCapture(args.filename)
for cap in caps:
    if "usbhid" not in cap.frame_info.protocols:
        continue
    if cap.usb.src != "host":
        continue
#    print(cap)
    if "usbhid_setup_brequest" not in cap.DATA.field_names:
        continue
    bRequest = cap.DATA.usbhid_setup_brequest.int_value
#    print("bRequest", bRequest)

    if bRequest != 0x09:
        continue

    converted = map(lambda b: int(b, 16), cap.DATA.usb_data_fragment.split(":"))
    values = []
    for val in converted:
        values.append(val)
    databytes = bytes(values)
    #print(databytes)
    #hexdump.hexdump(databytes)
    
    path = "commands/%s/" % (values[0])
    if not os.path.exists(path):
        os.makedirs(path)
    
    m = hashlib.sha256()
    m.update(databytes)
    name = m.digest().hex()
    fn = os.path.basename(args.filename).replace(".", "_")
    with open(path + fn + "_" + name + ".bin", "wb") as outfile:
        outfile.write(databytes)

