# https://zerojudge.tw/ShowProblem?problemid=c716 c716: Johnny B. Goode

import sys


s = sys.stdin.readline()
s = s.strip('\n').strip('\r')
while s:
    print('Go, ' + s + ', go go')
    s = sys.stdin.readline()
    s = s.strip('\n').strip('\r')