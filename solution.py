# coding=utf8
import re

input_str = "LZckWnfFS0NyHyjMpObY0aLi:cVJVcVZkWnfFS0NvlQNiyZa{NVCHJ6zWPPI5KXxGZyUo55ywhR8LzVm4KM92kSfi}fzQHpjMpOb0ii?"

regex = r"\w*?(p).*([a])[^l]*(l)[a-zA-Z\d]*?(a)({)\w*?(o).+([W-w])(h)[^f]+(f).*"
replace = "\\9\\3\\2g\\5t\\7\\6ste\\1s\\4\\8e\\2d}"

result = re.sub(regex, replace, input_str, 0)

print("Input string: %s" % input_str)
print("Search: %s" % regex)
print("Replace: %s" % replace)
print("-" * 25)
print("Result: %s" % result)
