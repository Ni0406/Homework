f = open("train.csv", "r")
a = f.readlines()
f.close()
male = "male"


count = 0
allive_male = 0
allive_female = 0

xb = []
for i in range(1, len(a)):
    xb = a[i].strip().split(",")
    if xb[1] == "1" and xb[5] == "male":
        allive_male += 1
    if xb[1] == "1" and xb[5] == "female":
        allive_female += 1

count = allive_female + allive_male
print(f" ALL survivors {count}")        
print(f" Survivors {allive_male} male")
print(f" Survivors {allive_female} female")      
