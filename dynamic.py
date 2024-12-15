#!/usr/bin/env python3

##
# Configuration settings
##


from subprocess import Popen,PIPE
import sys
import json

result = {}
result['webservers'] = {}
result['webservers']['hosts'] = []
result['webservers']['vars'] = {}
result['lbservers'] = {}
result['lbservers']['hosts'] = []
result['lbservers']['vars'] = {}

pipe = Popen(['getent', 'hosts'], stdout=PIPE, universal_newlines=True)

for line in pipe.stdout.readlines():
   s = line.split()
   if s[1].startswith('servere'):
      result['webservers']['hosts'].append(s[1])
   if s[1].startswith('serverf'):
      result['webservers']['hosts'].append(s[1])
   if s[1].startswith('serverd'):
      result['lbservers']['hosts'].append(s[1])


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '--list':
        print(json.dumps(result))
    elif len(sys.argv) == 3 and sys.argv[1] == '--host':
        print(json.dumps({}))
    else:
        print("Requires an argument, please use --list or --host <host>")
