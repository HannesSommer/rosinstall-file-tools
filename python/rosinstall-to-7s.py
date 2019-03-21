#!/usr/bin/env python
from __future__ import print_function
import sys
import yaml

import argparse


parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-d', '--debug', default=False, action='store_true')
parser.add_argument('-v', '--verbose', default=False, action='store_true')
parser.add_argument('-n', '--dry-run', default=False, action='store_true')
parser.add_argument("rosinstall_files", nargs='+')


args = parser.parse_args()


def error(text, exit_code=None):
    print(text, file)
    if exit_code is not None:
        sys.exit(exit_code)


for fp in args.rosinstall_files:
    with open(fp, 'r') as f:
        for item in yaml.load_all(f).next():
            if 'git' in item:
                d = item['git']
                print("""- name: {name}
  repository: {repo}
  commit: master
""".format(name=d['local-name'], repo=d['uri']))
            else:
                error("Only git entries supported, yet! Skipping %s" % item)
