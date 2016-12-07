# -*- coding: utf-8 -*-
from sys import stdout
while 1:
    cache = int(raw_input('Please input the number:'))
    num = int(cache)
    pf = []
    i = 2
    stdout.write(' The prime facors of 'str(num)+' : ')
    while num <> 1:
        if num % i ==0:
            pf.append(i)
            num = num / i
        else:
            i +=1       
    for i in range(0,len(pf)-1):
        stdout.write(str(pf[i]))
        stdout.write("、")
    print pf[-1]
    print pf[:]