class A:
    test1 = 'A: test1'  # puble
    __test3 = 'A: test3'  # private  توی خودش معنا داره
    _test4 = 'A: test4'  # protected  در کلاس خودم و فرزندم معنا میده

class B(A):
    test2 = 'B: test2'  

b = B()
print(b.test2)
print(b.test1)

a = A()
