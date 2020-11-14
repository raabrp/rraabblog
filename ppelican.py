#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import sys
import cProfile
import pstats

from pelican.__main__ import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    cProfile.run("sys.exit(main())", "profile")
    p = pstats.Stats("profile")
    out = p.print_stats()
    with open("log.txt", 'w') as f:
        f.write(out)
