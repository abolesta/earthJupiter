#ALEX BOLESTA
from visual import *

scene.range=2e12
scene.autoscale=0

yr=3.15e7 #Seconds in an Earth year
G=6.67e-11 #Gravitational constant

t=0
dt=0.001*yr #1000 steps per Earth year

sun=sphere(radius=7.0e10, pos=vector(0,0,0), color=color.yellow)
sun.mass=2.0e30

earth=sphere(radius=3.2e10, pos=vector(1.5e11,0,0), color=color.blue)
earth.vel=vector(0,3.0e4,0)
earth.trail=curve(color=color.blue)

jupiter=sphere(radius=3.5e10, pos=vector(1.3e12,0,0), color=color.orange)
jupiter.vel=vector(0,1.0e4,0)
jupiter.trail=curve(color=color.orange)

while (t < 200*yr) :
	rate (1000) #1000 steps per second
	
	earth.pos+=earth.vel*dt #xf=xo+vo*t+0.5*a*t**2
	earth.vel+=-((G*sun.mass)/mag(earth.pos-sun.pos)**3)*(earth.pos-sun.pos)*dt #vf=vo+a*t
	earth.trail.append(pos=earth.pos)

	jupiter.pos+=jupiter.vel*dt #xf=xo+vo*t+0.5*a*t**2
	jupiter.vel+=-((G*sun.mass)/mag(jupiter.pos-sun.pos)**3)*(jupiter.pos-sun.pos)*dt #vf=vo+a*t
	jupiter.trail.append(pos=jupiter.pos)
	
	t+=dt #Step forward