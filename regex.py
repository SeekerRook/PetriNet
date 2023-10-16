import re

arrow = re.compile("\(\(.*\)\)")
print(arrow.findall("((man))((moo))"))