#!/usr/bin/python
# -*- coding:utf8 -*-
import json
import argparse
import dependencies

parser = argparse.ArgumentParser(description='Search in repository and solve dependencies')
parser.add_argument('data', metavar='D', type=str,
                    help='json file converted from Packages file')
parser.add_argument('-V', dest='ignoreVersions', type=bool, help='ignore versions')

args = parser.parse_args()
data = args.data
ignoreVersions = args.ignoreVersions

print('Loading data...')
with open(data, 'r') as f:
    data = json.load(f)


if ignoreVersions:
    print('WARNING: Ignoring version!')

package = raw_input('package> ')
while package:
    if package in data.keys():
        result, error = dependencies.solve(data, package, ignoreVersions)

        result = ', '.join(map(str, result))
        error = map(lambda x: map(str, x), error)
        error = ', '.join(map(str, error))

        print('\nresult: {}'.format(result))
        print('error: {}'.format(error))
    else:
        print('Package not found')
    package = raw_input('package> ')
