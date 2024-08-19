from PIL import Image
import os
import time

start_time = time.time()
def resimolustur(framenum):
    framepath = f"C:\\Users\\user\\Desktop\\Bad Apple\\BadAppleFrames\\frame{framenum}.png"
    basx , basy=(0,0)
    sonx,sony=(0,0)
    with Image.open(framepath) as img:
        width, height = img.size
        pixels = img.load()
        frame_data = []
        bul=0
        for y in range(height):
            for x in range(width):                
                if(pixels[x,y][0]<255/2):
                    pixels[x,y]=(0, 0, 0)
                else:
                    pixels[x,y]=(255, 255, 255)
                
                if(pixels[x,y] != pixels[basx,basy]):
                    if(basy==y):
                        sonx,sony=(x-1,y)
                        if((basx,basy)!=(sonx,sony)):
                            frame_data.append(f"({basx},{basy}) // ({sonx},{sony}) // {pixels[basx,basy]} \n")
                    else:
                        sonx,sony=(width-1,y-1)
                        if((basx,basy)!=(sonx,sony)):
                            frame_data.append(f"({basx},{basy}) // ({sonx},{sony}) // {pixels[basx,basy]} \n")
                        if(x!=0):
                            basx,basy=(0,y)
                            sonx,sony=(x-1,y)
                            if((basx,basy)!=(sonx,sony)):
                                frame_data.append(f"({basx},{basy}) // ({sonx},{sony}) // {pixels[basx,basy]} \n")
                    basx,basy=(x,y)
                        
                if(x==width-1 and basx !=0 and basy==sony):
                    sonx,sony=(x,y)
                    if((basx,basy)!=(sonx,sony)):
                        frame_data.append(f"({basx},{basy}) // ({sonx},{sony}) // {pixels[basx,basy]} \n")
                    basx,basy=(0,y+1)
        if((sonx,sony)!=(width-1,height-1)):
            (sonx,sony)=(width-1,height-1)
            frame_data.append(f"({basx},{basy}) // ({sonx},{sony}) // {pixels[basx,basy]} \n")
        textpath = f"C:\\Users\\user\\Desktop\\Bad Apple\\BadAppleFramesRectangleText\\frame{framenum}.txt"
        with open(textpath, "w") as file:
            file.write("\n".join(frame_data))

for i in range(6572):
    resimolustur(i)
print(f"Execution time: {time.time() - start_time:.2f} seconds")
