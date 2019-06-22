import math

square_size = 100
displacement_scale = 5
rotation_scale = 2
plus_or_minus = 0
offset = 2
threshold = 100

def setup():
    size(800, 800)
    for i in range(2,9):
        filename = "flower_" + str(i) + ".jpg"
        #filename = "demon.png"
        img = loadImage(filename)
        img.resize(width, height)
        smooth(4);
        #image(img, 0, 0)
        bg = img.copy()
        bg.filter(BLUR, 6)
        image(bg, 0, 0)
         #background(0)
        cells = {}
        
        # store each block of image in a list of sub-image
        for i in range(0, width - square_size, square_size):
            for j in range(0, height - square_size, square_size):
                img.loadPixels()
                
                current_cell = img.get(i, j, square_size, square_size)
                
                if threshold > 0:
                    current_cell.loadPixels()
                    brightness_sum = 0
                    for p in range(current_cell.height * current_cell.width):
                        brightness_sum += brightness(current_cell.pixels[p])
                    brightness_avg = brightness_sum/(current_cell.height * current_cell.width)
                    if brightness_avg > threshold:
                        cells[(i,j)] = current_cell
                else:
                    cells[(i,j)] = current_cell
                    
                
        for cell_key in cells:
            pushMatrix()
            i, j = cell_key[0], cell_key[1]
            plus_or_minus = -1 if random(10)/10 < 0.5 else 1
            rotation_jitter = (i*square_size*0.1 /height) * (math.pi/180) * plus_or_minus * random(10)/10 * rotation_scale
            
            plus_or_minus = -1 if random(10)/10 < 0.5 else 1
            translation_jitter = plus_or_minus * random(10)/10 * displacement_scale
            
            rotate(rotation_jitter)
            stroke(255)
            noFill()
            strokeWeight(3)
            rect(i + translation_jitter + offset -2, j + translation_jitter-2 + offset, square_size +2, square_size+2)
            image(cells[cell_key], i + translation_jitter + offset, j + translation_jitter + offset , square_size, square_size)
            popMatrix()
        
        #save("destructured_img_bg_blur_200_content_thres100_" + str(random(1000)) +filename+".png")
        #save("demon_destructured" + str(random(1000))+ ".png")
