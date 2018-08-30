N=int(input())
list=[int(x) for x in raw_input().split()]
list.sort()
print " ". join(map(str,list))
