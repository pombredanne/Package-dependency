#!/usr/bin/python
# -*- coding:utf8 -*-
from distutils.version import LooseVersion
import re
import os


def read_data(fName):
    result = {}
    regex = re.compile(r' \((.*)\)')
    with open(fName, 'r') as f:
        size = os.fstat(f.fileno()).st_size
        while f.tell() != size:
            data = {}
            packData = ''
            while True:
                line = f.readline()
                if line != '\n':
                    packData += line
                else:
                    break
            packData = packData.rstrip('\n').split('\n')
            for i in packData:
                if i.startswith(' '):
                    continue
                key, value = i.split(': ', 1)
                data[key] = value

            if 'Depends' not in data.keys():
                depends = []
            else:
                depends = data['Depends'].split(', ')

                n = -1
                for i in depends:
                    n += 1
                    if ' | ' in i:
                        depends[n] = i.split(' | ')
                    else:
                        depends[n] = [i]

                nd = -1
                for i in depends:
                    np = -1
                    nd += 1
                    for package in i:
                        np += 1
                        splitted = regex.split(package)
                        if len(splitted) != 1:  # python (>= 1.2.5), python3 (= 1.4.2)
                            name = splitted[0]
                            version = splitted[1] if len(splitted) > 1 else '>= 0.0.0'
                            version = version.split(' ')
                        elif ':' in package:  # python:any, python3:any
                            splitted = package.split(':')
                            name = splitted[0]
                            version = splitted[1]
                            if version == 'any':
                                version = '>= 0.0.0'
                        else:
                            name = package
                            version = '>= 0.0.0'
                        depends[nd][np] = {'version': version, 'name': name}

            keys = data.keys()
            result[data['Package']] = {
                'package': data['Package'],
                'filename': data['Filename'],
                'version': data['Version'],
                'size': int(data['Size']),
                'SHA1': data['SHA1'],
                'architecture': data['Architecture'],

                'installed size': int(data['Installed-Size']) if 'Installed-Size' in keys else None,
                'section': data['Section'] if 'Section' in keys else None,
                'description': data['Description'] if 'Description' in keys else None,
                'homepage': data['Homepage'] if 'Homepage' in keys else None,
                'maintanier': data['Maintainer'] if 'Maintainer' in keys else None,

                'depends': depends
            }
            # print('{p}: Done'.format(p=data['Package']))
    return result


def solve(data, package, ignoreVersions=False):
    error = []
    result = []
    not_solved = [data[package]]
    while not_solved:
        current = not_solved.pop(0)
        if current['package'] in result:
            continue
        for dep in current['depends']:
            n = -1
            version_ok = False
            while not version_ok and not ignoreVersions:
                n += 1
                '''print('{cur}: dependency №{n}: {p} {v}{ver}'.format(
                    cur=current['package'], n=n, v=dep[n]['version'][0], ver=dep[n]['version'][1],
                    p=dep[n]['name']))'''
                try:
                    need_version = LooseVersion(dep[n]['version'][1])
                    get_version = LooseVersion(data[dep[n]['name']]['version'])
                except IndexError:
                    error.append(dep)
                    break
                if   dep[n]['version'][0] == '<<': version_ok = (get_version <  need_version)
                elif dep[n]['version'][0] == '<=': version_ok = (get_version <= need_version)
                elif dep[n]['version'][0] == '>>': version_ok = (get_version >  need_version)
                elif dep[n]['version'][0] == '>=': version_ok = (get_version >= need_version)
                elif dep[n]['version'][0] == '=' : version_ok = (get_version == need_version)
            else:
                not_solved.append(data[dep[n]['name']])
        result.append(current['package'])

    resError = []
    for i in error:
        packError = []
        for pack in i:
            packError.append(pack['name'])
        resError.append(packError)
    return result, resError
