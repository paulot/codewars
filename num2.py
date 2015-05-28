#!/usr/bin/env python2.6
ns = raw_input()
power = 10**len(ns)
n = int(ns)

lim = int('1'+'9'*(len(ns)-1))
upb = 3*(power/10)
mul = (len(ns)-1)*power/100

adj = (n-lim) if (n < upb) else power/10
print 'adj', adj
print n/(power/10)*mul + int(n%10 >= 2) + (adj if adj > 0 else 0)

# from 0-100
adj = (n-19) if (n < 30) else 10
print n/10 + int(n%10 >= 2) + (adj if adj > 0 else 0)
