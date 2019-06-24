import math
lines = 40
radius_x = 550
radius_y = 550
axes = 20

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

    m1 = [0,0]
    m2 = [0,0]
    
    for theta in frange(0, 2*math.pi, 2*math.pi/axes):
        for amt in frange(0, 1.0, 1.0/lines):
            theta_next = theta + (2*math.pi/axes)
            p0 = [0,0]
            p1 = [radius_x * math.cos(theta), radius_y * math.sin(theta)]
            p2 = [radius_x * math.cos(theta_next), radius_y * math.sin(theta_next)]
                      
            m1[0] = lerp(p1[0], p0[0], amt)
            m1[1] = lerp(p1[1], p0[1], amt)
            
            m2[0] = lerp(p2[0], p0[0], 1.0 - amt)
            m2[1] = lerp(p2[1], p0[1], 1.0 - amt)
            
            line(m1[0], m1[1], m2[0], m2[1])
    save("star_parabolic" + str(random(1000)))
    print("Done")
        
