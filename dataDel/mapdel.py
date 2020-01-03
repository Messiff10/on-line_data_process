import codecs
import sys
from builtins import int, sorted, tuple, str, set

file_path = sys.argv[1]
maps_sort_path = file_path.replace('.txt', '_sort')
maps = set()
with codecs.open(file_path, encoding='utf-8') as f1:
    for line in f1:
        fileds = line.strip().split('\t')
        if str(fileds[1].strip()) is not "":
            # if line.strip() not in maps:
            maps.add((fileds[0], fileds[1], fileds[2]))
with codecs.open(maps_sort_path, 'w', encoding='utf-8') as f_false:
    for f in sorted(maps, key=lambda x: (x[0], -int(x[2]))):
        s2 = "\t".join(tuple(f))
        f_false.write(s2)
        f_false.write('\n')
print("Finish Line")
