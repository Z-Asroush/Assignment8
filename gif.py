import os
import imageio

myfile=os.listdir('image2')

images=[]
for i in range (len(myfile)):
    image=imageio.imread('image2/'+myfile[i])
    images.append(image)

imageio.mimsave('mohsen2.gif', images)    