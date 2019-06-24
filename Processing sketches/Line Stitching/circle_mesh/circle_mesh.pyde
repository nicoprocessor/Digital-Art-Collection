import math
lines = 40
line_skip = 10
radius_x, radius_y = 500, 500

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
    scale(1, -1)
    
    ellipse(0, 0, radius_x, radius_y)
    p1 = [0,0]
    p2 = [0,0]

    for theta in frange(0, 2*math.pi, 2*math.pi/lines):
        # calculate intermediate points
        p1[0] = radius_x * math.cos(theta) 
        p1[1] = radius_y * math.sin(theta)
        
        theta_skip = theta + (2*math.pi/lines)*line_skip
        p2[0] = radius_x * math.cos(theta_skip) 
        p2[1] = radius_y * math.sin(theta_skip)
        
        # draw lines
        line(p1[0], p1[1], p2[0], p2[1])
        
    save("circle_parabolics" + str(random(1000)))
    print("Done")
        
