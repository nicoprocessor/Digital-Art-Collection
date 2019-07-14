add_library('peasycam')

# model initial conditions
x = 0.01
y = 0
z = 0
t = 0

# model constants
sigma = 10
rho = 28
beta = 8.0/3.0

# gradients
palette_relaxing_red = [color(180, 15, 48), color(255, 251, 213)]
palette_shahabi = [color(104, 250, 0), color(166, 1, 116)]
palette_flare = [color(245, 174, 25), color(241, 40, 16)]
palette_rose_colored_lenses = [color(100, 112, 163), color(232, 203, 191)]

theta = 0
running = True
points = []

def setup():
    global cam
    size(1200, 1200, P3D)
    ellipseMode(RADIUS)
    background(51)
    smooth()
    #cam = PeasyCam(this, 500)
    
def eval_stroke_color(value,max_value,palette):        
    current_color = lerpColor(palette[1], palette[0], float(value)/max_value)    
    stroke(current_color)
    noFill()
    #fill(current_color)
    
def draw():
    global x,y,z,t,points,theta,cam
    strokeWeight(10)
    background(51)
    
    camera(0,0,200,
           0,0,0,
           0.0,1.0,0.0)
    
    scale(1.3)
    # differential equations model
    dt = 0.007
    dx = (sigma * (y - x))*dt
    dy = (x * (rho - z) - y)*dt
    dz = (x * y - beta * z)*dt
    
    # increment derivatives
    x += dx
    y += dy
    z += dz
    t += dt
    
    p = PVector(x,y,z) 
    points.append(p)
    
    theta+=0.01
    #rotateX(theta/5)
    rotateY(theta/2)
    #rotateZ(theta)
    
    beginShape()
    for p in points:
        strokeWeight(max(p.z, 1.0))
        eval_stroke_color(p.z,50,palette_rose_colored_lenses)
        vertex(p.x, p.y, p.z)
    endShape()

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
