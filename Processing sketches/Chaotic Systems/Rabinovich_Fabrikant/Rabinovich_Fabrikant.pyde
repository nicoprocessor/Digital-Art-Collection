# model initial conditions
x = -1
y = 0
z = 0.5
t = 0

# model constants
_alpha = 0.3
gamma = 0.01

# gradients
palette_relaxing_red = [color(180, 15, 48), color(255, 251, 213)]
palette_shahabi = [color(104, 250, 0), color(166, 1, 116)]
palette_flare = [color(245, 174, 25), color(241, 40, 16)]
palette_rose_colored_lenses = [color(100, 112, 163), color(232, 203, 191)]
palette_mean_fruit = [color(247, 193, 158), color(219, 138, 222)]

theta = 0
running = True
points = []

frame_count = 0
scale_factor = 20.0
scale_factor_step = 0

initial_scale_factor = 20.0
final_scale_factor = 20.0
full_scale_time = 8.5 # in seconds
movie_length = 50 # in seconds


def setup():
    global scale_factor_step
    size(1200, 1200, P3D)
    ellipseMode(RADIUS)
    background(255)
    smooth()
    
    rescaling_frames = (movie_length - full_scale_time)*60
    rescaling_fps_frequency = (rescaling_frames * final_scale_factor)/initial_scale_factor
    scale_factor_step = 1/rescaling_fps_frequency
    
def eval_stroke_color(value,max_value,palette):        
    current_color = lerpColor(palette[1], palette[0], float(value)/max_value)    
    stroke(current_color)
    #noFill()
    fill(current_color)
    
def draw():
    global x,y,z,t,points,theta,frame_count,scale_factor
    strokeWeight(1)
    background(255)
    
    #camera positioning
    camera(40,40,200,
           0,0,0,
           0.0,1.0,0.0)
    
    # incremental resizing of the scene (fading)
    if frame_count < 60*full_scale_time:
        scale(initial_scale_factor)
    else:
        print("Scale factor: " + str(scale_factor))
        print(scale_factor_step)
        scale_factor -= scale_factor_step
        scale(scale_factor)
        
    # differential equations model
    dt = 0.02
    dx = (y * (z - 1 + x**2) + gamma * x)*dt
    dy = (x * (3 * z + 1 - x**2) + gamma * y)*dt
    dz = (-2 * z * (_alpha + x * y))*dt
    
    # increment derivatives
    x += dx
    y += dy
    z += dz
    t += dt
    
    p = PVector(x,y,z) 
    points.append(p)
    
    theta+=0.05
    rotateX(theta/5)
    rotateY(theta/2)
    #rotateZ(theta/3)
    
    beginShape()
    for p in points:
        strokeWeight(max(p.z * 100, 1.0))
        eval_stroke_color(p.z * 100,50,palette_flare)
        vertex(p.x, p.y, p.z)
    endShape()

    saveFrame("movie_2/rab_fabri_####.png")
    frame_count+=1
    print(frame_count)
    
    if frame_count >= movie_length*60:
        noLoop()

def keyPressed():
    global running
    save("lorentz" + str(random(1000)) + ".png")
    if running:
        noLoop()
        running = False
    else:
        loop()
        running = True
    print("Saved")
