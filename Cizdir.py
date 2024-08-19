#"execute if score @p Frames matches 10 run function applebad:frame10"
liste=[]
for i in range(0,6572):
    liste.append(f"execute if score @p Frames matches {i} run function applebad:frame{i}\n")
with open ("dosyaciz.mcfunction","w",encoding="utf-8") as dosya:
    for eleman in liste:
        dosya.write(eleman)
