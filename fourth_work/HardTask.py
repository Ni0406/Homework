from math import sqrt
#от сюда(Как то сложность домашки/проектов резко возросла)
chogs = []
results = {}
with open("123.txt", "r") as f:
    for pep in f.readlines():
        pep_split = pep.replace("\n", "").split(", ")
        book = pep_split[0]
        for chog in pep_split[1:]:
            chogs.append(int(chog))
            print(chogs)

        results[book] = chogs
        print(results)
#до сюда,всё то что успел сделать за 1,5 часа
input_rat = input()
input_rat_list = []
for value in input_rat.split(", "):
    input_rat_list.append(int(value))

for value in result:
    scalar_result += value

for value in input_ratings_list:
    length_first += value ** 2

for value in ratings_list:
    length_second += value ** 2

 cosine_distance = scalar_result / (sqrt(length_first)*sqrt(length_second))
    list_of_cosine_distances.append(cosine_distance)
    dict_with_cosine_results[cosine_distance] = name
#Cложна
