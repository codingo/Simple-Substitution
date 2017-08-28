# Simple-Substitution
A regular expression CTF challenge for CrikeyCon 2018

## Search
```
\w*?(p).*([a])[^l]*(l)[a-zA-Z\d]*?(a)({)\w*?(o).+([W-w])(h)[^f]+(f).*
```
## Replace 
```
\9\3\2g\5t\7\6ste\1s\4\8e\2d}
```
