import random as rnd
import math

offset = 40
padding = 0
theta_steps = 360
cmap = []
noise_y_range = 200
noise_increment = 0.09

def setup():
    size(1200, 1200)
    background(51)
    time = 0
    circles = {}
    
    translate(width/2, height/2)

    # create the circles
    for rho in range(0, height/2 - 100, offset):
        c = []
        for theta in range(theta_steps):
            noise_theta = noise(time)
            noise_rho = noise(time) * noise_y_range
            p = {'rho': rho + noise_rho, 'theta': theta + noise_theta}
            c.append(p)
            
            if theta >= theta_steps//2:
                time -= noise_increment
            else:
                time += noise_increment
        circles[rho] = c
        
    # create color map
    c_begin = color(0,0,0)
    c_end = color(100, 100, 100)
    gradient_step = 1.0/len(circles)
    
    for c in range(len(circles)):
        c_lerp = lerpColor(c_begin, c_end, gradient_step*c)
        cmap.append(c_lerp)
    
            
    # draw the lines
    circle_count = 0
    for c_index, c in sorted(circles.items()):
        for k in range(len(c[:-1])):
            stroke(255)
            strokeWeight(2)
            
            #connect tail with head
            if k == len(c[:-1])-1: #last element
                x1 = c[k]['rho']*cos(math.pi/180*c[k]['theta'])
                y1 = c[k]['rho']*sin(math.pi/180*c[k]['theta'])
                x2 = c[-k-1]['rho']*cos(math.pi/180*c[-k-1]['theta'])
                y2 = c[-k-1]['rho']*sin(math.pi/180*c[-k-1]['theta'])
            else:
                x1 = c[k]['rho']*cos(math.pi/180*c[k]['theta'])
                y1 = c[k]['rho']*sin(math.pi/180*c[k]['theta'])
                x2 = c[k+1]['rho']*cos(math.pi/180*c[k+1]['theta'])
                y2 = c[k+1]['rho']*sin(math.pi/180*c[k+1]['theta'])
            line(x1, y1, x2, y2)
        
            # fill with color
            fill(cmap[circle_count])
            noStroke()
            beginShape()
            
            x1 = c[k]['rho']*cos(math.pi/180*c[k]['theta'])
            y1 = c[k]['rho']*sin(math.pi/180*c[k]['theta'])
            x2 = c[k+1]['rho']*cos(math.pi/180*c[k+1]['theta'])
            y2 = c[k+1]['rho']*sin(math.pi/180*c[k+1]['theta'])
            
            if cos(math.pi/180*c[k]['theta']) > 0:
                vertex(x1, y1)
                vertex(width, y1)
                vertex(width, y2)
                vertex(x2, y2)
                endShape()

        circle_count += 1
        save("joy_division_experiment_" + str(rnd.random()*1000) + ".png")
