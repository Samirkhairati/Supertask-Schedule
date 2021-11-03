def mint(t):
	h,m = str(t//60),str(t%60)
	if int(h)>=24:
		h = '0'
	if int(h)<10:
		h = '0'+h
	if int(m)<10:
		m = '0'+m
	return h+':'+m
	
# start time
a = 7*60+45
# first slot length
x = 90
# slope
d = -5
# number of slots
n = 12
# minutes per break
b = 10

f = x
for i in range(n):
	print(mint(a)+'-'+mint(a+f)+' →')
	f+=d
	a+=f+b
s = (n/2)*(2*x+(n-1)*d)

print('\nHours Studied: ',int(s//60),':',int(s%60))
print('Total Hours: ',int((s+b*n)//60),':',int((s+b*n)%60))
