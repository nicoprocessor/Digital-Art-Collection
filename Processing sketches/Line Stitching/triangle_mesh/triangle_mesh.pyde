import math
lines = 20
k = 2

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
    translate(0, height)
    scale(1, -1)
    
    p1 = [-240*k, 90*k]
    p2 = [500*k, -180*k]
    p3 = [200*k, 500*k]
    m1 = p1[:]
    m2 = p2[:]
    m3 = p3[:]
    
    triangle(p1[0],p1[1],p2[0],p2[1],p3[0],p3[1])

    for amt in frange(0, 1.0, 1.0/lines):
        # calculate intermediate points
        m1[0] = lerp(p1[0], p2[0], amt)
        m1[1] = lerp(p1[1], p2[1], amt)
        
        m2[0] = lerp(p2[0], p3[0], amt)
        m2[1] = lerp(p2[1], p3[1], amt)
        
        m3[0] = lerp(p3[0], p1[0], amt)
        m3[1] = lerp(p3[1], p1[1], amt)
        
        # draw lines
        line(m1[0], m1[1], m2[0], m2[1])
        line(m2[0], m2[1], m3[0], m3[1])
        line(m3[0], m3[1], m1[0], m1[1])
        
    save("triangle_parabolics" + str(random(1000)))
    print("Done")
        
