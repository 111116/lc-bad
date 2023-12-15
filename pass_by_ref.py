import luisa
from luisa.mathtypes import *
luisa.init()


@luisa.func
def g(sampler, v):
    v.x = 322
    sampler = luisa.util.make_random_sampler(22,3456) # THIS SHOULD BE PROHIBITED
    a = sampler.next2f()

@luisa.func
def f(x):
    v = float3(1,2,3)
    s1 = luisa.util.make_random_sampler(123,3456)
    s2 = s1
    g(s2,v)
    print("v=",v)
    print(s2.next2f())
    print(s1.next2f())
    print(s1.next2f())

f(1, dispatch_size=1)