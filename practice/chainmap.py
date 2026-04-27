from collections import ChainMap

d1={'a':1}
d2={'b':2}
d3={'c':3}

cm=ChainMap(d1,d2,d3)

print(cm['c'])
