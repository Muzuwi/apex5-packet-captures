# SteelSeries Apex 5 keyboard packet captures

This repository contains USB packet captures of communication between the SteelSeries Engine application and the keyboard. 
This was captured on a Windows 10 virtual machine with USBshark. 

The ```pcaps/``` folder contains the raw PCAP files from USBshark. The filenames roughly correspond to the action that was taken inside Steelseries Engine when they were received. 

# Extracting raw feature request packets

The ```extract.py``` script is provided to allow extracting raw SET_FEATURE request data from a given capture file. Raw packet data is then dumped
to the ```commands/{id}/{filename}``` directory, where ```{id}``` is the first byte of the packet, i.e the report ID the packet is sent to. The output packet
name contains the original PCAP file name, and SHA-256 of the packet itself. 

The following packages are required for running the script:

    - pyshark
