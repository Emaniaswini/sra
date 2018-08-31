N=int(input())
list4=[int(x) for x in raw_input().split()]
list4.sort()
print " ". join(map(str,list4))
