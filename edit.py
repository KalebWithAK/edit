#! /usr/bin/env python3
import os
import sys

editor = 'visual studio code' # Change to your preferred IDE.

if len(sys.argv) > 1:
    src = sys.argv[1]
    if len(sys.argv) == 3:
        editor = sys.argv[2]
    os.system('open -a \'%s\' %s' % (editor, src))
    print('opened %s with %s' % (src, editor))
else:
    print('Usage:\n  %s: ./edit <src>' % editor)
    print('  custom editor: ./edit <src> <editor>')