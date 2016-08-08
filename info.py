#!/usr/bin/python
# -*- coding:utf8 -*-
import json
import argparse
from collections import OrderedDict


parser = argparse.ArgumentParser(description='Get info about package.')
parser.add_argument('data', metavar='D', type=str, nargs='+',
                    help='Json file converted from Packages file')

args = parser.parse_args()
dataArgs = args.data

print('Loading data...')
loadedData = {}
for fName in dataArgs:
    print(fName)
    with open(fName, 'r') as f:
        loadedData[fName] = json.load(f)

words = OrderedDict([
    ('package', 'Package name'),
    ('description', 'Description'),
    ('maintanier', 'Maintainer'),
    ('homepage', 'Homepage'),
    ('version', 'Version'),
    ('section', 'Section'),
    # ('installed size', 'Installed size'),  # Only in Debian, not Ubuntu
    ('size', 'Download size'),
    ('architecture', 'Architecture'),
    ('filename', '.deb path'),
    ('SHA1', 'SHA1'),
])

package = raw_input('\npackage> ')
while package:
    if package == '/all':
        for dataName, data in loadedData.iteritems():
            print(dataName)
            packages = data.keys()
            packages = [packages[i:i + 3] for i in xrange(0, len(packages), 3)]
            packages = map(lambda x: map(str, x), packages)
            packages = map(', '.join, packages)
            print('\n\t'.join(map(str, packages)))
    else:
        for dataName, data in loadedData.iteritems():
            print(dataName)
            if package in data.keys():
                for key, value in words.iteritems():
                    result = data[package][key]
                    if result:
                        print('\t{v}: {r}'.format(v=value, r=result))
            else:
                print('\tPackage not found')
    try:
        package = raw_input('\npackage> ')
    except (KeyboardInterrupt, EOFError) as e:
        package = ''
