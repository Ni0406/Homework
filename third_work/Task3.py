with open("file.xml", "r", encoding="utf-8") as file:
    list = file.read()

frsttag = "<a href=\""
scndtag = "\">"

links = []
frstindex = list.find(frsttag)
while frstindex != -1:
    scnd = list.find(scndtag, frstindex + len(frsttag))
    link = list[frstindex + len(frsttag):scnd]
    links.append(link)
    frstindex = list.find(frsttag, scnd)
    
for link in links:
    print(link)
