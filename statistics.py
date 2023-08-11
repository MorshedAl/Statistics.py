

import statistics as s
# mean(),harmonic_mean()
# median(),median_high(),median_low()
#mode()
# pvariance()
# pstdev()
# variance()
# stdev()

#mean()
print("mean:")
print(s.mean([1,2,3,4,5]))
print(s.mean([6,3,9,61,0]))

#harmonic_mean()
# [1,2,3,4]
# harmonic_mean= 3/(1/1+1/2+1/3+1/4)
print("harmonic_mean")
print(s.harmonic_mean([1,2,3,4,5]))
print(s.harmonic_mean([6,3,9,61,1]))

print("median():")
print(s.median([1,2,3,4,5]))#বিজোড়
print(s.median_high([1,2,3,4,5,6]))
print(s.median_low([1,2,3,4,5,6]))


#mode() তথা প্রচুরক
print('mode():')
print(s.mode([1,2,3,4,4,5]))
print(s.mode([5,5,2,2,3,4,4,5,9,9]))

#pvariance
#pvariance=£(xi-mean)^2/n
print("pvariance:")
print(s.pvariance([5,3,9,8,1]))

#pstdev
# sd=√variance^2
print("pstdev:")
print(s.pstdev([5,3,9,8,1]))
print("variance:")
print(s.variance([5,3,9,8,1]))
print("stdev:")
print(s.stdev([5,3,9,8,1]))



