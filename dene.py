import pandas
# a={'english': {0: 'you', 1: 'bang', 2: 'the'}, 'turkish': {0: 'Sen', 1: 'Ben', 2: 'bir'}}
# print(a)
# del a["english"][2]
# del a["turkish"][2]
# print(a)

data=pandas.read_csv("./data/french_words.csv")
print(data["French"])
Fransiz=data["French"].to_list()
print(Fransiz)

# import csv
# with open("./data/french_words.csv") as file:
#     data=csv.reader(file)
#     temp=[]
#     for i in data:
#         temp.append(i[1])
#     print(temp)
