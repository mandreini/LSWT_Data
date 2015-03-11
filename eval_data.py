import numpy
import matplotlib.pyplot as plt

def determine_time(nt):
    #nt is decimal of day past. 0 is midnight, 0.5 noon, 0.75 6PM etc
    pt = nt * 24
    hr = int(pt)
    m = int(round((pt - hr) * 60))
    shr, shm = str(hr), str(m)
    if len(shm) == 1:
        shm += "0"
    return float(shr + "." + shm)
    #float of hour.minute - purely for readibiliy purposes, might remove
    
data = numpy.genfromtxt("ExtraData.csv", delimiter=",", skip_header=1)

#get time in hr.m fashion
for line in range(len(data)):
    t = determine_time(data[line,1])
    data[line,0] = t

#need a way to ascertain that there isn't a bunch of nan rows or columns!

#split data accordingly
utime = data[:,0]           #[hr.m]
ptime = data[:,1]           #[dec of day]
alpha = data[:,2]           #[deg]
temp  = data[:,3]           #[deg C]
p     = data[:,4] * 100     #[Pa]
dpb   = data[:,5]           #[Pa}
rho   = data[:,6]           #[kg/m^3]
v     = data[:,7]           #[m/s]
Re    = data[:,8]           #[-]

#plot 1: time - effects
plt.subplot(221)
plt.title("time-temperature")
plt.xlabel("time [hr.m]")
plt.ylabel("temperature [deg C]")
plt.plot(utime, temp)

plt.subplot(222)
plt.title("time-pressure")
plt.xlabel("time [hr.m]")
plt.ylabel("pressure [Pa]")
plt.plot(utime, p)

plt.subplot(223)
plt.title("time-density")
plt.xlabel("time [hr.m]")
plt.ylabel("density [kg/m^3]")
plt.plot(utime, rho)

plt.subplot(224)
plt.title("time-velocity")
plt.xlabel("time [hr.m]")
plt.ylabel("velocity [m/s]")
plt.ylim(min(v),max(v)+0.1) 
plt.plot(utime, v)

plt.tight_layout()
plt.savefig("timeEffects.png")
plt.figure()

#plot 2: alpha - effects

plt.subplot(211)
plt.title("alpha-deltaPb")
plt.xlabel("alpha [deg]")
plt.ylabel("deltaPb [Pa]")
plt.plot(alpha, dpb)

plt.subplot(212)
plt.title("alpha-Re")
plt.xlabel("alpha [deg]")
plt.ylabel("Re [-]")
plt.plot(alpha, Re)

plt.tight_layout()
plt.savefig("alphaEffects.png")
plt.show()


