# Simple-Substitution
A regular expression CTF challenge for CrikeyCon 2018

# Challenge
```
\w*?(p).*([a])[^l]*(l)[a-zA-Z\d]*?(a)({)\w*?(o).+([W-w])(h)[^f]+(f).*
LZckWnfFS0NyHyjMpObY0aLi:cVJVcVZkWnfFS0NvlQNiyZa{NVCHJ6zWPPI5KXxGZyUo55ywhR8LzVm4KM92kSfi}fzQHpjMpOb0ii?
```
## Example
https://regex101.com/r/l1i0Bs/1
## Search
```
\w*?(p).*([a])[^l]*(l)[a-zA-Z\d]*?(a)({)\w*?(o).+([W-w])(h)[^f]+(f).*
```
## Replace 
```
\9\3\2g\5t\7\6ste\1s\4\8e\2d}
```
