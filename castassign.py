from sys import argv
import luisa
luisa.init(None if len(argv)<=1 else argv[1])

@luisa.func
def f():
    a = luisa.float3()
    b = 1.0
    a = b

f(dispatch_size=1)
