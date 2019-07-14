import math

count = 0
starting_threshold = 1000
threshold_count = 1000
count_inversion = False
t = 0
A=500
B=500
a=6
b=4
delta = 3
t_increment=3*1e-3

def setup():
    size(1200, 1200)
    background(51)
    ellipseMode(CENTER)
    noStroke()
    smooth()
        
def eval_fill_color():
    global count
    start_color = color(185, 43, 39)
    end_color = color(26, 100, 188)
        
    current_color = lerpColor(start_color, end_color,float(count)/starting_threshold)    
    fill(current_color)

def draw():
    global t, count, count_inversion, threshold_count
    translate(width/2, height/2)
    scale(1,-1)
    
    t+=t_increment
    x = A*sin(a*t+delta)
    y = B*sin(b*t)
    eval_fill_color()
    
    ellipse(x,y,50,50)
    
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

def keyPressed():
    save("lissajous" + str(random(1000)))
    print("Saved")
    
