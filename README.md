# BruteRatel-DetectionTools
A collection of Tools and Rules for decoding Brute Ratel C4 badgers

All tools and rules are based on samples identified by PaloAlto in their report https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/


### Yara Rule

The yara rule has been tested against the samples included in the Unit42 report and additioanl samples identifed by this rule

```
❯ yara rule.yar
BruteRatel ./hacker.exe
BruteRatel ./badger_x64.exe
BruteRatel ./trustwave.exe
BruteRatel ./adi_badger_x64_2.exe
BruteRatel ./npser.exe
BruteRatel ./twitter.exe
BruteRatel ./X64 Brute Ratel C4 Windows Kernel Module.bin
BruteRatel ./sample2.exe
BruteRatel ./HorionInjector.exe
BruteRatel ./http_badger_x64.exe
BruteRatel ./sample1.exe
```


### Config Parser

The Config Decoder has been tested against the samples idetified in the Unit42 report and additioanl samples foudn using the yara rule above. 

Only a single static Key has been obeserved in samples so far. 

```
❯ python3 decoder.py sample1.exe                                                           
[+] Brute Ratel C4 Config Extractor by Immersive Labs
[+] Reading contents of file "sample1.exe"
  [-] Config Pattern Detected
  [-] May be encrypted testing key b'bYXJm/3#M?:XyMBF'
[+] Printing config to screen

||0|1|192.168.2.9|443|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36|12345|P@ssw0rd|/admin||

```