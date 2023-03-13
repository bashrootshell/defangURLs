#!/usr/bin/env python3

# -*- coding: utf-8 -*-
__author__ = "Marcos Cicero"
__license__ = "BSD"
__version__ = "1.0.0"

""" PEP8 Compliant - Complex is better than complicated. """ 

from sys import argv
from re import findall

main_regex = '(?:ftp|sftp|https?)://(?:\w+\.)*\w+(?:[-./?=&%]\w*)*'
replace_pattern = [("/", "\/"), (".", "[.]"), ("tt", "XX")]

FILE = argv[1] if len(argv) == 2 else exit("Provide a file name.")

with open(FILE) as input, open("defanged.txt", "w") as output:

    content = input.read()
    matchurl = findall(main_regex, content)
    for url in set(matchurl):
        [url := url.replace(a, b) for a, b in replace_pattern]
        print(url, file=output)
