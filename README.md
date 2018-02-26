# Simple-Substitution
[![Twitter](https://img.shields.io/badge/twitter-@codingo__-blue.svg)](https://twitter.com/codingo_)
A regular expression CTF challenge for CrikeyCon 2018

# Challenge Description
```
\w*?(p).*([a])[^l]*(l)[a-zA-Z\d]*?(a)({)\w*?(o).+([W-w])(h)[^f]+(f).*
\9\3\2g\5t\7\6ste\1s\4\8e\2d}
LZckWnfFS0NyHyjMpObY0aLi:cVJVcVZkWnfFS0NvlQNiyZa{NVCHJ6zWPPI5KXxGZyUo55ywhR8LzVm4KM92kSfi}fzQHpjMpOb0ii?
```

## Search
```
\w*?(p).*([a])[^l]*(l)[a-zA-Z\d]*?(a)({)\w*?(o).+([W-w])(h)[^f]+(f).*
```
## Replace 
```
\9\3\2g\5t\7\6ste\1s\4\8e\2d}
```
# Flag
```
flag{twostepsahead}
```
# Example Solutions
https://regex101.com/r/l1i0Bs/1

```
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
```

