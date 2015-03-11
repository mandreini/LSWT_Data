import numpy
import matplotlib.pyplot as plt

def round_to_half(num):
    floor = num // 0.5
    if num % 0.5 > 0.25:
        floor = floor + 1 
    return float(floor * 0.5)

def plot_pressure(alpha):
    #input
        #alpha - float: angle of attack in degrees, rounded to nearest 0.5

    #output
        #returns and displays matplotlib plot if alpha is in the data
        #returns and error string if alpha is not

    alpha = float(alpha)
    if alpha in pressure_dist.keys():
        x  = range(len(pressure_dist[alpha][0]))
        y1 = pressure_dist[alpha][0]
        y2 = pressure_dist[alpha][1]

        plt.plot(x, y1, label = "Lower side")
        plt.plot(x, y2, label = "Upper side")
        plt.ylabel("Cp")
        plt.title("Pressure coefficient distribution for angle of attack " + str(alpha))
        plt.legend(loc="best")
        plt.show()
        return plt
    else:
        return "Error: alpha not found in pressure distribution."

def plot_values(xval, yval):
    #inputs:
        #xval - string: x value for plotting, case sensitive
        #yval - string: y value for plotting, case sensitive
    #outputs:
        #returns and shows matplotlib plot if both xval and yval are in data.
        #returns error string if not.
    if xval not in ordered_data.keys():
        return "'" + xval + "' not found in data."
    if yval not in ordered_data.keys():
        return "'" + yval + "' not found in data."

    plt.plot(ordered_data[xval], ordered_data[yval])
    plt.xlabel(xval)
    plt.ylabel(yval)
    plt.title("Relationship between " + xval + " and " + yval + "in low speed wind tunnel test.")
    plt.show()
    return plt

data = numpy.genfromtxt("CorrData.csv", delimiter=",", skip_header=2)

f = open("CorrData.csv")
firstline = f.readline()
f.close()

firstline = firstline.split(",")
firstline = [i.strip() for i in firstline]
firstline.pop(-1)

ordered_data  = {} #keys are colum headers
pressure_dist = {} #keys are alpha, rounded to nearest half

#get columns
for line in range(len(data)):
    colCat               = firstline[line]
    column               = data[:,line]
    ordered_data[colCat] = column

#get pressure distribution for an angle of attack
#CPu_### -> firstline[15:39]
#Cpl_### -> firstline[40:63]
for line in range(len(data)):
    upperDist              = data[line,15:39] #CPu_001 - CPu_024
    lowerDist              = data[line,40:64] #CPl_001 - CPl_024
    alpha                  = round_to_half(data[line,1])
    pressure_dist[alpha]   = [upperDist, lowerDist]


    
