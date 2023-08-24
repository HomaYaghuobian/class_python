# Kasr
def show_kasr(dict_kasr):
    print(dict_kasr['sorat'], '/' , dict_kasr['makhraj'])
A = {'sorat' : 2 ,
     'makhraj' : 5
}
print(A['sorat'])
print('-')
print(A['makhraj'])
B = {'sorat' : 4 ,
     'makhraj' : -8
}
show_kasr(B)

C = {'sorat' : A['sorat'] * B['sorat'],
     'makhraj' : A['makhraj'] * B['makhraj']}

show_kasr(C)

# watch


# complex numbers