import random as rnd
import math

offset = 30
padding = 0
c_begin = color(0)
c_end = color(100)
step_resolution = 1
lines = {}
cmap = []
noise_y_range = 200
noise_increment = 0.02

def setup():
    size(1080, 2340)
    background(0)
    t = 0

    # create the lines
    for y in range(10, height - 200, offset):
        l = []
        for x in range(padding, width - padding, step_resolution):
            dist_to_center = abs(x - width/2)
            noise_x = noise(t)
            noise_y = noise(t) * noise_y_range
            p = {'x': x + noise_x, 'y': y + noise_y}
            l.append(p)
            t += noise_increment
        lines[y] = l
        
    # create color map
    gradient_step = 1.0/len(lines)
    
    for c in range(len(lines)):
        c_lerp = lerpColor(c_begin, c_end, gradient_step*c)
        cmap.append(c_lerp)
    
            
    # draw the lines
    line_count = 0
    for c, l in sorted(lines.items()):
        for k in range(len(l[:-1])):
            stroke(255)
            strokeWeight(2.5)
            line(l[k]['x'], l[k]['y'], l[k+1]['x'], l[k+1]['y'])

            if c != len(lines):          
                #fill the region below each line
                fill(cmap[line_count])
                noStroke()
                beginShape()
                vertex(l[k]['x'], l[k]['y'])
                vertex(l[k+1]['x'], l[k+1]['y'])
                vertex(l[k+1]['x'], height)            
                vertex(l[k]['x'], height)
                endShape()
            else:
                pass
        line_count += 1
    save("joy_division_experiment_" + str(rnd.random()*1000) + ".png")
