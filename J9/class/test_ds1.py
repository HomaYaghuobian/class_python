# # ساختمان داده ها
# test_list = [] # list()
# test_set = set()
# test_tuple = () # tuple()
# test_dict = {} # dict()

colors = {'blue' ,'yellow' , 'black' , 'yellow'} #set
print(colors)
# colors[0] == yellow خطا میده

car_brands = ['BMW','Benz','mvm','mvm']
print(car_brands)
car_brands[0] = 'toyota'
print(car_brands)

# drink_brand = ('monster' ,'hype' , 'vigt30','red bull','TNT','TNT')
# print(type(drink_brand))
# # drink_brand[2] = 'TREX'   خطا
# print(drink_brand)

# books = { "karkhane shokolat sazi" : "roold dool" ,
#          "be zirzamin nazdik nasho" : "rl stine" ,
#          "it" : "steven king" ,
#          "rohe sag zoze mikeshad": "rl stine"}
# books["harry potest"] = "jk rolling"
# print(books)
# # کلید : مقدار

mydict = {
    "sadra" : 55,
    '"sina"' : 72,
    'navid' : 54,
    'mohammad' : 52,
    'pooria' : 90}
for param in mydict:
    print(param) # کلید ها مهم ترن برای همین اینجا نشون میده

#  .keys()
print(mydict.keys())
# .values()
print(mydict.values())
#  .items()
print(mydict.items())

for param in mydict.items():
    print(param[0],param[1])

for param in mydict.keys():
    print(param[0],param[1])