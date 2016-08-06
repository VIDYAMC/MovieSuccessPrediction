import scipy as sc
import matplotlib.pyplot as plt
import numpy as np

M1=0.1
M2=0.2
M3=0.7
M4=0.3
M5=0.7
n=30
data=sc.genfromtxt('data.tsv',delimiter='\t')
y=data[120:151,8]
d=data[120:151,3]
a=data[120:151,2]
gen=data[120:151,10]
g=gen[gen>9]
a1=a[gen>9]
d1=d[gen>9]
a2=a[gen<=9]
d2=d[gen<=9]
y1=y[gen>9]
y2=y[gen<=9]

def model1(d,a,g):
	return M1*(0.535*d*d - 2.939*d + 8.21) + M2*(0.495*a*a - 2.547*a + 8.705) + M3*(-0.015*g*g+0.585*g+1.703)

def model2(d,a):
	return M4*(0.535*d*d - 2.939*d + 8.21) + M5*(0.495*a*a - 2.547*a + 8.705)

def error(m,y):
	return ((m-y)**2)

m1=model1(d1,a1,g)
m2=model2(d2,a2)
print sum(error(m1,y1))+sum(error(m2,y2))

