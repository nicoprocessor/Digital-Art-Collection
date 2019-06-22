import random as rnd
import math

offset = 50
padding = 0
theta_steps = 360
cmap = []
noise_y_range = 100
noise_increment = 0.009

def setup():
    size(800, 800)
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
    c_begin = color(255, 0, 0)
    c_end = color(50, 0, 150)
    gradient_step = 1.0/len(circles)
    
    for c in range(len(circles)):
        c_lerp = lerpColor(c_begin, c_end, gradient_step*c)
        cmap.append(c_lerp)
    
            
    # draw the lines
    circle_count = 0
    print(circles.keys())
    for rho_index, c in sorted(circles.items()):
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
        
            # filling with color gradient
            fill(cmap[circle_count])
            noStroke()
            beginShape()
            
            if rho_index == height/2 - 100 - offset:
                pass
            else:
                #print(rho_index)
                current_circle = circles[rho_index]
                next_circle = circles[rho_index + offset] #exception
                
                if k == len(c[:-1])-1: #last element
                    x1 = current_circle[k]['rho']*cos(math.pi/180*current_circle[k]['theta'])
                    y1 = current_circle[k]['rho']*sin(math.pi/180*current_circle[k]['theta'])
                    x2 = current_circle[-k-1]['rho']*cos(math.pi/180*current_circle[-k-1]['theta'])
                    y2 = current_circle[-k-1]['rho']*sin(math.pi/180*current_circle[-k-1]['theta'])
                    
                    x3 = next_circle[k]['rho']*cos(math.pi/180*next_circle[k]['theta'])
                    y3 = next_circle[k]['rho']*sin(math.pi/180*next_circle[k]['theta'])
                    x4 = next_circle[-k-1]['rho']*cos(math.pi/180*next_circle[-k-1]['theta'])
                    y4 = next_circle[-k-1]['rho']*sin(math.pi/180*next_circle[-k-1]['theta'])
                else:
                    x1 = current_circle[k]['rho']*cos(math.pi/180*current_circle[k]['theta'])
                    y1 = current_circle[k]['rho']*sin(math.pi/180*current_circle[k]['theta'])
                    x2 = current_circle[k+1]['rho']*cos(math.pi/180*current_circle[k+1]['theta'])
                    y2 = current_circle[k+1]['rho']*sin(math.pi/180*current_circle[k+1]['theta'])
                
                    x3 = next_circle[k]['rho']*cos(math.pi/180*next_circle[k]['theta'])
                    y3 = next_circle[k]['rho']*sin(math.pi/180*next_circle[k]['theta'])
                    x4 = next_circle[k+1]['rho']*cos(math.pi/180*next_circle[k+1]['theta'])
                    y4 = next_circle[k+1]['rho']*sin(math.pi/180*next_circle[k+1]['theta'])
                    
                vertex(x1, y1)
                vertex(x2, y2)
                vertex(x4, y4)
                vertex(x3, y3)
                endShape(CLOSE)
    
        circle_count += 1
        #save("joy_division_experiment_" + str(rnd.random()*1000) + ".png")
