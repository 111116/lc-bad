from sys import argv
import luisa
luisa.init(None if len(argv)<=1 else argv[1])

@luisa.func
def f():
    if dispatch_id().x == 999:
    #if False:
        a = 0
    else:
        a = 0.5
    print('a:', a)

f(dispatch_size=1)
# Result: a: 0
