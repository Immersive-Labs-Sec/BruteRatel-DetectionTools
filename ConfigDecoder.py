# Copyright (C) 2022 Kevin Breen, Immersive Labs
# https://github.com/Immersive-Labs-Sec/BruteRatel-DetectionTools
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import re
import argparse
from base64 import b64decode

from Crypto.Cipher import ARC4

CONFIG_PATTERN = b'\x50\x48\xb8(.*)\x50\x68'
DEFAULT_KEY = b'bYXJm/3#M?:XyMBF'

def decrypt(key, data):
    # Init the Cipher with the key
    cipher = ARC4.new(key)

    # Decode Base64
    decoded = b64decode(data)

    # Then Decrypt
    decrypted = cipher.decrypt(decoded)
    return decrypted

def main(file_path, key):
    print(f'[+] Reading contents of file "{file_path}"')
    file_contents = open(file_path, 'rb').read()
    pattern_match = re.search(CONFIG_PATTERN, file_contents)

    if pattern_match:
        raw_config = pattern_match.group(1)
        print('  [-] Config Pattern Detected')

        sections = raw_config.split(b'PH\xb8')
        sections.reverse()

        config = b''.join(sections)
        # This is a quick test for encrypted config
        if b'|' not in config:
            print(f'  [-] May be encrypted testing key {key}')
            config = decrypt(key, config)
        print("[+] Printing config to screen")

        print(f'\n{config.decode()}')


parser = argparse.ArgumentParser(description='Brute Ratel Config Extractor')
parser.add_argument('filepath', help='Path to file')
parser.add_argument('--key', default=DEFAULT_KEY, help='Change the Default key for encrypted configs')
args = parser.parse_args()


print('[+] Brute Ratel C4 Config Extractor by Immersive Labs')

if os.path.exists(args.filepath):
    main(args.filepath, args.key)
else:
    print('[!] File does not exist or can not be accessed.')