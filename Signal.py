from numpy import fft, arange
from numpy.dual import fft2

data = arange(0,1,10)
f=fft.fft(data, 100)
print (f)