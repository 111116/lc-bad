import luisa
luisa.init()

@luisa.func
def f(a):
    print(a)

f((2,4), dispatch_size=1)
