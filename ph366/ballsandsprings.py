import matplotlib as plt
import numpy as np
import pylab
import math

pylab.ion() # this turns on interaction---needed for animation

numballs = 240 # number of balls
scale = 20 # scale for wavelength
runtime = 100

t = 0 # time in seconds
delta_x = .1 # distance between balls in meters
delta_t = .1 # time step in seconds
mass = 10 # mass of balls in kilograms
tension = 10 # tension of springs in newtons

current = np.zeros(numballs) # array of current positions of balls
previous = np.zeros(numballs)  # array of previous positions of balls
future = np.zeros(numballs)  # array of future positions of balls

def initial_positions(i): # plot initial positions
        global current, previous, future, t
        #for i in range(0,i-1):
        #        current[i] = pylab.sin(scale*i*math.pi/(numballs-1))
        current[20] = 15
        future[20] = 15
        line.set_ydata(current)
        pylab.draw()

def rebuild_arrays(i):
        global current, previous, future, t
        for i in range(1,i-1):
                future[i] = 2*current[i] - previous[i] + ((tension*delta_t**2)/(mass*delta_x))*(current[i+1] + current[i-1] - 2*current[i])

        line.set_ydata(current)
        pylab.draw()
        previous[:] = current
        current[:] = future

x = pylab.arange(0,numballs,1) # space the xs

line, = pylab.plot(x, current, 'o-')
pylab.xlabel('Balls')
pylab.ylabel('Displacement')
pylab.ylim([-2*scale,2*scale])

initial_positions(numballs)

while t < runtime:
        rebuild_arrays(numballs)
        t += delta_t

# array, array, array = function(array, array, array)
# def function:
#   return array, array, array
