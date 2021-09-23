#!/usr/bin/python

import subprocess
import re

#subprocess.run("sudo apt-get install jq")
#subprocess.run("brew install jq")
#subprocess.run("jq -s 'reduce .[] as $item ({}; reduce ($item | keys_unsorted[]) as $key (.; $item[$key] as $val | ($val | type) as $type | . [$key] = if ($type == "array") then (.[$key] + $val | unique) elif ($type == "object") then (.[$key] + $val) else $val end))' *.json", shell=True)

subprocess.run("./combine_json > result1.json", shell=True)

file = open('result1.json', 'r')
lines = file.readlines()
count = 0

for line in lines:
    count += 1
    line = re.sub("(code\d)", "code", line)
    print(line)

