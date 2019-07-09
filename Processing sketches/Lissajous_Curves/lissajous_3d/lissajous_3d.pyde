import math

count = 0
t = 0
starting_threshold = 1000
threshold_count = 1000
count_inversion = False
A,B,a,b,delta=500,500,4,6,-1
t_increment=1e-3

color_palette = [color(26, 100, 188), color(185, 43, 39)]

def setup():
    size(1100, 1100)
    background(51)
    ellipseMode(CENTER)
    noStroke()
    smooth()
        
def eval_fill_color(start_c, end_c):
    global count
    current_color = lerpColor(start_c, end_c,float(count)/starting_threshold)    
    fill(current_color)

def draw():
    global t, count, count_inversion, threshold_count
    global color_palette
    translate(width/2, height/2)
    scale(1,-1)
    
    t+=t_increment
    x = A*sin(a*t+delta)
    y = B*sin(b*t)
    
    eval_fill_color(color_palette[0], color_palette[1])
    ellipse(x1,y1,50,50)
    
    if not count_inversion:
        if count < threshold_count:
            count_inversion = False
        else:
            count_inversion = True
            threshold_count = 0
    else:
        if count > threshold_count:
            count_inversion = True
        else:
            count_inversion = False
            threshold_count = starting_threshold
        
    if count_inversion:
        count -= 1
    else:
        count += 1
        
    print(count, count_inversion)

    
