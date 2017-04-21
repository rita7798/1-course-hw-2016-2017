##Написать программу, которая рисует дерево текущей папки в таком виде:
##--folder1
## --folder4
##       file4
##       file5
## --folder5
##--folder2
## file2
## file3
##--folder3

import os
import re


for d in os.listdir():
                if d[0] == ".":
                    continue
                else:
                    name = d
                    print(name)
                    if re.search('[.]', name) != None:
                        t1 = "  {}"
                        print(t1.format(name))
                    else:
                        t = "--{}"
                        print(t.format(name))
                        path = "{}"
                        folder = os.listdir(path.format(name))
                        for j in range(len(folder)):
                            if folder[j][0] == ".":
                                continue
                            else:
                                if re.search('[.]', folder[j]) != None:
                                    t3 = "      {}"
                                    print(t3.format(folder[j]))
                                else:
                                    t2 = " --{}"
                                    print(t2.format(folder[j]))
                                    folder1 = os.listdir(os.path.join(path.format(name), path.format(folder[j])))
                                    for k in range(len(folder1)):
                                        if folder1[k][0] == ".":
                                            continue
                                        else:
                                            if re.search('[.]', folder1[k]) != None:
                                                t5 = "          {}"
                                                print(t5.format(folder1[k]))
                                            else:
                                                t4 = "  --{}"
                                                print(t4.format(folder1[k]))
