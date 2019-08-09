#!/usr/bin/env python

import json
import subprocess
from glob import glob
# print("test")
#


def get_git_hash():
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()


print(get_git_hash())

for path in glob('results/*.json'):
    with open(path) as result_file:
        result = json.load(result_file)
        print(result)
#
import argparse

# with open('results/result-o1909_49.json') as result_file:
#     print(result_file.read())
#     # result = json.load(result_file)
#     # print(result)

# from pypastry.commands import print_
#
# print_.print_results()
