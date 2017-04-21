import os
import re


list_of_dirs = {}
files = []
roots = [root[1:] for root, dirs, files in os.walk('.')]

for root in roots:
    list_of_dirs[root] = len(re.findall('[/]', root))

max_value = max(list_of_dirs.values())

t = "Максимальная глубина папки в этом дереве -- {}"
for key in list_of_dirs:
    if list_of_dirs[key] == max_value:
        print(t.format(list_of_dirs[key]))
        break
