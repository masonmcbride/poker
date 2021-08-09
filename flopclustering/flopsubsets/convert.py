from collections import defaultdict
import pprint

flops = defaultdict(int)

orig_file = open('184flops.txt', 'r')
entries = orig_file.readlines()

for entry in entries:
    flop, freq = entry.strip().split(":")
    flops[flop] = freq

sorted_flops = {k: v for k, v in reversed(sorted(flops.items(), key=lambda item: item[1]))}

with open('sorted184flops.txt', 'w') as out_file:
    for flop, freq in sorted_flops.items():
        out_file.write(flop + ': ' + freq + '\n')
