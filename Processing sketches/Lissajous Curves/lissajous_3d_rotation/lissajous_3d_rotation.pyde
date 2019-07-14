import math

total_points = 1e4
A,B,C,a,b,c,delta=500,500,1000,4,6,8,-1
t_increment=1e-3

color_palette_flare = [color(241, 40, 16), color(245, 175, 25)]

def setup():
    size(1100, 1100, P3D)
    background(51)
    ellipseMode(CENTER)
    strokeWeight(10)
    smooth()
    translate(width/2, height/2, -1000)
    
    for t in frange(0.0, 20.0, t_increment):
        print(t)
        x = A*sin(a*t+delta)
        y = B*sin(b*t)
        z = C*sin(c*t)
        stroke(lerpColor(color_palette_flare[0], 
                        color_palette_flare[1], t))
        point(x,y,z)
        
        
def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step
    
