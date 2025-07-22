#!/usr/bin/env python3

import argparse
import os
import locale
import sys

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Files", nargs="?")
parser.add_argument("-c", "--bytes", help="print the byte counts", action="store_true")
parser.add_argument("-l", "--lines", help="print the newline counts", action="store_true")
parser.add_argument("-w", "--words", help="print the word counts", action="store_true")
parser.add_argument("-m", "--chars", help="print the character counts", action="store_true")
args = parser.parse_args()

def count_bytes(file_name):
    file_size_bytes = os.path.getsize(file_name)
    return file_size_bytes

def count_lines(file_name):
    with open(file_name, 'r') as file:
        lines_of_file = len(file.readlines())
    
    return lines_of_file

def count_words(file_name):
    count_words = 0
    with open(file_name, 'r') as file:
        data = file.read()
        w = data.split()
        count_words += len(w)
    
    return count_words

def count_chars(file_name):
    # Get the system's default encoding (usually UTF-8 on Linux)
    system_encoding = locale.getpreferredencoding(False)
    with open(file_name, 'rb') as file:
        binary_data = file.read()
        count_chars = len(binary_data.decode(system_encoding))
    return count_chars

if __name__ == '__main__':
    if args.file:
        file_name = args.file

        if args.bytes:
            print(count_bytes(file_name), file_name)

        if args.lines:
            print(count_lines(file_name), file_name)

        if args.words:
            print(count_words(file_name), file_name)

        if args.chars:
            print(count_chars(file_name), file_name)

        if not args.bytes and not args.lines and not args.words and not args.chars:
            c_bytes = count_bytes(file_name)
            c_lines = count_lines(file_name)
            c_words = count_words(file_name)
            print(c_lines, c_words, c_bytes, file_name)
    else:
        # Final step on-going
        data = sys.stdin.read()
        print(data)