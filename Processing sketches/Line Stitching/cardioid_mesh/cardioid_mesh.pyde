import math
lines = 300
line_skip = 1
radius_x, radius_y = 900, 900

def frange(start, stop, step):
    while start < stop:
        yield start
        start += step

def setup():
    size(1200, 1200)
    background(51)
    ellipseMode(RADIUS)
    stroke(255)
    noFill()
    strokeWeight(1)

    # center the coordinate system
    translate(width/2, height/2)
    rotate(math.pi/3)
    scale(1, -1)
    
    ellipse(0, 0, radius_x, radius_y)
    p1 = [0,0]
    p2 = [0,0]
    counter = 0

    for theta in frange(0, 2*math.pi, 2*math.pi/lines):
        # calculate intermediate points
        p1[0] = radius_x * math.cos(theta) 
        p1[1] = radius_y * math.sin(theta)
        counter += 1
        
        theta_skip = theta + (2*math.pi/lines)*line_skip*counter
        p2[0] = radius_x * math.cos(theta_skip) 
        p2[1] = radius_y * math.sin(theta_skip)
        
        # draw lines
        line(p1[0], p1[1], p2[0], p2[1])
        
    save("cardioid_standard" + str(random(1000)))
    print("Done")
        
