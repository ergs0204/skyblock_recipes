from os import walk
import json

def stripp(s):
    return s.replace("§a","").replace("§f","").replace("§9","").replace("§5","").replace("§c","").replace("§6","").replace("§3","").replace("§7","")

path="C:\\Users\\ASUS\\Desktop\\python\\skb_recipe\\items\\"
recipes={}
files = []
poss=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]


for (dirpath, dirnames, filenames) in walk(path):
    files.extend(filenames)
files.sort()
files=tuple(files)
#print(files)

for file in files:
    if ("GENERATOR" in file) or ("SACK" in file and "INK" not in file):
        print(file[:-4])
        continue
    data=json.load(open(path+file,"r",encoding="UTF-8"))
    if ("recipe" in data) and ("vanilla" not in data):
        name=stripp(data["displayname"])
        #print(name)
        ingre={}
        for pos in poss:
            if data["recipe"][pos]=="":
                continue
            iname,iamount=data["recipe"][pos].split(":")
            if iname+".json" in files:
                iname=stripp(json.load(open(path+iname+".json","r",encoding="UTF-8"))["displayname"])
            iamount=int(iamount)
            ingre.setdefault(iname, 0) 
            ingre[iname] = ingre[iname] + iamount 
        #print(ingre)
        recipes[name]=ingre

print(recipes)
print("Totally "+str(len(recipes)))