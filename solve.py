#!/usr/bin/python
# -*- coding:utf8 -*-
import json
import argparse
import dependencies

parser = argparse.ArgumentParser(description='Search in repository and solve dependencies')
parser.add_argument('data', metavar='D', type=str, nargs='+',
                    help='json file converted from Packages file')
parser.add_argument('-V', action='store_true', dest='ignoreVersions', default=False,
                    help='ignore versions')

args = parser.parse_args()
ignoreVersions = args.ignoreVersions
dataArgs = args.data

print('Loading data...')
loadedData = {}
for fName in dataArgs:
    print(fName)
    with open(fName, 'r') as f:
        loadedData[fName] = json.load(f)

if ignoreVersions:
    print('WARNING: Ignoring version!')

package = raw_input('package> ')
while package:
    for dataName, data in loadedData.iteritems():
        print(dataName)
        if package in data.keys():
            result, error = dependencies.solve(data, package, ignoreVersions)

            result = ', '.join(map(str, result))
            error = map(lambda x: map(str, x), error)
            error = ', '.join(map(str, error))

            print('\tresult: {}'.format(result))
            print('\terror: {}\n'.format(error))
        else:
            print('\tPackage not found')
    package = raw_input('package> ')
