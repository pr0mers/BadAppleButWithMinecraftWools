import time
bas=time.time()
def hazirla(framesay):
    inputfile=f"C:\\Users\\user\\Desktop\\Bad Apple\\BadAppleFramesRectangleText\\frame{framesay}.txt"
    outputfile=f"C:\\Users\\user\\Desktop\\Bad Apple\\BadAppleFramesRectangleMCfunction\\frame{framesay}.mcfunction"
    a=0
    liste=[]
    with open(inputfile,"r",encoding="utf-8") as dosya:
        for line in dosya:
            satir=line.split("//")
            i=0
            x1,x2,y1,y2,renk="","","","",""
            for deger in satir:
                if(deger=="\n"):
                    break
                if(i==0):
                    x1=deger.strip().strip("()").split(",")[0]
                    y1=deger.strip().strip("()").split(",")[1]
                if(i==1):
                    x2=deger.strip().strip("()").split(",")[0]
                    y2=deger.strip().strip("()").split(",")[1]
                if(i==2):
                    if(deger.strip().strip("()") == "255, 255, 255"):
                        renk="minecraft:white_wool"
                    elif(deger.strip().strip("()") == "0, 0, 0"):
                        renk="minecraft:black_wool"
                i=i+1
            if(x1!=""):
                liste.append(f"fill {x1} -61 {y1} {x2} -61 {y2} {renk}")
    with open(outputfile,"w",encoding="utf-8") as dosya:
        for eleman in liste:
            dosya.write(eleman+"\n")

for i in range (0,6572):
    hazirla(i)
print(f"{time.time()-bas} saniye kadar sürdü")
