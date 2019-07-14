import math

count = 0
t = 0
starting_threshold = 1000
threshold_count = 1000
count_inversion = False
A1,B1,a1,b1,delta1=350,350,4,6,-1
A2,B2,a2,b2,delta2=350,350,6,4,1
t_increment=3*o1e-3

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
    x1 = A1*sin(a1*t+delta1)
    y1 = B1*sin(b1*t)
    
    y2 = A2*sin(a2*t+delta2)
    x2 = B2*sin(b2*t)
    
    eval_fill_color(color_palette[0], color_palette[1])
    ellipse(x1,y1,40,40)
    
    eval_fill_color(color_palette[1], color_palette[0])
    ellipse(x2,y2,40,40)
    
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
    save("lissajous" + str(random(1000)) + ".png")
    print("Saved")
    
