# https://zerojudge.tw/ShowProblem?problemid=a020

import sys
import re


def checkID2(s):

    pat = '([A-Z]{1})([1-2]{1}\\d{8})'
    county = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15',
              'G': '16', 'H': '17', 'I': '34', 'J': '18', 'K': '19', 'L': '20',
              'M': '21', 'N': '22', 'O': '35', 'P': '23', 'Q': '24', 'R': '25',
              'S': '26', 'T': '27', 'U': '28', 'V': '29', 'W': '32', 'X': '30',
              'Y': '31', 'Z': '33'}
    w = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    p = re.compile(pat)
    m = p.match(s)
    if m:
        s = county[m.group(1)] + m.group(2)
        checkSum = 0
        for i in range(len(s)):
            x = int(s[i])
            checkSum += x * w[i]
        if checkSum % 10 == 0:
            print('real')
        else:
            print('fake')
    else:
        print('error')

for s in sys.stdin:
    checkID2(s)

