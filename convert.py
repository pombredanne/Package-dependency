#!/usr/bin/python
# -*- coding:utf8 -*-
import json
import time
import argparse
import dependencies

parser = argparse.ArgumentParser(description='Converts Package file to json file')
parser.add_argument('input', metavar='I', type=str,
                    help='Input Packages file')
parser.add_argument('output', metavar='O', type=str,
                    help='Output json file')
parser.add_argument('-r', dest='readable', action='store_true', default=False,
                    help='Is readable json')

args = parser.parse_args()
inName = args.input
outName = args.output
readable = args.readable

start = time.time()
data = dependencies.read_data(inName)
stop = time.time()
print('Parsing file: {} seconds'.format(stop-start))


start = time.time()
with open(outName, 'w') as f:
    if readable:
        json.dump(data, f, indent=4, sort_keys=True)
    else:
        json.dump(data, f)
stop = time.time()
print('Saving json: {} seconds'.format(stop-start))
