import math

count = 0
t = 0
total_points = 1e4
starting_threshold = 1000
threshold_count = 1000
count_inversion = False
A,B,C,a,b,c,delta=500,500,1000,4,6,5,-1
t_increment=3 *1e-3

#color_palette = [color(26, 100, 188), color(185, 43, 39)]
color_palette= [color(241, 40, 16), color(245, 175, 25)]

def setup():
    size(1100, 1100, P3D)
    background(51)
    ellipseMode(CENTER)
    strokeWeight(10)
    smooth()
        
def eval_fill_color(start_c, end_c):
    global count
    current_color = lerpColor(start_c, end_c,float(count)/starting_threshold)    
    stroke(current_color)

def draw():
    global t, count, count_inversion, threshold_count
    global color_palette
    
    translate(width/2, height/2,0)
    camera(0, 0, height*2,
           0, 0, 0,
           0, 1, 0)
    
    if count < total_points:
        pushMatrix()
        t+=t_increment
        x = A*sin(a*t+delta)
        y = B*sin(b*t)
        z = C*sin(c*t)
    
        z_persp = z + 1000
        strokeWeight(max(5,z_persp/50))
        
        eval_fill_color(color_palette[0], color_palette[1])
        point(x,y,z)
        popMatrix()
        
        # gradient controls
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
    
