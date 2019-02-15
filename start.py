#!/usr/bin/python

import argparse
import fileMaster

parser = argparse.ArgumentParser(description='Write dummy files with specified content.')
parser.add_argument('file_size', metavar='file size', type=int,
                    help='the new file size')

parser.add_argument('--file_name', default='test.txt',
                    help='the file name you want to write to (WILL BE OVERWRITTEN!), default: test.txt')

parser.add_argument('--fill_byte', dest='fill_byte', default='0',
                    help='byte you want the file be filled with, Ascii char OR byte (0-255)')


args = parser.parse_args()

file_size = args.file_size
file_name = args.file_name
fill_byte = args.fill_byte

# the byte must be always an integer between 0 and 255!
if not fill_byte.isdigit():
    fill_byte = ord(fill_byte)
if fill_byte < 0 or fill_byte > 255:
    raise ValueError('the byte has to be between 0 and 255, got: "{0}"'.format(fill_byte))

print(file_name, file_size, fill_byte)

fm = fileMaster.FileMaster(args.file_size)
fm.create_size(file_size, fill_byte)
