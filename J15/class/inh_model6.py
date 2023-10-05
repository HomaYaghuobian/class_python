# 1:
class A:
    pass
class B(A):
    pass
class C(A):
    pass

# 2:
class A:
    pass
class B:
    pass
class C(A,B):
    pass

# 3:
class A:
    pass
class B(A):
    pass
class C(B):
    pass