def sumofAP(n,a,d):
	sum=0
	s=0
	while s<n:
		sum=sum+a
		a=a+d
		s=s+1
	return sum
n,a,d=map(int,raw_input().split())
print(sumofAP(n,a,d))
