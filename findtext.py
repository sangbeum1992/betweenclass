import PIL
import numpy as np
 
# Read image
im = image.open( {'F:\\timetable\\1.jpg'} )
 
# Display image
im.show()
 
# Fetch image pixel data to numpy array
pix = np.array(im)