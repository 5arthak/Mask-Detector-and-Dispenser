

# creating a object
#im = Image.open('C:/Users/Naman Pundir/Desktop/ubhack/no.jpg')
  
#im.show()

import matplotlib.pyplot as pl
import matplotlib.image as mpimg
import random
import cv2
#ax = plt.axes([0,0,1,1], frameon=False)
#fig = plt.figure(figsize=(1,1))
#ax.set_axis_off()
  

# Then we disable our xaxis and yaxis completely. If we just say plt.axis('off'),
# they are still used in the computation of the image padding.
im=pl.imread("C:/Users/Naman Pundir/Desktop/ubhack/no.jpg")
img = pl.imshow(im, interpolation='nearest')
# Even though our axes (plot region) are set to cover the whole image with [0,0,1,1],
# by default they leave padding between the plotted data and the frame. We use tigher=True
# to make sure the data gets scaled to the full extents of the axes.
pl.autoscale(tight=True)
while(True):
    
    counter = random.randint(1, 2)
    if counter==1:
        im=pl.imread("C:/Users/Naman Pundir/Desktop/ubhack/no.jpg")
        img.set_data(im)
    else:
        im=pl.imread("C:/Users/Naman Pundir/Desktop/ubhack/yes.jpg")
        img.set_data(im)
    pl.axis('off')
    pl.pause(.1)
    pl.draw()
        
    