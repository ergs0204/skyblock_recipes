from os import walk
import json

def stripp(s):
    return s.replace("§a","").replace("§f","").replace("§9","").replace("§5","").replace("§c","").replace("§6","").replace("§3","").replace("§7","")

path="C:\\Users\\ASUS\\Desktop\\python\\skb_recipe\\items\\"

files=[]
for (dirpath, dirnames, filenames) in walk(path):
    files.extend(filenames)
files.sort()
files=tuple(files)
#print(files)
vanilla={}

for file in files:
    data=json.load(open(path+file,"r",encoding="UTF-8"))
    if "vanilla" in data:
        name=stripp(data["displayname"])
        print(name)
        vanilla[name]=True

print(vanilla)
print("Totally "+str(len(vanilla)))

f=open("vanilla.json","w",encoding="utf-8")
json.dump(vanilla,f)