file = open('J12\exercise\movie.txt','r')
data = file.readlines()

def read_data():
    dict_data = {}
    for num_data in data:
        data2 = num_data.rstrip()
        name , i = data2.split(' ')
        dict_data[name] = i
    return dict_data

def add(dict):
    name = input('name: ')
    