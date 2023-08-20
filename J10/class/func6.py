# دو لیست دریافت و بگه طولش برابره یا نه 

def check_len(l1,l2):
    len1 = len(l1)
    len2 = len(l2)

    if len1 == len2:
        return 'Equal'  #چون ریترن کرده باید بریزیش تو چیزی
    else:
        return ' Not Equal'

sadra_l = ['m','h','sh','n']
amirmahdi_l = ['a','s','d','sd','we']

javab = check_len(sadra_l,amirmahdi_l)
print(javab)